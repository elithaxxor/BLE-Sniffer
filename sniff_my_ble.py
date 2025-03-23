import bluetooth
import time
import sqlite3
import logging
from datetime import datetime

# Set up verbose logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Database setup: Create/connect to a SQLite database and a table for device logs.
db_file = "bluetooth_devices.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    mac_address TEXT,
    device_name TEXT,
    vendor TEXT
)
''')
conn.commit()

def lookup_vendor(mac):
    """
    Extract the OUI (first 3 octets) from the MAC address and return a vendor name.
    You can expand this mapping or integrate with an external API for more detailed info.
    """
    # Normalize MAC address (e.g., "00:1A:7D:xx:xx:xx")
    oui = mac.upper()[0:8]
    # Example vendor mapping (expand as needed)
    vendor_mapping = {
        "00:1A:7D": "Apple, Inc.",
        "00:1B:63": "Samsung Electronics",
        # Add additional mappings here
    }
    return vendor_mapping.get(oui, "Unknown Vendor")

def scan_devices():
    """
    Perform a Bluetooth scan, log found devices, and save details to the database.
    """
    logging.debug("Starting Bluetooth scan...")
    try:
        # Discover devices for about 8 seconds. lookup_names=True returns the device name.
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
        logging.debug(f"Found {len(devices)} device(s).")
        for addr, name in devices:
            logging.debug(f"Device found: MAC={addr} | Name={name}")
            vendor = lookup_vendor(addr)
            logging.debug(f"Vendor lookup result: {vendor}")
            timestamp = datetime.now().isoformat()
            cursor.execute(
                "INSERT INTO devices (timestamp, mac_address, device_name, vendor) VALUES (?, ?, ?, ?)",
                (timestamp, addr, name, vendor)
            )
            conn.commit()
    except Exception as e:
        logging.error(f"Error during Bluetooth scan: {e}")

if __name__ == "__main__":
    try:
        while True:
            scan_devices()
            logging.debug("Sleeping for 5 minutes...")
            time.sleep(300)  # Wait 5 minutes (300 seconds) before the next scan.
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    finally:
        conn.close()
