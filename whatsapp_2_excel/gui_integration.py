"""
GUI Integration Module for Multi-Report Support
Add this to your existing GUI without modifying the original code
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
from datetime import datetime
import logging
import os

# Import your existing modules
# from automation_controller import AutomationController
# from config import Config

# Import the new multi-report parsers
from multi_report_parsers import MultiReportController


class MultiReportGUI:
    """Extended GUI that supports multiple report types"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Multi-Report Automation - v3.0")
        self.root.geometry("1200x900")
        
        self.multi_controller = MultiReportController()
        self.selected_report_type = tk.StringVar(value="new_ccs")
        self.chat_file = None
        self.start_time = None
        
        self._setup_ui()
        self._setup_logging()
    
    def _setup_ui(self):
        """Setup the extended user interface"""
        
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Report Type Selection Frame
        report_frame = ttk.LabelFrame(main_frame, text="Select Report Type", padding=10)
        report_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        # Radio buttons for report types
        ttk.Radiobutton(
            report_frame, 
            text="🆕 New CCS Report (Original)", 
            variable=self.selected_report_type, 
            value="new_ccs"
        ).pack(side='left', padx=10)
        
        ttk.Radiobutton(
            report_frame, 
            text="📊 Old CCS Report", 
            variable=self.selected_report_type, 
            value="old_ccs"
        ).pack(side='left', padx=10)
        
        ttk.Radiobutton(
            report_frame, 
            text="🌍 NRW Report", 
            variable=self.selected_report_type, 
            value="nrw"
        ).pack(side='left', padx=10)
        
        ttk.Radiobutton(
            report_frame, 
            text="🌅 Eastern Report", 
            variable=self.selected_report_type, 
            value="eastern"
        ).pack(side='left', padx=10)
        
        # File Selection Frame
        file_frame = ttk.Frame(main_frame)
        file_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        
        self.file_label = ttk.Label(file_frame, text="No file selected", font=("Arial", 10))
        self.file_label.pack(side='left', padx=10)
        
        ttk.Button(
            file_frame, 
            text="📁 Select Chat File", 
            command=self.select_file
        ).pack(side='right', padx=10)
        
        # Log area
        log_frame = ttk.LabelFrame(main_frame, text="Processing Log", padding=10)
        log_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        log_frame.grid_rowconfigure(0, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        
        from tkinter import scrolledtext
        self.text_area = scrolledtext.ScrolledText(
            log_frame, 
            state='disabled', 
            font=("Consolas", 9),
            bg="#1e1e1e", 
            fg="#00ff00"
        )
        self.text_area.grid(row=0, column=0, sticky="nsew")
        
        # Error area
        error_frame = ttk.LabelFrame(main_frame, text="Errors & Warnings", padding=10)
        error_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        error_frame.grid_rowconfigure(0, weight=1)
        error_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(3, weight=0)
        
        self.error_area = scrolledtext.ScrolledText(
            error_frame, 
            state='disabled', 
            font=("Consolas", 9),
            height=8, 
            bg="#2d1f1f", 
            fg="#ff6b6b"
        )
        self.error_area.grid(row=0, column=0, sticky="nsew")
        
        # Status and progress
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
        
        self.status_var = tk.StringVar(value="Ready - Select report type and chat file")
        self.eta_var = tk.StringVar(value="")
        
        ttk.Label(
            status_frame, 
            textvariable=self.status_var, 
            font=("Arial", 11, "bold")
        ).pack(side='left', padx=10)
        
        ttk.Label(
            status_frame, 
            textvariable=self.eta_var, 
            font=("Arial", 10), 
            foreground="blue"
        ).pack(side='right', padx=10)
        
        self.progress = ttk.Progressbar(main_frame, length=1150, mode="determinate")
        self.progress.grid(row=5, column=0, pady=5, padx=10)
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=6, column=0, pady=15)
        
        self.start_btn = ttk.Button(
            btn_frame, 
            text="▶️ Start Processing", 
            command=self.start_processing_thread,
            state='disabled'
        )
        self.start_btn.pack(side='left', padx=10)
        
        self.clear_btn = ttk.Button(
            btn_frame, 
            text="🗑️ Clear Logs", 
            command=self.clear_logs
        )
        self.clear_btn.pack(side='left', padx=10)
        
        # Info labels
        info_frame = ttk.Frame(main_frame)
        info_frame.grid(row=7, column=0, pady=5)
        
        ttk.Label(
            info_frame, 
            text="✨ Multi-Report Support: New CCS, Old CCS, NRW, Eastern", 
            font=("Arial", 8), 
            foreground="blue"
        ).pack()
        
        ttk.Label(
            info_frame, 
            text="📝 Each report type has its own parser and Excel file", 
            font=("Arial", 8), 
            foreground="gray"
        ).pack()
    
    def _setup_logging(self):
        """Setup logging configuration"""
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # Custom handler for GUI
        class GUIHandler(logging.Handler):
            def __init__(self, text_widget):
                super().__init__()
                self.text_widget = text_widget
            
            def emit(self, record):
                msg = self.format(record)
                self.text_widget.configure(state='normal')
                self.text_widget.insert(tk.END, msg + "\n")
                self.text_widget.see(tk.END)
                self.text_widget.configure(state='disabled')
        
        handler = GUIHandler(self.text_area)
        handler.setFormatter(
            logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        )
        logger.addHandler(handler)
    
    def clear_logs(self):
        """Clear all log areas"""
        self.text_area.configure(state='normal')
        self.text_area.delete('1.0', tk.END)
        self.text_area.configure(state='disabled')
        self.error_area.configure(state='normal')
        self.error_area.delete('1.0', tk.END)
        self.error_area.configure(state='disabled')
        logging.info("🧹 Logs cleared")
    
    def log_error(self, msg: str):
        """Log error message to error area"""
        self.error_area.configure(state='normal')
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.error_area.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.error_area.see(tk.END)
        self.error_area.configure(state='disabled')
    
    def select_file(self):
        """Handle file selection"""
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            self.chat_file = path
            filename = os.path.basename(path)
            self.file_label.config(text=f"Selected: {filename}")
            logging.info(f"📂 File selected: {filename}")
            
            report_type = self.selected_report_type.get()
            report_name = {
                'new_ccs': 'New CCS',
                'old_ccs': 'Old CCS',
                'nrw': 'NRW',
                'eastern': 'Eastern'
            }[report_type]
            
            self.status_var.set(f"Ready: {report_name} Report - {filename}")
            self.start_btn.config(state='normal')
    
    def update_progress(self, value: int):
        """Update progress bar and ETA"""
        self.progress['value'] = value
        self.root.update_idletasks()
        
        if self.start_time and value > 0:
            elapsed = (datetime.now() - self.start_time).total_seconds()
            if value < 100:
                total_estimated = (elapsed / value) * 100
                remaining = total_estimated - elapsed
                minutes = int(remaining // 60)
                seconds = int(remaining % 60)
                self.eta_var.set(f"ETA: {minutes}m {seconds}s")
            else:
                self.eta_var.set("Complete!")
    
    def process_report(self):
        """Process the selected report"""
        if not self.chat_file:
            logging.warning("⚠️ No file selected!")
            self.status_var.set("Ready - Select report type and chat file")
            return
        
        report_type = self.selected_report_type.get()
        
        try:
            self.start_time = datetime.now()
            
            report_names = {
                'new_ccs': 'New CCS',
                'old_ccs': 'Old CCS',
                'nrw': 'NRW',
                'eastern': 'Eastern'
            }
            report_name = report_names[report_type]
            
            self.status_var.set(f"⏳ Processing {report_name} Report...")
            self.update_progress(10)
            
            if report_type == 'new_ccs':
                # Use your existing controller for new CCS
                logging.info("📋 Using original New CCS parser...")
                # Call your existing automation controller here
                # result = your_existing_controller.run(...)
                messagebox.showinfo(
                    "Info", 
                    "New CCS Report uses the original automation.\n"
                    "Please use the original interface for this report type."
                )
                return
            
            else:
                # Use new multi-report controller
                logging.info(f"📋 Processing {report_name} Report...")
                entries, skipped, unmatched = self.multi_controller.parse_report(
                    self.chat_file,
                    report_type,
                    error_logger=self.log_error,
                    progress_callback=self.update_progress
                )
                
                self.status_var.set(f"✅ {report_name} Processing Complete!")
                self.update_progress(100)
                
                # Get Excel file for this report type
                excel_file = self.multi_controller.get_excel_file(report_type)
                
                # Show summary
                elapsed = (datetime.now() - self.start_time).total_seconds()
                summary = (
                    f"✅ {report_name} Report Processing Complete!\n\n"
                    f"📊 Parsing Results:\n"
                    f"  • Valid entries parsed: {len(entries)}\n"
                    f"  • Skipped entries: {skipped}\n"
                    f"  • Unmatched blocks: {len(unmatched)}\n\n"
                    f"📁 Target Excel File:\n"
                    f"  • {os.path.basename(excel_file)}\n\n"
                    f"⏱️ Time taken: {int(elapsed)}s\n\n"
                    f"💡 Note: Entries have been parsed.\n"
                    f"   Use the Excel updater to write to file."
                )
                
                messagebox.showinfo("Success", summary)
                
                # Log sample entries
                if entries:
                    logging.info(f"\n📝 Sample parsed entry:")
                    sample = entries[0]
                    for key, value in sample.items():
                        logging.info(f"   {key}: {value}")
        
        except FileNotFoundError as e:
            logging.error(f"❌ File not found: {str(e)}")
            self.status_var.set("Error: File not found")
            messagebox.showerror("File Error", f"File not found:\n{str(e)}")
        
        except Exception as e:
            logging.error(f"❌ Unexpected error: {str(e)}")
            self.status_var.set("Error occurred!")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        
        finally:
            self.update_progress(0)
            self.eta_var.set("")
            self.start_btn.config(state='normal')
    
    def start_processing_thread(self):
        """Start processing in separate thread"""
        self.clear_logs()
        self.status_var.set("⏳ Starting...")
        self.eta_var.set("Calculating...")
        self.start_btn.config(state='disabled')
        
        threading.Thread(target=self.process_report, daemon=True).start()


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point for multi-report GUI"""
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    
    app = MultiReportGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()