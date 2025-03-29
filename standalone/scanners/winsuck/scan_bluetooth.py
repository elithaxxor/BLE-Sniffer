import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import logging
import os
import glob
from datetime import datetime


class BluetoothScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bluetooth Scanner")
        self.setup_ui()
        self.setup_logging()

    def setup_ui(self):
        # Setup UI elements: start/stop buttons, entry for duration, and log output
        tk.Label(self.root, text="Scanning Duration (seconds):").pack(pady=5)
        self.duration_entry = tk.Entry(self.root)
        self.duration_entry.pack(pady=5)
        self.start_button = tk.Button(self.root, text="Start Scanning", command=self.start_scanning)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.root, text="Stop Scanning", command=self.stop_scanning)
        self.stop_button.pack(pady=10)
        self.log_output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.log_output.pack(pady=10)

    def setup_logging(self):
        # Log directory setup
        LOG_DIR = "logs"
        os.makedirs(LOG_DIR, exist_ok=True)

        # Get the current timestamp for the log file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        log_file = os.path.join(LOG_DIR, f"bluetooth_scan_{timestamp}.log")

        # Configure logging to file and GUI
        logging.basicConfig(level=logging.DEBUG,
                            format="%(asctime)s - %(levelname)s - %(message)s",
                            handlers=[
                                logging.FileHandler(log_file),
                                logging.StreamHandler(self)  # Stream logs to the GUI
                            ])

        # Manage log files (keep only the 3 most recent)
        log_files = sorted(glob.glob(os.path.join(LOG_DIR, "bluetooth_scan_*.log")))
        if len(log_files) > 3:
            for old_log in log_files[:-3]:
                os.remove(old_log)

    def write(self, message):
        # Write log messages to the GUI
        self.log_output.insert(tk.END, message)
        self.log_output.yview(tk.END)

    def flush(self):
        pass

    def start_scanning(self):
        try:
            duration = int(self.duration_entry.get())
            self.scan_thread = threading.Thread(target=self.scan_bluetooth, args=(duration,), daemon=True)
            self.scan_thread.start()
            messagebox.showinfo("Info", "Started Bluetooth scanning.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid duration.")

    def stop_scanning(self):
        if hasattr(self, 'scan_thread') and self.scan_thread.is_alive():
            self.scanning = False
            messagebox.showinfo("Info", "Stopped Bluetooth scanning.")
        else:
            messagebox.showwarning("Warning", "No active scanning to stop.")

    def scan_bluetooth(self, duration):
        self.scanning = True
        command = f"powershell.exe -Command Get-PnpDevice -Class Bluetooth -Status OK | Select-Object -Property FriendlyName, Manufacturer, Status"
        self.log_output.insert(tk.END, f"Scanning for {duration} seconds...\n")

        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(timeout=duration)
            self.log_output.insert(tk.END, stdout.decode())
            if stderr:
                self.log_output.insert(tk.END, stderr.decode())
        except subprocess.TimeoutExpired:
            process.kill()
            self.log_output.insert(tk.END, "Scanning timed out.\n")
        except Exception as e:
            self.log_output.insert(tk.END, f"Error during scanning: {e}\n")
        finally:
            self.scanning = False

    def on_closing(self):
        if self.scanning:
            self.stop_scanning()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = BluetoothScannerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
