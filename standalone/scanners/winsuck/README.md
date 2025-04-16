
# 🕵️‍♂️ BLE-Sniffer

Welcome to the **BLE-Sniffer** repository! 🎉 Your ultimate toolkit for scanning and logging Bluetooth Low Energy (BLE) devices. Whether you’re a network security enthusiast, a device tracker, or a researcher, this project has something for you.

Development Status: **Alpha Stage** – Under active development. Expect frequent updates and potential bugs.

---

## 🌟 Overview

The **BLE-Sniffer** makes scanning and logging BLE devices effortless. It supports **standalone scripts** and a **web-based interface** for flexibility.

### 🎯 Purpose

- **Packet Sniffing**: Capture and analyze BLE packets.
- **Multi-Device Support**: Monitor multiple BLE devices simultaneously.
- **Real-Time Monitoring**: Track and log BLE communications live.

---

## 🚀 Features

- **🔍 Bluetooth Scanning**: Detects and logs nearby BLE devices.
- **🏷️ Vendor Identification**: Maps MAC addresses to manufacturers.
- **📄 Detailed Logging**: Saves data into an SQLite database.
- **📂 Log Management**: Automatically removes old logs to prevent clutter.
- **⚡ High Performance**: Uses threading and multiprocessing for efficiency.
- **🛑 Graceful Shutdown**: Cleanly exits with hotkeys.

---

## 🌐 Web Interface (`app.py`)

The `app.py` script provides a sleek web interface to display Bluetooth device logs.

### 🔑 Key Features:
- **Web Framework**: Built on Flask for simplicity.
- **Database Interaction**: Fetches records from the SQLite database.
- **User-Friendly UI**: Displays logs in a table format.

### 🏃 How to Run:
1. Install Flask:
    ```bash
    pip install flask
    ```
2. Run the app:
    ```bash
    python app.py
    ```
3. Access the web interface at `http://127.0.0.1:5000`.

---

## 🗂️ Repository Structure

Here’s what you’ll find in this repository:

```
standalone/
├── scanners/
│   ├── logs/                  # Log files
│   ├── sniff_my_ble.py        # Python script for BLE scanning
│   ├── scan_bluetooth.ps1     # PowerShell script for Windows scanning
│   ├── bluetooth_devices.db   # SQLite database for logs
├── create_db/
│   ├── bash/                  # Bash script to initialize SQLite database
│   ├── c/                     # C program to initialize SQLite database
│   ├── powershell/            # PowerShell script for database creation
```

---

## 🛠️ Scripts

### 🐍 Python Script: `sniff_my_ble.py`

This script is the core of the project, enabling BLE scanning and logging.

#### Key Features:
- **Bluetooth Scanning**: Detects BLE devices.
- **Vendor Detection**: Matches MAC prefixes to manufacturers.
- **Database Logging**: Logs data into an SQLite database.
- **Concurrency**: Implements threading for faster scanning.
- **Log Management**: Automatically removes old logs.

---

### 🎮 PowerShell Script: `scan_bluetooth.ps1`

Designed for Windows users, this script scans BLE devices and logs results.

#### Key Features:
- **Device Scanning**: Uses `Get-PnpDevice` to find Bluetooth devices.
- **Logging**: Saves results and errors with timestamps.
- **Colorful Feedback**: Outputs messages with colors and emojis.
- **Scan Intervals**: Supports periodic or continuous scanning.

---

### 🔧 Database Initialization Scripts

The repository includes scripts in **Bash**, **PowerShell**, and **C** to initialize the SQLite database. These scripts create the database if it doesn’t already exist.

#### Usage:
1. Navigate to the respective directory (e.g., `create_db/bash`).
2. Run the script:
    ```bash
    ./create_db.sh
    ```

---

## 📝 Changelog

### v1.1.0 (2025-03-25)
- Enhanced `sniff_my_ble.py` with asynchronous functions and improved logging.
- Updated `scan_bluetooth.ps1` with colorful feedback and scan interval options.
- Improved vendor lookup with a comprehensive MAC prefix list.
- Introduced `app.py` for a Flask-based web interface.
- Updated documentation to reflect new features and improvements.

### v1.0.0 (Initial Release)
- Introduced `sniff_my_ble.py` and `scan_bluetooth.ps1`.
- Set up SQLite database for logging BLE data.
- Implemented basic vendor identification.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

We hope you find **BLE-Sniffer** helpful for your BLE-related projects. If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request. Happy sniffing! 🕵️‍♂️
```

This updated `README.md` reflects the recent changes and provides clear instructions for using the project. Let me know if you'd like further refinements!
```markdown
# Bluetooth Scanner Script

This repository contains a PowerShell script `scan_bluetooth.ps1` designed to scan for active Bluetooth devices on a Windows machine. The script logs the results, handles errors, and provides user-friendly output.

## Overview

The `scan_bluetooth.ps1` script performs the following tasks:
- Scans for active Bluetooth devices using the `Get-PnpDevice` cmdlet.
- Logs the scan results and any errors to a log file.
- Provides console output with different levels of messages (info, success, error).
- Allows the user to choose scan intervals or perform continuous scanning via a menu.

## Features

