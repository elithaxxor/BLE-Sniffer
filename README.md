# 🕵️‍♂️ BLE-Sniffer + Scanner

Welcome to the **BLE-Sniffer** repository! 🎉 This is your one-stop toolkit for scanning and logging Bluetooth Low Energy (BLE) devices. Whether you’re a network security enthusiast, a device tracker, or a researcher, this project will light up your Bluetooth world! 🔥

Development Status: The project is currently in the alpha stage, indicating that it is still under active development and may contain bugs or incomplete features.

#### TODO: Experiment w, NLTK Training on master_mac_list.csv 
---

## 🌟 Overview
    =-- standalone or webinterface. 

    [Standalone] --> Install dependencies, read README.md and then python3.
    [web-interface]--> Cd into standalone, choose what you want and corresponding read README.md and then python3.
### 🎯 Purpose

The **BLE-Sniffer** exists to make scanning and logging BLE devices a breeze! From **network monitoring** to **device tracking** and **research**, this repository has something for everyone.

    ** Packet Sniffing: Ability to capture and analyze BLE packets.
    ** Multi-Device Support: Can monitor multiple BLE devices simultaneously.
    ** Real-Time Monitoring: Offers live tracking and logging of BLE communications.
    
---

### 🚀 Features

- **🔍 Bluetooth Scanning**: Detects and logs nearby BLE devices.
- **🏷️ Vendor Identification**: Matches MAC addresses to manufacturers (like a Bluetooth Sherlock Holmes 🕵️‍♂️).
- **📄 Detailed Logging**: Stores insights in an SQLite database for easy access.
- **📂 Log Management**: Automatically deletes older logs to keep things tidy.
- **⚡ Concurrency**: Uses threading to make the scan process faster and more efficient.
- **🛑 Graceful Shutdown**: Stops cleanly with a hotkey—no crashing allowed!

---

---

### 🌐 Flask Application: `app.py`

The `app.py` script creates a web interface to display Bluetooth device logs stored in the SQLite database.

#### 🔑 Key Features:
- **Web Framework**: Powered by Flask for a sleek and simple web app.
- **Database Interaction**: Fetches device logs from the SQLite database.
- **HTML Templates**: Displays logs in a user-friendly table format.

#### 🏃 How to Run:
1. Install Flask:
   ```bash
   pip install flask


---

## 🗂️ Repository Structure

Here's what you’ll find in this repository:


# 🕵️‍♂️ BLE-Sniffer

Welcome to the **BLE-Sniffer** repository! 🎉 This is your one-stop toolkit for scanning and logging Bluetooth Low Energy (BLE) devices. Whether you’re a network security enthusiast, a device tracker, or a researcher, this project will light up your Bluetooth world! 🔥

---

## 🌟 Overview

### 🎯 Purpose

The **BLE-Sniffer** exists to make scanning and logging BLE devices a breeze! From **network monitoring** to **device tracking** and **research**, this repository has something for everyone.

---

### 🚀 Features

- **🔍 Bluetooth Scanning**: Detects and logs nearby BLE devices.
- **🏷️ Vendor Identification**: Matches MAC addresses to manufacturers (like a Bluetooth Sherlock Holmes 🕵️‍♂️).
- **📄 Detailed Logging**: Stores insights in an SQLite database for easy access.
- **📂 Log Management**: Automatically deletes older logs to keep things tidy.
- **⚡ Concurrency**: Uses threading to make the scan process faster and more efficient.
- **🛑 Graceful Shutdown**: Stops cleanly with a hotkey—no crashing allowed!

---

## 🗂️ Repository Structure

Here's what you’ll find in this repository:


# 🕵️‍♂️ BLE-Sniffer

Welcome to the **BLE-Sniffer** repository! 🎉 This is your one-stop toolkit for scanning and logging Bluetooth Low Energy (BLE) devices. Whether you’re a network security enthusiast, a device tracker, or a researcher, this project will light up your Bluetooth world! 🔥

---

## 🌟 Overview

### 🎯 Purpose

The **BLE-Sniffer** exists to make scanning and logging BLE devices a breeze! From **network monitoring** to **device tracking** and **research**, this repository has something for everyone.

---

### 🚀 Features

- **🔍 Bluetooth Scanning**: Detects and logs nearby BLE devices.
- **🏷️ Vendor Identification**: Matches MAC addresses to manufacturers (like a Bluetooth Sherlock Holmes 🕵️‍♂️).
- **📄 Detailed Logging**: Stores insights in an SQLite database for easy access.
- **📂 Log Management**: Automatically deletes older logs to keep things tidy.
- **⚡ Concurrency**: Uses threading to make the scan process faster and more efficient.
- **🛑 Graceful Shutdown**: Stops cleanly with a hotkey—no crashing allowed!

---

## 🗂️ Repository Structure

Here's what you’ll find in this repository:



```
standalone/
└── scanners/
    ├── logs/                  # Log files live here
    ├── sniff_my_ble.py        # Python script for scanning BLE devices
    ├── scan_bluetooth.ps1     # PowerShell script for Windows Bluetooth scanning
    └── bluetooth_devices.db   # SQLite database for device logs
