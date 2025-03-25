# 🕵️‍♂️ BLE-Sniffer

Welcome to the **BLE-Sniffer** repository! 🎉 This is your one-stop toolkit for scanning and logging Bluetooth Low Energy (BLE) devices. Whether you’re a network security enthusiast, a device tracker, or a researcher, this project will light up your Bluetooth world! 🔥

---

## 🌟 Overview
    =-- standalone or webinterface. 
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



