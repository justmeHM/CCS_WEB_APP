"""
Multi-Report Parser Modules
Handles Old CCS, NRW, and Eastern reports without modifying existing code
"""

import re
import logging
from datetime import datetime
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass

# Assuming these are imported from your existing modules
# from config import Config
# from data_normalizer import DataNormalizer
# from technician_mapper import TechnicianMapper


# ============================================================================
# OLD CCS PARSER MODULE
# ============================================================================

@dataclass
class OldCCSConfig:
    """Configuration for Old CCS Report"""
    excel_file: str = r"C:\Users\HARRISON MWEWA\Desktop\whatsapp_2_excel\old ccs report.xlsx"
    sheet_name: str = "fuel report"
    
    # Field variations for Old CCS format
    field_patterns = {
        "DATE": [r"Date\s*[:=]?\s*(\d{1,2}/\d{1,2}/\d{2,4})", r"Date\s+(\d{1,2}/\d{1,2}/\d{2,4})"],
        "SITE_NAME": [r"(?:Site name|Site ID).*?(?:CBT|Cbt|cbt)\s*(\d+[A-Z]?)", r"([A-Za-z\s]+)\s+CBT"],
        "SITE_ID": [r"(?:CBT|Cbt|cbt)\s*[=:]?\s*(\d+[A-Z]?)", r"Site ID\s*[:=]?\s*(?:CBT|Cbt|cbt)\s*(\d+[A-Z]?)"],
        "RUNTIME": [
            r"RT\s*[:=]\s*(\d+|fault|faulty)",
            r"Run(?:\s+T|t)ime\s*[:=]\s*(\d+|fault|faulty)",
            r"GD\s+Run\s+Time\s*[:=]\s*(\d+|fault|faulty)"
        ],
        "PREV_RUNTIME": [r"Previous\s+(?:GD\s+)?(?:Run\s*)?[Tt]ime\s*[:=]?\s*(\d+|fault|faulty)"],
        "INITIAL": [
            r"Initial\s*(?:fuel\s+level)?\s*[:=]\s*(\d+)",
            r"Found\s*[:=]?\s*(\d+)"
        ],
        "ADDED": [
            r"Added\s*[:=]\s*(\d+)",
            r"Fuel\s+added\s*[:=]\s*(\d+)"
        ],
        "FINAL": [
            r"(?:Final|Total)\s*(?:fuel\s+level)?\s*[:=]\s*(\d+)"
        ],
        "CPH": [r"CPH\s*[:=]\s*([\d.]+|Lh)"],
        "SUPPLIER": [
            r"Fuel\s+source\s*[:=]?\s*(Meru|MERU|Puma|PUMA|meru|puma|lake\s+oil|CCS|Sahara|Total)",
            r"Source\s*[:=]?\s*(Meru|MERU|Puma|PUMA|meru|puma|CCS)"
        ]
    }


