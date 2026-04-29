# technician_manager.py
"""
Technician management dashboard for the Fuel Automation System.
Place this file in the same folder as east_auto.py and technicians.py
"""
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
import csv
from datetime import datetime
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass
from functools import lru_cache
import re

# Import your existing technicians data
try:
    from technicians import REGION_MAPPINGS
except ImportError:
    # Fallback if technicians.py not found
    REGION_MAPPINGS = {}
    print("WARNING: technicians.py not found. Using empty mappings.")

@dataclass(frozen=True)
class TechnicianAssignment:
    """Immutable technician assignment record."""
    site_id: str
    technician_name: str
    region: str

class TechnicianManager:
    """
    Manages technician lookups with caching and multiple strategies.
    """
    
    def __init__(self, region_mappings: Dict[str, Dict[str, str]]):
        self.region_mappings = region_mappings
        self._build_indices()
        self.stats = {
            'exact_matches': 0,
            'prefixed_matches': 0,
            'suffix_matches': 0,
            'no_matches': 0
        }
        
    def _build_indices(self):
        """Build search indices for fast lookups."""
        self.exact_match: Dict[str, TechnicianAssignment] = {}
        self.suffix_match: Dict[str, List[TechnicianAssignment]] = {}
        self.technician_to_sites: Dict[str, List[str]] = {}
        self.all_technicians = set()
        
        for region, mapping in self.region_mappings.items():
            for site_id, tech_name in mapping.items():
                # Clean and normalize
                site_id = site_id.strip().upper()
                tech_name = tech_name.strip().upper()
                
                # Create assignment
                assignment = TechnicianAssignment(
                    site_id=site_id,
                    technician_name=tech_name,
                    region=region
                )
                
                # Exact match index
                self.exact_match[site_id] = assignment
                
                # Suffix index (for numbers like "001M")
                suffix = self._extract_suffix(site_id)
                if suffix:
                    if suffix not in self.suffix_match:
                        self.suffix_match[suffix] = []
                    self.suffix_match[suffix].append(assignment)
                
                # Reverse index (technician -> sites)
                if tech_name not in self.technician_to_sites:
                    self.technician_to_sites[tech_name] = []
                self.technician_to_sites[tech_name].append(site_id)
                self.all_technicians.add(tech_name)
    
    def _extract_suffix(self, site_id: str) -> Optional[str]:
        """Extract the numeric suffix from a site ID."""
        match = re.search(r'(\d+[A-Z]?)$', site_id)
        return match.group(1) if match else None
    
    @lru_cache(maxsize=500)
    def get_technician(self, site_id: str, context: str = "") -> Optional[TechnicianAssignment]:
        """Get technician for a site ID."""
        if not site_id:
            return None
            
        site_id = site_id.strip().upper()
        
        # Strategy 1: Exact match
        if site_id in self.exact_match:
            self.stats['exact_matches'] += 1
            return self.exact_match[site_id]
        
        # Strategy 2: Try with prefix
        if not site_id.startswith('IHS_'):
            for prefix in ['IHS_CBT_', 'IHS_NRW_', 'IHS_EST_']:
                prefixed = f"{prefix}{site_id}"
                if prefixed in self.exact_match:
                    self.stats['prefixed_matches'] += 1
                    return self.exact_match[prefixed]
        
        # Strategy 3: Suffix matching
        suffix = self._extract_suffix(site_id)
        if suffix and suffix in self.suffix_match:
            assignments = self.suffix_match[suffix]
            # If context provided, try to match by region
            if context and len(assignments) > 1:
                for a in assignments:
                    if a.region == context:
                        self.stats['suffix_matches'] += 1
                        return a
            self.stats['suffix_matches'] += 1
            return assignments[0]
        
        self.stats['no_matches'] += 1
        return None
    
    def get_technician_name(self, site_id: str, context: str = "") -> str:
        """Get just the technician name."""
        assignment = self.get_technician(site_id, context)
        return assignment.technician_name if assignment else ""
    
    def validate_technician(self, name: str) -> bool:
        """Check if technician exists."""
        return name.strip().upper() in self.all_technicians

