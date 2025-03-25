import subprocess, bluetooth, logging, sqlite3, time, os, sys
import threading
import keyboard  # TODO: Make sure to install this module: pip install keyboard
import glob
import asyncio
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Pool

# Log directory setup
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    # Get the current timestamp for the log file name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_file = os.path.join(LOG_DIR, f"bluetooth_scan_{timestamp}.log")

    # Configure logging
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])

    # Manage log files (keep only the 3 most recent)
    log_files = sorted(glob.glob(os.path.join(LOG_DIR, "bluetooth_scan_*.log")))
    if len(log_files) > 3:
        for old_log in log_files[:-3]:
            os.remove(old_log)

# Initialize logging
setup_logging()

# SQLite Database setup (opened in the main thread)
db_file = "bluetooth_devices.db"
conn = sqlite3.connect(db_file, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    mac_address TEXT,
    device_name TEXT,
    vendor TEXT,
    extra_info TEXT
)
''')
conn.commit()

class VendorLookup:
    """
    Encapsulates the vendor mapping and lookup logic.
    """
    def __init__(self):
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
        """
        Extracts the OUI (first 3 octets) from the MAC address and returns the corresponding vendor.
        """
        oui = mac.upper()[0:8]
        return self.vendor_mapping.get(oui, "Unknown Vendor")

# Instantiate the vendor lookup object
vendor_lookup = VendorLookup()

def get_extra_info(mac):
    """
    Attempts to gather extra information about a device using the bluetoothctl command.
    """
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

async def scan_device(addr, name):
    """
    Async function to scan a single device and log its information.
    """
    extra_info = await asyncio.to_thread(get_extra_info, addr)
    vendor = vendor_lookup.get_vendor(addr)
    timestamp = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info) VALUES (?, ?, ?, ?, ?)",
        (timestamp, addr, name, vendor, extra_info)
    )
    conn.commit()
    logging.debug(f"Logged device {addr} ({name}) with vendor {vendor}.")

async def scan_devices():
    """
    Performs a Bluetooth scan, concurrently retrieves extra device information,
    and logs the data into a SQLite database.
    """
    logging.debug("Starting Bluetooth scan...")
    try:
        # Discover devices for about 8 seconds (device tuple: (mac_address, device_name))
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
        logging.debug(f"Found {len(devices)} device(s).")

        # Create a list of tasks for asyncio to run concurrently
        tasks = [scan_device(addr, name) for addr, name in devices]
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.error(f"Error during Bluetooth scan: {e}")

def scanning_loop():
    """
    Runs the scanning process indefinitely at 5-minute intervals.
    """
    while True:
        asyncio.run(scan_devices())
        logging.debug("Sleeping for 5 minutes before next scan...")
        time.sleep(300)  # Sleep for 5 minutes

def quit_program():
    """
    Function called when the hotkey is pressed.
    """
    logging.info("Quit hotkey pressed. Exiting program.")
    raise KeyboardInterrupt

if __name__ == "__main__":
    try:
        # Set up the hotkey for quitting the program: cmd+c (on macOS)
        keyboard.add_hotkey('cmd+c', quit_program)

        # Start the scanning loop in a separate daemon thread.
        scan_thread = threading.Thread(target=scanning_loop, daemon=True)
        scan_thread.start()

        # Keep the main thread running so that the daemon thread is not terminated.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    finally:
        conn.close()
## TODO: Make into a function, wrapper to log various tables 
# Log directory setup
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    # Get the current timestamp for the log file name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_file = os.path.join(LOG_DIR, f"bluetooth_scan_{timestamp}.log")

    # Configure logging
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])

    # Manage log files (keep only the 3 most recent)
    log_files = sorted(glob.glob(os.path.join(LOG_DIR, "bluetooth_scan_*.log")))
    if len(log_files) > 3:
        for old_log in log_files[:-3]:
            os.remove(old_log)

# Initialize logging
setup_logging()

# SQLite Database setup (opened in the main thread)
db_file = "bluetooth_devices.db"
conn = sqlite3.connect(db_file, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    mac_address TEXT,
    device_name TEXT,
    vendor TEXT,
    extra_info TEXT
)
''')
conn.commit()

class VendorLookup:
    """
    Encapsulates the vendor mapping and lookup logic.
    """
    def __init__(self):
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
        """
        Extracts the OUI (first 3 octets) from the MAC address and returns the corresponding vendor.
        """
        oui = mac.upper()[0:8]
        return self.vendor_mapping.get(oui, "Unknown Vendor")

# Instantiate the vendor lookup object
vendor_lookup = VendorLookup()

def get_extra_info(mac):
    """
    Attempts to gather extra information about a device using the bluetoothctl command.
    """
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

async def scan_device(addr, name):
    """
    Async function to scan a single device and log its information.
    """
    extra_info = await asyncio.to_thread(get_extra_info, addr)
    vendor = vendor_lookup.get_vendor(addr)
    timestamp = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info) VALUES (?, ?, ?, ?, ?)",
        (timestamp, addr, name, vendor, extra_info)
    )
    conn.commit()
    logging.debug(f"Logged device {addr} ({name}) with vendor {vendor}.")

async def scan_devices():
    """
    Performs a Bluetooth scan, concurrently retrieves extra device information,
    and logs the data into a SQLite database.
    """
    logging.debug("Starting Bluetooth scan...")
    try:
        # Discover devices for about 8 seconds (device tuple: (mac_address, device_name))
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
        logging.debug(f"Found {len(devices)} device(s).")

        # Create a list of tasks for asyncio to run concurrently
        tasks = [scan_device(addr, name) for addr, name in devices]
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.error(f"Error during Bluetooth scan: {e}")

def scanning_loop():
    """
    Runs the scanning process indefinitely at 5-minute intervals.
    """
    while True:
        asyncio.run(scan_devices())
        logging.debug("Sleeping for 5 minutes before next scan...")
        time.sleep(300)  # Sleep for 5 minutes

def quit_program():
    """
    Function called when the hotkey is pressed.
    """
    logging.info("Quit hotkey pressed. Exiting program.")
    raise KeyboardInterrupt

if __name__ == "__main__":
    try:
        # Set up the hotkey for quitting the program: cmd+c (on macOS)
        keyboard.add_hotkey('cmd+c', quit_program)

        # Start the scanning loop in a separate daemon thread.
        scan_thread = threading.Thread(target=scanning_loop, daemon=True)
        scan_thread.start()

        # Keep the main thread running so that the daemon thread is not terminated.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    finally:
        conn.close()