```



---

## 🛠️ Scripts

### 🐍 Python Script: `sniff_my_ble.py`

This Python script is the star of the show! 🌟 It scans for BLE devices, retrieves additional data, and logs everything into an SQLite database.

#### 🔑 Key Features:
- **Bluetooth Scanning**: Uses the `bluetooth` module to detect BLE devices.
- **Vendor Detective**: Matches MAC prefixes to vendors like Apple 🍎 or Samsung 📱.
- **Extra Info**: Fetches additional details using the `bluetoothctl` command.
- **Database Logging**: Logs everything neatly into an SQLite database.
- **Log Management**: Keeps only the 3 most recent log files—no clutter! 🧹
- **Smooth Shutdown**: Can be terminated with `Ctrl+C` or `Cmd+C`.

---

### 🎮 PowerShell Script: `scan_bluetooth.ps1`

This script is designed for Windows users who want to scan Bluetooth devices with style. 🎩

#### 🔑 Key Features:
- **Device Scanning**: Uses the `Get-PnpDevice` cmdlet to find Bluetooth devices.
- **Logging**: Saves results and errors with timestamps.
- **Colorful Feedback**: Outputs messages with colors and emojis for better readability. 🌈
- **Scan Intervals**: Offers the flexibility to choose between scan intervals or continuous scanning.
- 






3 references

Here is a proposed changelog for the README.md file:
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



---

## 📝 Changelog

### v1.2.0 (2025-04-16)
- **PowerShell Script Enhancements (`scan_bluetooth.ps1`)**:
  - Added dynamic log file configuration via parameters and environment variables.
  - Improved error handling with detailed exception messages.
  - Introduced logging levels (`INFO`, `ERROR`, `OK`) for better log clarity.
  - Ensured compatibility checks for required cmdlets (`Get-PnpDevice`).
  - Modularized functions for reusability and maintainability.
  - Added fallback handling for missing device properties.

- **Documentation Updates**:
  - Added a detailed description of the `scan_bluetooth.ps1` script.
  - Updated usage instructions for database initialization scripts.
  - Refined repository structure and overview sections in the README.
  - Included examples for Python and PowerShell scripts.

---

### v1.1.0 (2025-03-25)
- Enhanced `sniff_my_ble.py` with asynchronous functions and improved logging.
- Updated `scan_bluetooth.ps1` with colorful feedback and scan interval options.
- Improved vendor lookup with a comprehensive MAC prefix list.
- Introduced `app.py` for a Flask-based web interface.
- Updated documentation to reflect new features and improvements.

---

### v1.0.0 (Initial Release)
- Introduced `sniff_my_ble.py` and `scan_bluetooth.ps1`.
- Set up SQLite database for logging BLE data.
- Implemented basic vendor identification.

---