- **Logging**: All scan results and messages are logged with timestamps.
- **User Feedback**: Messages are displayed in the console with different colors to indicate their type (info, success, error).
- **Menu for Scan Intervals**: Users can select scan intervals of 30 seconds, 3 minutes, 10 minutes, or continuous scanning.
- **Error Handling**: The script includes error handling to catch and log any issues encountered during the Bluetooth scan process.
- **Manufacturer Identification**: Identifies and categorizes Bluetooth devices based on MAC address prefixes using a predefined list.
- **Additional Device Details**: Retrieves additional details such as device type and placeholder for signal strength (RSSI).

## Script Details

### Functions

#### `Log`
Logs messages to the log file with a timestamp.

```powershell
function Log {
    param ($Level, $Message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}
```

#### `Info`
Displays and logs informational messages.

```powershell
function Info {
    param ($Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}
```

#### `Success`
Displays and logs success messages.

```powershell
function Success {
    param ($Message)
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}
```

#### `ErrorMsg`
Displays and logs error messages.

```powershell
function ErrorMsg {
    param ($Message)
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}
```

#### `Identify-Manufacturer`
Identifies the manufacturer based on the MAC address prefix.

```powershell
function Identify-Manufacturer {
    param ($MAC)
    $prefix = $MAC.Substring(0, 8)
    return $MAC_PREFIXES[$prefix] -or "Unknown"
}
```

#### `Scan-Bluetooth`
Performs the Bluetooth scan, identifies the manufacturer, and logs the results. If no Bluetooth devices are found, it logs an error message.

```powershell
function Scan-Bluetooth {
    try {
        Info "Scanning Bluetooth devices using Get-PnpDevice..."
        $devices = Get-PnpDevice -Class Bluetooth -Status OK

        if ($devices.Count -eq 0) {
            ErrorMsg "No active Bluetooth devices found."
        } else {
            foreach ($device in $devices) {
                $name = $device.FriendlyName
                $id = $device.InstanceId
                $manufacturer = Identify-Manufacturer $id
                $deviceType = $device.DeviceClass
                $rssi = "RSSI information not available in PowerShell"

                Success "Found: $name ($id) - Manufacturer: $manufacturer - Type: $deviceType - RSSI: $rssi"
            }
        }
    } catch {
        ErrorMsg "Error scanning Bluetooth devices: $_"
    }
}
```

#### `Show-Menu`
Displays menu options for the user to choose the scan interval.

```powershell
function Show-Menu {
    Write-Host "Choose scan interval:"
    Write-Host "1. Scan every 30 seconds"
    Write-Host "2. Scan every 3 minutes"
    Write-Host "3. Scan every 10 minutes"
    Write-Host "4. Continuous scan"
    Write-Host "5. Exit"
}
```

#### `Get-Interval`
Maps the user’s choice to the corresponding interval in seconds.

```powershell
function Get-Interval {
    param ($choice)
    switch ($choice) {
        1 { return 30 }
        2 { return 180 }
        3 { return 600 }
        4 { return 0 }
        default { return -1 }
    }
}
```

### Main Script Logic

The main script logic includes a loop that continuously displays the menu, processes the user's choice, and sets up the scan interval accordingly.

```powershell
# Main loop
while ($true) {
    Show-Menu
    $choice = Read-Host "Enter your choice (1-5)"
    $interval = Get-Interval $choice

    if ($interval -eq -1) {
        Write-Host "Invalid choice. Please select a valid option." -ForegroundColor Red
        continue
    } elseif ($interval -eq 0) {
        Info "Starting continuous Bluetooth scan..."
        while ($true) {
            Scan-Bluetooth
            Start-Sleep -Seconds 30
        }
    } elseif ($choice -eq 5) {
        Write-Host "Exiting..."
        break
    } else {
        Info "Starting Bluetooth scan every $interval seconds..."
        while ($true) {
            Scan-Bluetooth
            Start-Sleep -Seconds $interval
        }
    }
    break
}

Success "Script terminated. Log saved to $LogFile"
```

## Usage

### Prerequisites

- Windows operating system with PowerShell installed.
- Bluetooth functionality enabled on the machine.

### Running the Script

1. Open PowerShell with administrative privileges.
2. Navigate to the directory containing the `scan_bluetooth.ps1` script.
3. Execute the script by running the following command:
   ```powershell
   .\scan_bluetooth.ps1
   ```

### Log File

The script generates a log file named `bluetooth_scan.log` in the same directory as the script. The log file contains timestamps and details of the Bluetooth scan results.

### Example Output

```plaintext
[!] Starting Bluetooth scan...
[!] Scanning Bluetooth devices using Get-PnpDevice...
[+] Found: Bluetooth Device (ID: 12345) - Manufacturer: Example Inc. - Type: Computer - RSSI: RSSI information not available in PowerShell
[+] Scan complete. Log saved to bluetooth_scan.log
```

## Error Handling

The script includes error handling to catch and log any issues encountered during the Bluetooth scan process.

---

This repository aims to provide robust scripts for scanning and logging Bluetooth device data efficiently and maintainably.
```

This updated `README.md` includes all the changes and enhancements made to the `scan_bluetooth.ps1` script, detailing the new features, script details, and usage instructions.
