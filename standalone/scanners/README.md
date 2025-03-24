
```markdown
# Bluetooth Sniffer Script

This repository contains a Python script `sniff_my_ble.py` designed to scan for active Bluetooth devices, retrieve additional information, and log the data into an SQLite database. The script runs continuously and supports graceful termination via a hotkey.

## Overview

### Features

- **Bluetooth Device Scanning**: Scans for nearby Bluetooth devices using the `bluetooth` module.
- **Vendor Identification**: Identifies the manufacturer of each device based on a predefined mapping of MAC address prefixes (OUIs).
- **Additional Device Information**: Retrieves extra information about each device using the `bluetoothctl` command.
- **Database Logging**: Logs detailed information about each discovered device into an SQLite database.
- **Log File Management**: Creates a folder for storing log files and keeps only the 3 most recent log files.
- **Concurrency**: Uses threading to perform scans and fetch extra device information concurrently.
- **Graceful Shutdown**: Can be gracefully terminated using a hotkey (`cmd+c` on macOS).

## Script Details

### Directory Structure

```markdown
standalone/
└── scanners/
    ├── logs/                  # Directory for log files
    ├── sniff_my_ble.py        # Bluetooth sniffer script
    └── bluetooth_devices.db   # SQLite database file
```

### SQLite Database Setup

The script sets up an SQLite database (`bluetooth_devices.db`) in the same directory as the script. It creates a table `devices` if it does not exist to store the scanned device information.

### Logging Setup

The script creates a directory named `logs` to store log files. Each log file is named with a timestamp to ensure uniqueness. The script keeps only the 3 most recent log files and deletes older ones automatically.

### Vendor Lookup Class

The `VendorLookup` class encapsulates logic for mapping MAC address prefixes to vendor names and provides a method to lookup the vendor based on the MAC address.

### Functions

#### `setup_logging`

Sets up the logging configuration and manages log files.

```python
def setup_logging():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_file = os.path.join(LOG_DIR, f"bluetooth_scan_{timestamp}.log")

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])

    log_files = sorted(glob.glob(os.path.join(LOG_DIR, "bluetooth_scan_*.log")))
    if len(log_files) > 3:
        for old_log in log_files[:-3]:
            os.remove(old_log)
```

#### `get_extra_info`

Attempts to gather extra information about a device using the `bluetoothctl` command.

```python
def get_extra_info(mac):
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
```

#### `scan_devices`

Performs a Bluetooth scan, concurrently retrieves extra device information, and logs the data into an SQLite database.

```python
def scan_devices():
    logging.debug("Starting Bluetooth scan...")
    try:
        devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
        logging.debug(f"Found {len(devices)} device(s).")

        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_device = {
                executor.submit(get_extra_info, addr): (addr, name)
                for addr, name in devices
            }
            for future in as_completed(future_to_device):
                addr, name = future_to_device[future]
                extra_info = future.result()
                vendor = vendor_lookup.get_vendor(addr)
                timestamp = datetime.now().isoformat()
                cursor.execute(
                    "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info) VALUES (?, ?, ?, ?, ?)",
                    (timestamp, addr, name, vendor, extra_info)
                )
                conn.commit()
                logging.debug(f"Logged device {addr} ({name}) with vendor {vendor}.")
    except Exception as e:
        logging.error(f"Error during Bluetooth scan: {e}")
```

#### `scanning_loop`

Runs the scanning process indefinitely at 5-minute intervals.

```python
def scanning_loop():
    while True:
        scan_devices()
        logging.debug("Sleeping for 5 minutes before next scan...")
        time.sleep(300)  # Sleep for 5 minutes
```

#### `quit_program`

Function called when the hotkey is pressed to gracefully terminate the program.

```python
def quit_program():
    logging.info("Quit hotkey pressed. Exiting program.")
    raise KeyboardInterrupt
```

### Main Execution Block

Sets up the hotkey for quitting the program, starts the scanning loop in a separate daemon thread, and keeps the main thread running to prevent termination of the daemon thread.

```python
if __name__ == "__main__":
    try:
        keyboard.add_hotkey('cmd+c', quit_program)

        scan_thread = threading.Thread(target=scanning_loop, daemon=True)
        scan_thread.start()

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Program terminated by user.")
    finally:
        conn.close()
```

## Usage

### Prerequisites

- Python 3.x
- Bluetooth functionality enabled on the machine
- Required Python modules:
  ```bash
  pip install pybluez keyboard
  ```

### Running the Script

1. Open a terminal with appropriate privileges.
2. Navigate to the directory containing the `sniff_my_ble.py` script.
3. Execute the script by running the following command:
   ```bash
   python sniff_my_ble.py
   ```

### Log File

The script generates log files in the `logs` directory. Each log file is named with a timestamp to ensure uniqueness. The script keeps only the 3 most recent log files and deletes older ones automatically. The log files contain timestamps and details of the Bluetooth scan results.

### Example Output

```plaintext
2025-03-24 17:45:10 - DEBUG - Starting Bluetooth scan...
2025-03-24 17:45:18 - DEBUG - Found 2 device(s).
2025-03-24 17:45:19 - DEBUG - Extra info for XX:XX:XX:XX:XX:XX: Device XX:XX:XX:XX:XX:XX
2025-03-24 17:45:19 - DEBUG - Logged device XX:XX:XX:XX:XX:XX (Device Name) with vendor Apple, Inc.
2025-03-24 17:45:19 - DEBUG - Extra info for YY:YY:YY:YY:YY:YY: Device YY:YY:YY:YY:YY:YY
2025-03-24 17:45:19 - DEBUG - Logged device YY:YY:YY:YY:YY:YY (Another Device) with vendor Samsung Electronics Co., Ltd.
2025-03-24 17:45:19 - DEBUG - Sleeping for 5 minutes before next scan...
```

## Error Handling

The script includes error handling to catch and log any issues encountered during the Bluetooth scan process and while retrieving extra device information.

---

This repository aims to provide a robust script for scanning and logging Bluetooth device data efficiently and maintainably.
```