class TechnicianManagerGUI:
    """GUI for managing technician assignments."""
    
    def __init__(self, parent):
        self.manager = TechnicianManager(REGION_MAPPINGS)
        self.parent = parent
        self.top = tk.Toplevel(parent)
        self.top.title("Technician Manager")
        self.top.geometry("900x600")
        
        self._setup_ui()
        self._load_data()
        
    def _setup_ui(self):
        # Main container
        main = ttk.Frame(self.top, padding=10)
        main.pack(fill='both', expand=True)
        
        # Stats bar at top
        stats_frame = ttk.Frame(main)
        stats_frame.pack(fill='x', pady=5)
        
        self.stats_label = ttk.Label(stats_frame, text="Loading statistics...", font=('Arial', 10, 'bold'))
        self.stats_label.pack(side='left')
        
        # Search frame
        search_frame = ttk.LabelFrame(main, text="Search", padding=10)
        search_frame.pack(fill='x', pady=10)
        
        # Search by Site
        ttk.Label(search_frame, text="Search by Site ID:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.site_search = ttk.Entry(search_frame, width=30)
        self.site_search.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(search_frame, text="Search Site", command=self.search_site).grid(row=0, column=2, padx=5, pady=5)
        
        # Search by Technician
        ttk.Label(search_frame, text="Search by Technician:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.tech_search = ttk.Entry(search_frame, width=30)
        self.tech_search.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(search_frame, text="Show Sites", command=self.show_technician_sites).grid(row=1, column=2, padx=5, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(main, text="Assignments", padding=10)
        results_frame.pack(fill='both', expand=True, pady=10)
        
        # Treeview for results
        columns = ('site_id', 'technician', 'region')
        self.tree = ttk.Treeview(results_frame, columns=columns, show='headings', height=15)
        
        self.tree.heading('site_id', text='Site ID')
        self.tree.heading('technician', text='Technician')
        self.tree.heading('region', text='Region')
        
        self.tree.column('site_id', width=250)
        self.tree.column('technician', width=150)
        self.tree.column('region', width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Button frame
        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill='x', pady=10)
        
        ttk.Button(btn_frame, text="Refresh All", command=self._load_data).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Export to CSV", command=self.export_data).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="View Statistics", command=self.show_stats).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Close", command=self.top.destroy).pack(side='right', padx=5)
    
    def _load_data(self):
        """Load all assignments into tree."""
        # Clear existing
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load from manager
        for region, mapping in self.manager.region_mappings.items():
            for site_id, tech in mapping.items():
                self.tree.insert('', 'end', values=(
                    site_id,
                    tech,
                    region
                ))
        
        # Update stats
        self._update_stats()
    
    def _update_stats(self):
        """Update statistics display."""
        total_sites = len(self.manager.exact_match)
        total_techs = len(self.manager.all_technicians)
        
        # Calculate region counts
        region_counts = {}
        for region, mapping in self.manager.region_mappings.items():
            region_counts[region] = len(mapping)
        
        stats_text = f"📊 Total Sites: {total_sites} | 👥 Technicians: {total_techs}"
        for region, count in region_counts.items():
            stats_text += f" | {region.upper()}: {count}"
        
        self.stats_label.config(text=stats_text)
    
    def search_site(self):
        """Search for a specific site."""
        site_id = self.site_search.get().strip()
        if not site_id:
            messagebox.showwarning("Warning", "Please enter a site ID")
            return
        
        assignment = self.manager.get_technician(site_id)
        if assignment:
            # Clear and show only this site
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            self.tree.insert('', 'end', values=(
                assignment.site_id,
                assignment.technician_name,
                assignment.region
            ))
            
            messagebox.showinfo("Found", f"Site found! Technician: {assignment.technician_name}")
        else:
            messagebox.showwarning("Not Found", f"No technician found for site: {site_id}")
    
    def show_technician_sites(self):
        """Show all sites for a technician."""
        tech_name = self.tech_search.get().strip().upper()
        if not tech_name:
            messagebox.showwarning("Warning", "Please enter a technician name")
            return
        
        # Clear current view
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Find all sites for this technician
        count = 0
        for region, mapping in self.manager.region_mappings.items():
            for site_id, tech in mapping.items():
                if tech.upper() == tech_name:
                    self.tree.insert('', 'end', values=(
                        site_id,
                        tech,
                        region
                    ))
                    count += 1
        
        if count > 0:
            messagebox.showinfo("Found", f"Found {count} sites for technician: {tech_name}")
        else:
            messagebox.showwarning("Not Found", f"No sites found for technician: {tech_name}")
            # Reload all data
            self._load_data()
    
    def export_data(self):
        """Export all assignments to CSV."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"technician_assignments_{timestamp}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Site ID', 'Technician', 'Region'])
                
                for region, mapping in self.manager.region_mappings.items():
                    for site_id, tech in mapping.items():
                        writer.writerow([site_id, tech, region])
            
            messagebox.showinfo("Success", f"Data exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def show_stats(self):
        """Show detailed statistics."""
        stats = self.manager.stats
        total_lookups = sum(stats.values())
        
        stats_text = f"""TECHNICIAN STATISTICS
{'='*40}

Total Sites: {len(self.manager.exact_match)}
Total Technicians: {len(self.manager.all_technicians)}

Lookup Performance:
- Exact Matches: {stats['exact_matches']}
- Prefixed Matches: {stats['prefixed_matches']}
- Suffix Matches: {stats['suffix_matches']}
- No Matches: {stats['no_matches']}
- Total Lookups: {total_lookups}

Region Breakdown:"""
        
        for region, mapping in self.manager.region_mappings.items():
            stats_text += f"\n- {region.upper()}: {len(mapping)} sites"
        
        messagebox.showinfo("Statistics", stats_text)

# Create a global instance for use in main app
TECHNICIAN_MANAGER = TechnicianManager(REGION_MAPPINGS)