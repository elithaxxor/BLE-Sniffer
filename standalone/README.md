
# BLE-Sniffer+Scanner || Standalone 🛰️🔎

<p align="center">
  <img src="https://img.shields.io/badge/Bluetooth-Low%20Energy-blue?style=for-the-badge&logo=bluetooth"/>
  <img src="https://img.shields.io/badge/Sniffer-Tool-green?style=for-the-badge&logo=powerbi"/>
</p>

Welcome to **BLE-Sniffer Standalone**!  
This powerful utility empowers developers, researchers, and security enthusiasts to sniff, log, and analyze Bluetooth Low Energy (BLE) communications with **ease** and **flexibility**. Whether you’re debugging your smart devices🕹️, reverse engineering BLE protocols🧩, or monitoring Bluetooth environments in real-time, this tool is designed to make your BLE adventures insightful and efficient.

---

## ✨ What is BLE-Sniffer Standalone?

**BLE-Sniffer Standalone** is a Python-based application built to capture BLE packets, decode advertising and connection events, and present the data in a human-readable format—no complicated infrastructure required! Simply deploy, run, and start inspecting BLE traffic around you.

- **No dependencies on other repos.**
- **Suitable for laptops, Raspberry Pi, and desktops.**
- **Focus on simplicity and rapid insight.**

---

## 🎯 Features

| Feature                           | Description                                                                          | Icon      |
|------------------------------------|--------------------------------------------------------------------------------------|-----------|
| **Device Scanning**                | Detects and lists all broadcasting BLE devices in real time.                        | 🛰️         |
| **Packet Logging**                 | Records advertisements, connection requests, and control packets.                   | 📜         |
| **Live Decoding**                  | Decodes common BLE advertising/report fields on the fly.                            | 🧬         |
| **Export Capability**              | Logs can be exported to text/CSV for later analysis.                                | 📤         |
| **Simple Controls**                | Command-line interface for fast usage and automation.                               | 💡         |
| **Cross Platform**                 | Runs anywhere Python and compatible Bluetooth hardware are available.                | 🖥️         |

---

## 🚀 Quick Start

### 1. Prerequisites

- **Python 3.x** 🐍  
- **BLE Dongle or Adapter** supporting sniffing (recommended: [nRF51822 Dongle](https://www.nordicsemi.com/Products/Development-hardware/nRF51822-Dongle) or similar)
- `pip` for installing Python dependencies, if required

### 2. Installation

Clone this repository and dive into the `standalone` directory:

```sh
git clone https://github.com/elithaxxor/BLE-Sniffer.git
cd BLE-Sniffer/main_pi/standalone
```

(Optional) Set up a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

Install requirements (`requirements.txt` if present):

```sh
pip install -r requirements.txt
```

> **Tip:** If no requirements file, this tool likely uses `pyserial`, `bleak`, or similar libraries; check codebase comments for hints.

---

### 3. Usage 🏃‍♂️

Basic usage from the terminal:

```sh
python ble_sniffer.py
```
or, replace the filename with the actual main script's name if different.

**Command-Line Options:**  
Check built-in help:
```sh
python ble_sniffer.py --help
```
Typical options may include:

| Option             | Description                            | Example                           |
|--------------------|----------------------------------------|-----------------------------------|
| `--interface`      | Specify BLE interface/hardware         | `--interface hci0`                |
| `--output`         | Save output to specific file           | `--output scan_results.csv`       |
| `--duration`       | Set scan/sniff duration (seconds)      | `--duration 120`                  |

All scanned BLE packets and meta-information will be shown in your terminal and can be logged, filtered, or piped for further processing.

---

## 📁 Folder Structure

```
standalone/
├── ble_sniffer.py     # Main sniffer script (example)
├── utils.py           # Helper utilities (if present)
├── requirements.txt   # Python dependencies
├── README.md          # You're here!
└── logs/              # (Optional) Output directory for logs
```

> Filename(s) may differ; replace with actual script names if needed.

---

## 🏆 Use Cases

- **IoT Device Analysis:**  
  Sniff and decode BLE communication between fitness trackers, beacons, smart locks, or other embedded devices.
- **Protocol Reverse Engineering:**  
  Identify unknown profiles or proprietary data in custom BLE packets.
- **Security Auditing:**  
  Detect weak pairing, sniff data exfiltration, or monitor for rogue advertisements.
- **Development Debugging:**  
  Test and verify your BLE code under real-world radio conditions.

---

## 🦾 How It Works

1. **Scan:** Continuously scans for BLE advertising and connection packets.
2. **Log:** Captures raw packets, hone in on specific devices by MAC or UUID.
3. **Decode:** Attempts to parse key fields: device name, manufacturer data, TX power, etc.
4. **Export/Report:** Save logs for Wireshark or CSV for easy post-analysis.

*Note: Sniffing encrypted BLE connections is out of scope and generally requires hardware-level attacks.*

---

## ⌨️ Commands Cheat Sheet

| Use Case                              | Command Example                             |
|----------------------------------------|---------------------------------------------|
| Scan for devices 60s, save to CSV      |  `python ble_sniffer.py --duration 60 --output scan.csv` |
| Verbose output                        |  `python ble_sniffer.py -v`                 |
| Specify Bluetooth dongle               |  `python ble_sniffer.py --interface hci1`   |

---

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
