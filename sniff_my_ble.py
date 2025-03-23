import bluetooth
import time
import sqlite3
import logging
import subprocess
from datetime import datetime

# Configure verbose logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# SQLite Database setup
db_file = "bluetooth_devices.db"
conn = sqlite3.connect(db_file)
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

# Define a sample vendor mapping for the first three octets (OUI)
vendor_mapping = {
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

def lookup_vendor(mac):
    """
    Extract the OUI (first 3 octets) from the MAC address and return the vendor name.
    """
    oui = mac.upper()[0:8]
    vendor = vendor_mapping.get(oui, "Unknown Vendor")
    return vendor

def get_extra_info(mac):
    """
    Attempt to gather extra information about a device by using bluetoothctl.
    This function calls: bluetoothctl info <MAC>
    """
    try:
        # Run bluetoothctl info command for the given MAC address.
        result = subprocess.run(["bluetoothctl", "info", mac],
                                capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            # Return the output (you could parse this further if desired)
            extra = result.stdout.strip()
            logging.debug(f"Extra info for {mac}: {extra}")
            return extra
        else:
            logging.debug(f"bluetoothctl returned non-zero exit for {mac}")
            return "No extra info available."
    except Exception as e:
        logging.error(f"Error retrieving extra info for {mac}: {e}")
        return "Error retrieving extra info."

def scan_devices():
    """
    Perform a Bluetooth scan, retrieve extra device information, and save details to the database.
    """
    logging.debug("Starting Bluetooth scan...")
    try:
        # Discover devices for about 8 seconds
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
        logging.debug(f"Found {len(devices)} device(s).")
        for addr, name in devices:
            logging.debug(f"Device found: MAC={addr} | Name={name}")
            vendor = lookup_vendor(addr)
            extra_info = get_extra_info(addr)
            timestamp = datetime.now().isoformat()
            cursor.execute(
                "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info) VALUES (?, ?, ?, ?, ?)",
                (timestamp, addr, name, vendor, extra_info)
            )
            conn.commit()
    except Exception as e:
        logging.error(f"Error during Bluetooth scan: {e}")

if __name__ == "__main__":
    try:
        while True:
            scan_devices()
            logging.debug("Sleeping for 5 minutes before next scan...")
            time.sleep(300)  # Pause for 5 minutes
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    finally:
        conn.close()