class OldCCSParser:
    """Parser for Old CCS Report format"""
    
    def __init__(self, config: OldCCSConfig):
        self.config = config
        self.site_pattern = re.compile(r"(?:CBT|Cbt|cbt)\s*[=:]?\s*(\d+[A-Z]?)", re.IGNORECASE)
    
    def parse_file(self, 
                   file_path: str, 
                   error_logger: Optional[Callable] = None,
                   progress_callback: Optional[Callable] = None) -> tuple:
        """Parse Old CCS chat file"""
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Split by date patterns as blocks
        blocks = self._split_into_blocks(content)
        entries = []
        unmatched_blocks = []
        skipped_count = 0
        
        total_blocks = len(blocks)
        
        for idx, block in enumerate(blocks):
            if progress_callback:
                progress = int((idx / total_blocks) * 40) + 20
                progress_callback(progress)
            
            result = self._parse_block(block, idx)
            
            if result is None or 'error' in result:
                skipped_count += 1
                reason = result.get('error', 'Parse failed') if result else 'Empty block'
                unmatched_blocks.append({
                    'reason': reason,
                    'content': block
                })
                if error_logger:
                    error_logger(f"❌ Old CCS Block {idx + 1}: {reason}")
                continue
            
            entries.append(result)
            logging.info(f"✅ Old CCS Block {idx + 1}: Parsed {result.get('SITE ID', 'Unknown')}")
        
        logging.info(f"📊 Old CCS: {len(entries)} valid entries, {skipped_count} skipped")
        
        return entries, skipped_count, unmatched_blocks
    
    def _split_into_blocks(self, content: str) -> List[str]:
        """Split content into individual refueling blocks"""
        # Split by date patterns
        date_pattern = r"(?=Date\s*[:=]?\s*\d{1,2}/\d{1,2}/\d{2,4})"
        blocks = re.split(date_pattern, content, flags=re.IGNORECASE)
        return [b.strip() for b in blocks if b.strip() and len(b) > 20]
    
    def _parse_block(self, block: str, block_idx: int) -> Optional[Dict]:
        """Parse a single Old CCS block"""
        data = {}
        
        # Extract date
        date_match = re.search(self.config.field_patterns["DATE"][0], block, re.IGNORECASE)
        if not date_match:
            return {'error': 'No valid date found'}
        
        date_str = date_match.group(1)
        try:
            dt = datetime.strptime(date_str, "%d/%m/%y")
        except ValueError:
            try:
                dt = datetime.strptime(date_str, "%d/%m/%Y")
            except ValueError:
                return {'error': 'Invalid date format'}
        
        data["CURRENT VISIT DATE"] = dt.strftime("%d/%m/%Y")
        
        # Extract Site ID
        site_match = self.site_pattern.search(block)
        if not site_match:
            return {'error': 'No valid SITE ID'}
        
        site_id = f"IHS_CBT_{site_match.group(1).upper()}"
        data["SITE ID"] = site_id
        
        # Extract site name (try to get text before CBT)
        name_patterns = [
            r"([A-Za-z\s]+?)\s+(?:CBT|Cbt|cbt)",
            r"Site\s+name\s*[:=]\s*([A-Za-z\s]+)"
        ]
        for pattern in name_patterns:
            name_match = re.search(pattern, block, re.IGNORECASE)
            if name_match:
                data["SITE NAME"] = name_match.group(1).strip()
                break
        
        if "SITE NAME" not in data:
            data["SITE NAME"] = ""
        
        # Extract Runtime
        for pattern in self.config.field_patterns["RUNTIME"]:
            rt_match = re.search(pattern, block, re.IGNORECASE)
            if rt_match:
                rt_val = rt_match.group(1).strip()
                if rt_val.lower() in ['fault', 'faulty']:
                    data["CURRENT DG RUN HOURS"] = "FAULTY"
                else:
                    try:
                        data["CURRENT DG RUN HOURS"] = int(rt_val)
                    except ValueError:
                        data["CURRENT DG RUN HOURS"] = "FAULTY"
                break
        
        # Extract Previous Runtime
        for pattern in self.config.field_patterns["PREV_RUNTIME"]:
            prev_rt_match = re.search(pattern, block, re.IGNORECASE)
            if prev_rt_match:
                prev_val = prev_rt_match.group(1).strip()
                if prev_val.lower() not in ['fault', 'faulty']:
                    try:
                        data["PREVIOUS DG RUN HOURS"] = int(prev_val)
                    except ValueError:
                        pass
                break
        
        # Extract Initial/Found fuel
        for pattern in self.config.field_patterns["INITIAL"]:
            init_match = re.search(pattern, block, re.IGNORECASE)
            if init_match:
                try:
                    data["FUEL FOUND"] = int(init_match.group(1))
                except ValueError:
                    pass
                break
        
        # Extract Added fuel
        for pattern in self.config.field_patterns["ADDED"]:
            added_match = re.search(pattern, block, re.IGNORECASE)
            if added_match:
                try:
                    data["FUEL ADDED"] = int(added_match.group(1))
                except ValueError:
                    pass
                break
        
        # Extract Final/Total fuel
        for pattern in self.config.field_patterns["FINAL"]:
            final_match = re.search(pattern, block, re.IGNORECASE)
            if final_match:
                try:
                    data["FUEL LEFT ON SITE"] = int(final_match.group(1))
                except ValueError:
                    pass
                break
        
        # Extract CPH
        for pattern in self.config.field_patterns["CPH"]:
            cph_match = re.search(pattern, block, re.IGNORECASE)
            if cph_match:
                cph_val = cph_match.group(1).strip()
                if cph_val.lower() != 'lh':
                    try:
                        data["CPH"] = float(cph_val)
                    except ValueError:
                        pass
                break
        
        # Extract Supplier
        for pattern in self.config.field_patterns["SUPPLIER"]:
            supplier_match = re.search(pattern, block, re.IGNORECASE)
            if supplier_match:
                data["SUPPLIER"] = supplier_match.group(1).upper()
                break
        
        # Map technician (if you have a mapping)
        data["NAME OF TECHNICIAN"] = "N/A"  # Update with actual mapping if available
        
        return data


