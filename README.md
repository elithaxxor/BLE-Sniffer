
```markdown
# BLE-Sniffer

Welcome to the BLE-Sniffer repository! This repository contains scripts for scanning and logging Bluetooth Low Energy (BLE) devices. The scripts are designed to detect, identify, and log information about nearby BLE devices.

## Overview

### Purpose

The primary purpose of this repository is to provide tools for scanning and logging BLE devices. These tools can be used for various applications, such as network security monitoring, device tracking, and research.

### Features

- **Bluetooth Device Scanning**: Detects and logs nearby Bluetooth devices.
- **Vendor Identification**: Identifies the manufacturer of each device based on MAC address prefixes.
- **Additional Information Retrieval**: Uses commands like `bluetoothctl` to gather extra details about devices.
- **Database Logging**: Stores detailed information about each discovered device in an SQLite database.
- **Log File Management**: Manages log files, keeping only the most recent logs and deleting older ones automatically.
- **Concurrency**: Utilizes threading to perform scans and fetch extra device information concurrently.
- **Graceful Shutdown**: Can be terminated gracefully using a hotkey.

## Repository Structure

```
standalone/
└── scanners/
    ├── logs/                  # Directory for log files
    ├── sniff_my_ble.py        # Python script for scanning BLE devices
    ├── scan_bluetooth.ps1     # PowerShell script for Windows Bluetooth scanning
    └── bluetooth_devices.db   # SQLite database file
```

## Scripts

### Python Script: `sniff_my_ble.py`

This script scans for nearby Bluetooth devices, retrieves additional information, and logs the data into an SQLite database.

#### Key Features:

- **Bluetooth Scanning**: Uses the `bluetooth` module to scan for devices.
- **Vendor Identification**: Identifies the manufacturer based on MAC address prefixes.
- **Additional Info**: Retrieves extra information using the `bluetoothctl` command.
- **Database Logging**: Logs detailed information in a SQLite database.
- **Log Management**: Creates a folder for logs and keeps only the 3 most recent log files.
- **Concurrency**: Uses threading for concurrent data fetching.
- **Graceful Shutdown**: Can be terminated using a hotkey (`cmd+c` on macOS).

### PowerShell Script: `scan_bluetooth.ps1`

This script is designed for Windows and scans for Bluetooth devices, logs the results, and handles errors. It provides user-friendly output with different message levels and colors.

#### Key Features:

- **Bluetooth Scanning**: Uses the `Get-PnpDevice` cmdlet for scanning.
- **Logging**: Logs results and errors with timestamps.
- **User Feedback**: Provides colored messages for info, success, and error.
- **Menu for Scan Intervals**: Allows users to select scan intervals or continuous scanning.

## Usage

### Prerequisites

- **Python Script**:
  - Python 3.x
  - Bluetooth functionality enabled
  - Required Python modules:
    ```bash
    pip install pybluez keyboard
    ```

- **PowerShell Script**:
  - Windows operating system with PowerShell installed
  - Bluetooth functionality enabled

### Running the Python Script

1. Open a terminal with appropriate privileges.
2. Navigate to the directory containing the `sniff_my_ble.py` script.
3. Execute the script by running:
   ```bash
   python sniff_my_ble.py
   ```

### Running the PowerShell Script

1. Open PowerShell with administrative privileges.
2. Navigate to the directory containing the `scan_bluetooth.ps1` script.
3. Execute the script by running:
   ```powershell
   .\scan_bluetooth.ps1
   ```

## Log File Management

The scripts generate log files in the `logs` directory. Each log file is named with a timestamp to ensure uniqueness. The scripts keep only the 3 most recent log files and delete older ones automatically.

## Example Output

### Python Script

```plaintext
2025-03-24 17:45:10 - DEBUG - Starting Bluetooth scan...
2025-03-24 17:45:18 - DEBUG - Found 2 device(s).
2025-03-24 17:45:19 - DEBUG - Extra info for XX:XX:XX:XX:XX:XX: Device XX:XX:XX:XX:XX:XX
2025-03-24 17:45:19 - DEBUG - Logged device XX:XX:XX:XX:XX:XX (Device Name) with vendor Apple, Inc.
2025-03-24 17:45:19 - DEBUG - Extra info for YY:YY:YY:YY:YY:YY: Device YY:YY:YY:YY:YY:YY
2025-03-24 17:45:19 - DEBUG - Logged device YY:YY:YY:YY:YY:YY (Another Device) with vendor Samsung Electronics Co., Ltd.
2025-03-24 17:45:19 - DEBUG - Sleeping for 5 minutes before next scan...
```

### PowerShell Script

```plaintext
[!] Starting Bluetooth scan...
[!] Scanning Bluetooth devices using Get-PnpDevice...
[+] Found: Bluetooth Device (ID: 12345) - Manufacturer: Example Inc. - Type: Computer - RSSI: RSSI information not available in PowerShell
[+] Scan complete. Log saved to bluetooth_scan.log
```

## Error Handling

Both scripts include error handling to catch and log any issues encountered during the Bluetooth scan process and while retrieving extra device information.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests. Contributions are welcome!

---

This repository aims to provide robust tools for scanning and logging Bluetooth device data efficiently and maintainably.
```

This `README.md` provides a comprehensive overview of the `BLE-Sniffer` repository, including details about its purpose, features, usage, and example outputs.
