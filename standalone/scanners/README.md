
```markdown
##### This is a light implimentatation.  "sniff_my_ble" is asynchonized with multi-threading, and works well with data transfer, and IO tasks. I've implimented "sniff_my_ble_cpuBound.py" if you plan to expand the project and require CPU processes (such as for data aggregation. #####


*The async magic of sniff_my_ble paired with multi-threading is a fantastic choice for smooth data transfer and I/O tasks—keeping it light and nimble.  

*Added sniff_my_ble_cpuBound.py for those CPU-heavy jobs (like data aggregation) is a brilliant move! It’s like giving your project a turbo boost for future growth.  

*Have you run into any bottlenecks yet, or are you just future-proofing like a pro? Either way, this setup is sleek, smart, with many optinos to chose from.

```

## The standalone versions can be found as CLI or GUI applications. 

```markdown
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
```

## 🌟 Overview

### 🎯 Purpose

Why does this repo exist? To make scanning and logging BLE devices as easy as pie! 🥧 Whether you're into **network security**, **device tracking**, or **research**, this toolkit has your back.

### 🚀 Features

✨ **Bluetooth Scanning**: Sniffs out nearby BLE devices.  
✨ **Vendor Detective**: Matches MAC address prefixes to manufacturers (like a Bluetooth CSI 🧬).  
✨ **Extra Details**: Fetches juicy info like device type and signal strength.  
✨ **SQLite Database Logging**: Keeps detailed records of all your discoveries.  
✨ **Log File Magic**: Manages logs like a pro—out with the old, in with the new! 🗂️  
✨ **Threading Power**: Multitasks like a champ for faster data collection.  
✨ **Smooth Shutdown**: Exits gracefully at the press of a button (no drama here!).

---


---

## 🛠️ Scripts

### 🐍 Python Script: `sniff_my_ble.py`

This Python wizard 🧙‍♂️ scans for nearby BLE devices, gathers extra details, and logs it all into an SQLite database. 

#### 🧩 Key Features:

- **Sniffer Mode**: Tracks down Bluetooth devices nearby.  
- **Vendor Detective**: Identifies manufacturers like Apple 🍎 or Samsung 📱.  
- **Extra Insights**: Fetches additional details using `bluetoothctl`.  
- **Database Logging**: Saves everything in an organized SQLite database.  
- **Log Management**: Keeps only the 3 most recent log files—clean and tidy! 🧹  
- **Threading**: Multitasks to speed up scanning and info fetching.  
- **Graceful Exit**: Stops with a hotkey (`Ctrl+C` or `Cmd+C`)—no crashing here! 🚦

---

### 🎮 PowerShell Script: `scan_bluetooth.ps1`

For our Windows warriors ⚔️, this PowerShell script scans for Bluetooth devices with style.

#### 🧩 Key Features:

- **Device Scanning**: Uses the `Get-PnpDevice` cmdlet to find devices.  
- **Logging**: Saves scan results with timestamps—because time is precious! ⏰  
- **Colorful Output**: Messages are color-coded for clarity and fun 🌈.  
- **Scan Intervals**: Choose between different scan intervals or go *continuous*. 🔄

---

## 🎉 How to Use

### ✅ Prerequisites

- **Python Script**:  
  - Python 3.x installed 🐍  
  - Bluetooth enabled on your device 🛠️  
  - Install the required modules:  
    ```bash
    pip install pybluez keyboard
    ```

- **PowerShell Script**:  
  - Windows operating system 🖥️  
  - Bluetooth enabled on your machine 📡

---

### 🏃‍♂️ Running the Python Script

1. Open a terminal with the right permissions.  
2. Navigate to the directory where `sniff_my_ble.py` is located.  
3. Run the script:  
   ```bash
   python sniff_my_ble.py
   ```

---

### 🎮 Running the PowerShell Script

1. Open PowerShell as an administrator.  
2. Navigate to the script’s directory.  
3. Run it like this:  
   ```powershell
   .\scan_bluetooth.ps1
   ```

---

## 🗂️ Log File Management

The scripts create log files in the `logs` folder. Each log is named with a timestamp (fancy, huh?) 🕒. Only the 3 most recent logs are kept, so your folder stays neat and tidy! 🧽

---

## 🔍 Example Output

### 🐍 Python Script

```plaintext
2025-03-24 17:45:10 - DEBUG - Starting Bluetooth scan...
2025-03-24 17:45:18 - DEBUG - Found 2 device(s).
2025-03-24 17:45:19 - DEBUG - Extra info for XX:XX:XX:XX:XX:XX: Device XX:XX:XX:XX:XX:XX
2025-03-24 17:45:19 - DEBUG - Logged device XX:XX:XX:XX:XX:XX (Device Name) with vendor Apple, Inc.
2025-03-24 17:45:19 - DEBUG - Extra info for YY:YY:YY:YY:YY:YY: Device YY:YY:YY:YY:YY:YY
2025-03-24 17:45:19 - DEBUG - Logged device YY:YY:YY:YY:YY:YY (Another Device) with vendor Samsung Electronics Co., Ltd.
2025-03-24 17:45:19 - DEBUG - Sleeping for 5 minutes before next scan...
```

---

### 🎮 PowerShell Script

```plaintext
[!] Starting Bluetooth scan... 🚀
[!] Scanning Bluetooth devices using Get-PnpDevice... 🔍
[+] Found: Bluetooth Device (ID: 12345) - Manufacturer: Example Inc. - Type: Computer - RSSI: RSSI information not available in PowerShell
[+] Scan complete. Log saved to bluetooth_scan.log 🎉
```

---

## 🛡️ Error Handling

Both scripts are equipped with error-handling magic to gracefully catch and log any hiccups along the way. No panic attacks here! 😌

---




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