# ============================================================================
# NRW PARSER MODULE
# ============================================================================

@dataclass
class NRWConfig:
    """Configuration for NRW Report"""
    excel_file: str = r"C:\Users\HARRISON MWEWA\Desktop\whatsapp_2_excel\nrw report.xlsx"
    sheet_name: str = "fuel report"


class NRWParser:
    """Parser for NRW Report format"""
    
    def __init__(self, config: NRWConfig):
        self.config = config
        self.site_pattern = re.compile(
            r"(?:NRW|nrw|Nrw)[\s_-]*(\d+[A-Z]?)|"
            r"(?:IHS[\s_-]*)?NRW[\s_-]*(\d+[A-Z]?)", 
            re.IGNORECASE
        )
    
    def parse_file(self, 
                   file_path: str, 
                   error_logger: Optional[Callable] = None,
                   progress_callback: Optional[Callable] = None) -> tuple:
        """Parse NRW chat file"""
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        blocks = self._split_into_blocks(content)
        entries = []
        unmatched_blocks = []
        skipped_count = 0
        
        total_blocks = len(blocks)
        
        for idx, block in enumerate(blocks):
            if progress_callback:
                progress = int((idx / total_blocks) * 40) + 20
                progress_callback(progress)
            
            result = self._parse_block(block, idx)
            
            if result is None or 'error' in result:
                skipped_count += 1
                reason = result.get('error', 'Parse failed') if result else 'Empty block'
                unmatched_blocks.append({
                    'reason': reason,
                    'content': block
                })
                if error_logger:
                    error_logger(f"❌ NRW Block {idx + 1}: {reason}")
                continue
            
            entries.append(result)
            logging.info(f"✅ NRW Block {idx + 1}: Parsed {result.get('SITE ID', 'Unknown')}")
        
        logging.info(f"📊 NRW: {len(entries)} valid entries, {skipped_count} skipped")
        
        return entries, skipped_count, unmatched_blocks
    
    def _split_into_blocks(self, content: str) -> List[str]:
        """Split content into individual refueling blocks"""
        # Split by date or site ID patterns
        date_pattern = r"(?=Date\s*[:=]?\s*\d{1,2}/\d{1,2}/\d{2,4})|(?=\d{1,2}/\d{1,2}/\d{2,4})"
        blocks = re.split(date_pattern, content, flags=re.IGNORECASE)
        return [b.strip() for b in blocks if b.strip() and len(b) > 20]
    
    def _parse_block(self, block: str, block_idx: int) -> Optional[Dict]:
        """Parse a single NRW block"""
        data = {}
        
        # Extract date - NRW uses various formats
        date_patterns = [
            r"Date\s*[:=]?\s*(\d{1,2}/\d{1,2}/\d{2,4})",
            r"(\d{1,2}/\d{1,2}/\d{2,4})",
            r"Date\s*[:=]\s*(\d{1,2}/\d{1,2}/\d{2})"
        ]
        
        date_found = False
        for pattern in date_patterns:
            date_match = re.search(pattern, block, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(1)
                try:
                    dt = datetime.strptime(date_str, "%d/%m/%y")
                    data["CURRENT VISIT DATE"] = dt.strftime("%d/%m/%Y")
                    date_found = True
                    break
                except ValueError:
                    try:
                        dt = datetime.strptime(date_str, "%d/%m/%Y")
                        data["CURRENT VISIT DATE"] = dt.strftime("%d/%m/%Y")
                        date_found = True
                        break
                    except ValueError:
                        continue
        
        if not date_found:
            return {'error': 'No valid date found'}
        
        # Extract Site ID (NRW format)
        site_match = self.site_pattern.search(block)
        if not site_match:
            return {'error': 'No valid SITE ID'}
        
        # Get the matched group (either group 1 or 2)
        site_num = site_match.group(1) or site_match.group(2)
        site_id = f"IHS_NRW_{site_num.upper()}"
        data["SITE ID"] = site_id
        
        # Extract site name
        name_patterns = [
            r"Site\s+(?:name|I[\'d])\s*[:=]?\s*([A-Za-z\s]+?)(?:\n|GD|RT|Fuel|$)",
            r"([A-Za-z\s]+?)\s+(?:NRW|nrw)"
        ]
        for pattern in name_patterns:
            name_match = re.search(pattern, block, re.IGNORECASE)
            if name_match:
                data["SITE NAME"] = name_match.group(1).strip()
                break
        
        if "SITE NAME" not in data:
            data["SITE NAME"] = ""
        
        # Extract Runtime
        rt_patterns = [
            r"(?:RT|GD\s+Run\s+Time|Run\s+Time)\s*[:=]?\s*(\d+|fault|faulty)",
            r"DG\s+RT\s*[:=]?\s*(\d+|fault|faulty)"
        ]
        for pattern in rt_patterns:
            rt_match = re.search(pattern, block, re.IGNORECASE)
            if rt_match:
                rt_val = rt_match.group(1).strip()
                if rt_val.lower() in ['fault', 'faulty']:
                    data["CURRENT DG RUN HOURS"] = "FAULTY"
                else:
                    try:
                        data["CURRENT DG RUN HOURS"] = int(rt_val)
                    except ValueError:
                        data["CURRENT DG RUN HOURS"] = "FAULTY"
                break
        
        # Extract fuel data
        found_patterns = [
            r"(?:Found|Fuel\s+found|Initial\s+fuel\s+level)\s*[:=]?\s*(\d+)",
            r"Intial\s+dp\s*[:=]?\s*(\d+)"  # Common typo in data
        ]
        for pattern in found_patterns:
            found_match = re.search(pattern, block, re.IGNORECASE)
            if found_match:
                try:
                    data["FUEL FOUND"] = int(found_match.group(1))
                except ValueError:
                    pass
                break
        
        added_patterns = [
            r"(?:Added|Fuel\s+added)\s*[:=]?\s*(\d+)"
        ]
        for pattern in added_patterns:
            added_match = re.search(pattern, block, re.IGNORECASE)
            if added_match:
                try:
                    data["FUEL ADDED"] = int(added_match.group(1))
                except ValueError:
                    pass
                break
        
        # Extract CPH
        cph_patterns = [r"CPH\s*[:=]?\s*([\d.]+|Lh)"]
        for pattern in cph_patterns:
            cph_match = re.search(pattern, block, re.IGNORECASE)
            if cph_match:
                cph_val = cph_match.group(1).strip()
                if cph_val.lower() != 'lh':
                    try:
                        data["CPH"] = float(cph_val)
                    except ValueError:
                        pass
                break
        
        # Extract Supplier
        supplier_patterns = [
            r"Fuel\s+source\s*[:=]?\s*(Meru|MERU|Puma|PUMA|CCS|meru|puma)",
            r"Source\s*[:=]?\s*(Meru|MERU|Puma|PUMA|CCS)"
        ]
        for pattern in supplier_patterns:
            supplier_match = re.search(pattern, block, re.IGNORECASE)
            if supplier_match:
                data["SUPPLIER"] = supplier_match.group(1).upper()
                break
        
        data["NAME OF TECHNICIAN"] = "N/A"
        
        return data


# ============================================================================
# EASTERN PARSER MODULE
# ============================================================================

@dataclass
class EasternConfig:
    """Configuration for Eastern Report"""
    excel_file: str = r"C:\Users\HARRISON MWEWA\Desktop\whatsapp_2_excel\eastern report.xlsx"
    sheet_name: str = "fuel capture"


class EasternParser:
    """Parser for Eastern Report format"""
    
    def __init__(self, config: EasternConfig):
        self.config = config
        self.site_pattern = re.compile(
            r"(?:EST|est|Est)[\s_:-]*(\d+[A-Z]?)|"
            r"(?:IHS[\s_-]*)?EST[\s_:-]*(\d+[A-Z]?)", 
            re.IGNORECASE
        )
    
    def parse_file(self, 
                   file_path: str, 
                   error_logger: Optional[Callable] = None,
                   progress_callback: Optional[Callable] = None) -> tuple:
        """Parse Eastern chat file"""
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        blocks = self._split_into_blocks(content)
        entries = []
        unmatched_blocks = []
        skipped_count = 0
        
        total_blocks = len(blocks)
        
        for idx, block in enumerate(blocks):
            if progress_callback:
                progress = int((idx / total_blocks) * 40) + 20
                progress_callback(progress)
            
            result = self._parse_block(block, idx)
            
            if result is None or 'error' in result:
                skipped_count += 1
                reason = result.get('error', 'Parse failed') if result else 'Empty block'
                unmatched_blocks.append({
                    'reason': reason,
                    'content': block
                })
                if error_logger:
                    error_logger(f"❌ Eastern Block {idx + 1}: {reason}")
                continue
            
            entries.append(result)
            logging.info(f"✅ Eastern Block {idx + 1}: Parsed {result.get('SITE ID', 'Unknown')}")
        
        logging.info(f"📊 Eastern: {len(entries)} valid entries, {skipped_count} skipped")
        
        return entries, skipped_count, unmatched_blocks
    
    def _split_into_blocks(self, content: str) -> List[str]:
        """Split content into individual refueling blocks"""
        date_pattern = r"(?=Date\s*[:=]?\s*\d{1,2}/\d{1,2}/\d{2,4})"
        blocks = re.split(date_pattern, content, flags=re.IGNORECASE)
        return [b.strip() for b in blocks if b.strip() and len(b) > 20]
    
    def _parse_block(self, block: str, block_idx: int) -> Optional[Dict]:
        """Parse a single Eastern block"""
        data = {}
        
        # Extract date
        date_patterns = [
            r"Date\s*[:=]?\s*(\d{1,2}/\d{1,2}/\d{2,4})",
            r"Date\s*[:=]\s*(\d{1,2}/\d{1,2}/\d{2})"
        ]
        
        date_found = False
        for pattern in date_patterns:
            date_match = re.search(pattern, block, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(1)
                try:
                    dt = datetime.strptime(date_str, "%d/%m/%y")
                    data["CURRENT VISIT DATE"] = dt.strftime("%d/%m/%Y")
                    date_found = True
                    break
                except ValueError:
                    try:
                        dt = datetime.strptime(date_str, "%d/%m/%Y")
                        data["CURRENT VISIT DATE"] = dt.strftime("%d/%m/%Y")
                        date_found = True
                        break
                    except ValueError:
                        continue
        
        if not date_found:
            return {'error': 'No valid date found'}
        
        # Extract Site ID (EST format)
        site_match = self.site_pattern.search(block)
        if not site_match:
            return {'error': 'No valid SITE ID'}
        
        site_num = site_match.group(1) or site_match.group(2)
        site_id = f"IHS_EST_{site_num.upper()}"
        data["SITE ID"] = site_id
        
        # Extract site name
        name_patterns = [
            r"Site\s+(?:name|Name|I[\'d])\s*[:=]?\s*([A-Za-z\s]+?)(?:\n|Run|RT|Intial|Fuel|$)",
        ]
        for pattern in name_patterns:
            name_match = re.search(pattern, block, re.IGNORECASE)
            if name_match:
                data["SITE NAME"] = name_match.group(1).strip()
                break
        
        if "SITE NAME" not in data:
            data["SITE NAME"] = ""
        
        # Extract Runtime
        rt_patterns = [
            r"(?:Run\s+Time|Runtime|Rt)\s*[:=]?\s*(\d+|fault|faulty)",
            r"Run\s*[:=]?\s*(\d+|fault|faulty)"
        ]
        for pattern in rt_patterns:
            rt_match = re.search(pattern, block, re.IGNORECASE)
            if rt_match:
                rt_val = rt_match.group(1).strip()
                if rt_val.lower() in ['fault', 'faulty']:
                    data["CURRENT DG RUN HOURS"] = "FAULTY"
                else:
                    try:
                        data["CURRENT DG RUN HOURS"] = int(rt_val)
                    except ValueError:
                        data["CURRENT DG RUN HOURS"] = "FAULTY"
                break
        
        # Extract fuel data (Eastern uses "Intial dp" - note the typo)
        found_patterns = [
            r"(?:Intial|Initial)\s+(?:dp|fuel\s+level)\s*[:=]?\s*(\d+)",
            r"Intial\s+level\s*[:=]?\s*(\d+)"
        ]
        for pattern in found_patterns:
            found_match = re.search(pattern, block, re.IGNORECASE)
            if found_match:
                try:
                    data["FUEL FOUND"] = int(found_match.group(1))
                except ValueError:
                    pass
                break
        
        added_patterns = [
            r"(?:Added\s+fuel|Fuel\s+added)\s*[:=]?\s*(\d+)",
            r"Fuel\s+a(?:d|de)ded\s*[:=]?\s*(\d+)"  # Handle typos
        ]
        for pattern in added_patterns:
            added_match = re.search(pattern, block, re.IGNORECASE)
            if added_match:
                try:
                    data["FUEL ADDED"] = int(added_match.group(1))
                except ValueError:
                    pass
                break
        
        final_patterns = [
            r"Final\s+(?:dp|fuel\s+level)\s*[:=]?\s*(\d+)"
        ]
        for pattern in final_patterns:
            final_match = re.search(pattern, block, re.IGNORECASE)
            if final_match:
                try:
                    data["FUEL LEFT ON SITE"] = int(final_match.group(1))
                except ValueError:
                    pass
                break
        
        # Extract Supplier
        supplier_patterns = [
            r"(?:Fuel\s+)?[Ss]ource\s*[:=]?\s*(Meru|MERU|Puma|PUMA|CCS|meru|puma|ccs)",
            r"[Ss]ource\s*[:=]?\s*(Meru|MERU|Puma|PUMA|CCS)"
        ]
        for pattern in supplier_patterns:
            supplier_match = re.search(pattern, block, re.IGNORECASE)
            if supplier_match:
                data["SUPPLIER"] = supplier_match.group(1).upper()
                break
        
        data["NAME OF TECHNICIAN"] = "N/A"
        
        return data


# ============================================================================
# UNIFIED MULTI-REPORT CONTROLLER
# ============================================================================

class MultiReportController:
    """Controls parsing and updating for all report types"""
    
    def __init__(self):
        self.old_ccs_parser = OldCCSParser(OldCCSConfig())
        self.nrw_parser = NRWParser(NRWConfig())
        self.eastern_parser = EasternParser(EasternConfig())
    
    def parse_report(self, 
                     file_path: str, 
                     report_type: str,
                     error_logger: Optional[Callable] = None,
                     progress_callback: Optional[Callable] = None) -> tuple:
        """
        Parse a report file based on type
        
        Args:
            file_path: Path to WhatsApp chat file
            report_type: One of 'old_ccs', 'nrw', 'eastern'
            error_logger: Optional error logging callback
            progress_callback: Optional progress callback
        
        Returns:
            tuple: (entries, skipped_count, unmatched_blocks)
        """
        
        report_type = report_type.lower()
        
        if report_type == 'old_ccs':
            return self.old_ccs_parser.parse_file(file_path, error_logger, progress_callback)
        elif report_type == 'nrw':
            return self.nrw_parser.parse_file(file_path, error_logger, progress_callback)
        elif report_type == 'eastern':
            return self.eastern_parser.parse_file(file_path, error_logger, progress_callback)
        else:
            raise ValueError(f"Unknown report type: {report_type}")
    
    def get_excel_file(self, report_type: str) -> str:
        """Get Excel file path for report type"""
        report_type = report_type.lower()
        
        if report_type == 'old_ccs':
            return self.old_ccs_parser.config.excel_file
        elif report_type == 'nrw':
            return self.nrw_parser.config.excel_file
        elif report_type == 'eastern':
            return self.eastern_parser.config.excel_file
        else:
            raise ValueError(f"Unknown report type: {report_type}")

