# 🕵️‍♂️ BLE-Sniffer

Welcome to the **BLE-Sniffer** repository! 🎉 This is your ultimate toolkit for tracking down Bluetooth Low Energy (BLE) devices like a tech-savvy detective. Think of it as your personal Bluetooth spy—minus the trench coat! 🕶️

---

run main to use the framework or direct access to the individual tooling is available:

Here’s what’s inside this treasure chest:

```bash
standalone/
└── scanners/
    ├── logs/                  # Where log files live
    ├── sniff_my_ble.py        # Python script for BLE scanning
    ├── scan_bluetooth.ps1     # PowerShell script for Windows scanning
    └── bluetooth_devices.db   # SQLite database for device info




3 references
Changelog
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
