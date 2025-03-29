import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import bluetooth
import logging
import sqlite3
import time
import os
import threading
import keyboard  # Make sure to install this module: pip install keyboard
import glob
import asyncio
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Pool

class BLEScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BLE Scanner")
        self.setup_ui()
        self.setup_logging()
        self.setup_db()
        self.scanning = False

    def setup_ui(self):
        # Setup UI elements: start/stop buttons and log output
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

    def setup_db(self):
        # SQLite Database setup (opened in the main thread)
        self.db_file = "bluetooth_devices.db"
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

        # Create the devices table if it doesn't exist
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            mac_address TEXT,
            device_name TEXT,
            vendor TEXT,
            extra_info TEXT
        )
        ''')
        self.conn.commit()

    def start_scanning(self):
        if not self.scanning:
            self.scanning = True
            # Start the scanning loop in a separate daemon thread
            self.scan_thread = threading.Thread(target=self.scanning_loop, daemon=True)
            self.scan_thread.start()
            messagebox.showinfo("Info", "Started Bluetooth scanning.")

    def stop_scanning(self):
        if self.scanning:
            self.scanning = False
            messagebox.showinfo("Info", "Stopped Bluetooth scanning.")

    def scanning_loop(self):
        # Scanning loop running asynchronously
        while self.scanning:
            asyncio.run(self.scan_devices())
            logging.debug("Sleeping for 5 minutes before next scan...")
            time.sleep(300)  # Sleep for 5 minutes

    class VendorLookup:
        def __init__(self):
            # Vendor mapping for MAC address prefixes
            self.vendor_mapping = {
                "F0:99:B6": "Apple, Inc.",
                "28:FF:3C": "Apple, Inc.",
                "D0:D0:03": "Samsung Electronics Co., Ltd.",
                "08:FD:0E": "Samsung Electronics Co., Ltd.",
                "CC:05:77": "Huawei Technologies Co., Ltd.",
                "30:FB:B8": "Huawei Technologies Co., Ltd.",
                "00:14:22": "Dell Inc.",
                "04:0E:3C": "HP Inc.",
                "00:68:EB": "HP Inc.",
                "10:C5:95": "Lenovo",
                "98:93:CC": "LG Electronics Inc.",
                "F0:BF:97": "Sony Corporation",
                "98:E8:FA": "Nintendo Co., Ltd.",
                "80:C5:E6": "Microsoft Corporation",
                "58:CB:52": "Google, Inc.",
                "68:DB:F5": "Amazon Technologies Inc.",
                "A4:45:19": "Xiaomi Communications Co., Ltd.",
                "A0:91:A2": "OnePlus Electronics (Shenzhen) Co., Ltd.",
                "18:02:AE": "Vivo Mobile Communication Co., Ltd.",
                "D8:1E:DD": "Guangdong Oppo Mobile Telecommunications Corp., Ltd.",
                "24:46:C8": "Motorola Mobility LLC (Lenovo)",
                "BC:C3:42": "Panasonic Communications Co., Ltd.",
                "1C:5A:6B": "Philips Electronics Nederland BV",
                "00:01:24": "Acer Incorporated",
                "04:92:26": "ASUSTek COMPUTER INC."
            }

        def get_vendor(self, mac):
            # Extract the OUI (first 3 octets) and return the corresponding vendor
            oui = mac.upper()[0:8]
            return self.vendor_mapping.get(oui, "Unknown Vendor")

    def get_extra_info(self, mac):
        # Use bluetoothctl to get extra information about a device
        try:
            result = subprocess.run(["bluetoothctl", "info", mac],
                                    capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                extra = result.stdout.strip()
                logging.debug(f"Extra info for {mac}: {extra}")
                return extra
            else:
                logging.debug(f"bluetoothctl returned non-zero exit for {mac}")
                return "No extra info available."
        except Exception as e:
            logging.error(f"Error retrieving extra info for {mac}: {e}")
            return "Error retrieving extra info."

    async def scan_device(self, addr, name):
        # Scan a single device and log its information asynchronously
        extra_info = await asyncio.to_thread(self.get_extra_info, addr)
        vendor = self.VendorLookup().get_vendor(addr)
        timestamp = datetime.now().isoformat()
        self.cursor.execute(
            "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info) VALUES (?, ?, ?, ?, ?)",
            (timestamp, addr, name, vendor, extra_info)
        )
        self.conn.commit()
        logging.debug(f"Logged device {addr} ({name}) with vendor {vendor}.")

    async def scan_devices(self):
        # Perform a Bluetooth scan and log data asynchronously
        logging.debug("Starting Bluetooth scan...")
        try:
            devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
            logging.debug(f"Found {len(devices)} device(s).")

            # Create a list of tasks for asyncio to run concurrently
            tasks = [self.scan_device(addr, name) for addr, name in devices]
            await asyncio.gather(*tasks)
        except Exception as e:
            logging.error(f"Error during Bluetooth scan: {e}")

    def on_closing(self):
        # Handle closing of the application
        if self.scanning:
            self.stop_scanning()
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BLEScannerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
