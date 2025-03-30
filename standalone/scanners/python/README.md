# Bluetooth Scanning Scripts

<img width="372" alt="Screenshot 2025-03-29 at 8 40 43 PM" src="https://github.com/user-attachments/assets/148a5b7d-2d00-4730-b54d-0e9853013c51"/>

```markdown 
## 1. `sniff_my_ble.py`

This script is designed to perform Bluetooth scanning and log the detected devices into a SQLite database. It includes the following key functionalities:

- **Logging Setup**: Configures logging to both a log file and the console, retaining only the three most recent log files.
- **SQLite Database Setup**: Initializes an SQLite database to store device information, including MAC addresses, device names, vendors, and extra information.
- **Vendor Lookup**: Contains a `VendorLookup` class that maps MAC address prefixes (OUIs) to vendor names.
- **Extra Information Retrieval**: Defines a function `get_extra_info` to attempt to gather additional information about a device using the `bluetoothctl` command.
- **Asynchronous Device Scanning**: Uses asynchronous functions `scan_device` and `scan_devices` to perform Bluetooth scans, retrieve extra device information, and log the data into the database.
- **Scanning Loop**: Runs the scanning process indefinitely at 5-minute intervals.
- **Hotkey for Quitting**: Sets up a hotkey (cmd+c on macOS) to quit the program gracefully.

## 2. `sniff_my_ble_cpuBound.py`

This script is very similar to `sniff_my_ble.py` with some differences:

- **Similar Logging and Database Setup**: Configures logging and initializes an SQLite database similarly to `sniff_my_ble.py`.
- **Vendor Lookup and Extra Information Retrieval**: Contains similar functionalities for vendor lookup and extra information retrieval.
- **Asynchronous Device Scanning**: Performs Bluetooth scans asynchronously and logs device information.
- **CPU-Bound Processing**: Utilizes `concurrent.futures.ThreadPoolExecutor` for potentially CPU-bound tasks, indicating a focus on optimizing thread-based concurrent execution.

## 3. `sniff_my_bles_cpu.py`

This script also performs Bluetooth scanning and logging but has a few notable differences:

- **Multiprocessing for Concurrency**: Instead of using threading and asyncio for concurrency, this script uses multiprocessing with the `Pool` class to utilize multiple CPU cores.
- **Direct Logging**: Implements a function `log_device_info` to directly log device information using a multiprocessing pool.
- **Simplified Structure**: The structure is simplified, directly using multiprocessing to handle device information logging, which can be more efficient for CPU-bound tasks.
- **Same Logging and Database Setup**: Similar logging and SQLite database setup as the other scripts.
- **Vendor Lookup and Extra Information Retrieval**: Contains similar functionalities for vendor lookup and extra information retrieval.

## Summary

All three scripts perform Bluetooth scanning and log device information into an SQLite database. They share common functionalities such as logging setup, database initialization, vendor lookup, and extra information retrieval. However, their concurrency and processing approaches differ:

- **`sniff_my_ble.py`**: Uses asyncio for asynchronous operations.
- **`sniff_my_ble_cpuBound.py`**: Uses `ThreadPoolExecutor` for thread-based concurrency.
- **`sniff_my_bles_cpu.py`**: Uses multiprocessing with the `Pool` class for CPU-bound tasks, leveraging multiple CPU cores.

These differences highlight the various approaches to handling asynchronous or CPU-bound tasks in Python.
```
