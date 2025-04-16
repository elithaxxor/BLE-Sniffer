
# 🕵️‍♂️ BLE-Sniffer+Scanner | Standalone 

Welcome to the **BLE-Sniffer+Scanner -- Standalone** repository! 🎉 This is your ultimate toolkit for tracking down Bluetooth Low Energy (BLE) devices like a tech-savvy detective. Think of it as your personal Bluetooth Sherlock Holmes.

---

## 🌟 Overview

This standalone framework allows you to scan and log BLE devices using individual tooling or by running the framework as a whole.

---

## 🛠️ Tools and Structure

Run the main framework or access individual scripts directly. Below is an overview of the repository's structure:

```bash
standalone/
└── scanners/
    ├── logs/                  # Where log files live
    ├── sniff_my_ble.py        # Python script for BLE scanning
    ├── scan_bluetooth.ps1     # PowerShell script for Windows scanning
    └── bluetooth_devices.db   # SQLite database for device info
```

The tools include:
- **`sniff_my_ble.py`**: A Python-based script for scanning BLE devices. Features threading, asynchronous functions, and detailed logging.
- **`scan_bluetooth.ps1`**: A PowerShell-based script for Windows users, providing colorful feedback, scan intervals, and robust error handling.
- **`bluetooth_devices.db`**: An SQLite database for storing BLE device information.
- **Logs**: All generated logs are stored in the `logs/` folder.

---

## 📝 Changelog

### v1.2.0 - 2025-04-16
- **`scan_bluetooth.ps1` Updates**:
  - Added dynamic log file configuration via parameters and environment variables.
  - Improved error handling with detailed exception messages.
  - Introduced logging levels (`INFO`, `ERROR`, `OK`) for better log clarity.
  - Ensured compatibility checks for required cmdlets (`Get-PnpDevice`).
  - Modularized functions for reusability and maintainability.
  - Added fallback handling for missing device properties.

- **Documentation Updates**:
  - Added detailed descriptions of `scan_bluetooth.ps1` and usage examples.
  - Updated logging structure and repository structure documentation.

### v1.1.0 - 2025-03-25
- Enhanced the `sniff_my_ble.py` script:
  - Added asynchronous functions for better performance.
  - Implemented threading and multiprocessing for concurrent execution.
  - Improved logging with detailed timestamps and log file management.
- Updated `scan_bluetooth.ps1` script:
  - Enhanced output with colorful feedback and emojis.
  - Added flexibility for scan intervals and continuous scanning.
- Improved vendor lookup with a more comprehensive list of MAC address prefixes.
- Added Flask application (`app.py`) for web interface to display device logs.
- Updated documentation to reflect new features and improvements.

### v1.0.0 - Initial Release
- Introduced `sniff_my_ble.py` for scanning BLE devices and logging the data.
- Included `scan_bluetooth.ps1` for Windows users to scan Bluetooth devices.
- Set up SQLite database for storing device logs.
- Implemented basic vendor identification based on MAC address prefixes.
- Provided initial documentation with usage instructions and repository structure.

---

Let me know if further refinements are needed!
```
v1.1.0 - 2025-03-25

    Enhanced the sniff_my_ble.py script:
        Added asynchronous functions for better performance.
        Implemented threading and multiprocessing for concurrent execution.
        Improved logging with detailed timestamps and log file management.
    Updated scan_bluetooth.ps1 script:
        Enhanced output with colorful feedback and emojis.
        Added flexibility for scan intervals and continuous scanning.
    Improved vendor lookup with a more comprehensive list of MAC address prefixes.
    Updated documentation to reflect new features and improvements.
    Added sections for:
        Flask application (app.py) for web interface to display device logs.
        Detailed repository structure.
        Example outputs for both Python and PowerShell scripts.
        Error handling for both scripts.
    Ensured SQLite database setup and logging configurations are robust and reliable.

v1.0.0 - Initial Release

    Introduced sniff_my_ble.py for scanning BLE devices and logging the data.
    Included scan_bluetooth.ps1 for Windows users to scan Bluetooth devices.
    Set up SQLite database for storing device logs.
    Implemented basic vendor identification based on MAC address prefixes.
    Provided initial documentation with usage instructions and repository structure.
