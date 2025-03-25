# 🔍 Bluetooth Scanner Script

Welcome to the **Bluetooth Scanner Script** repository! 🎉 This is your one-stop solution for scanning active Bluetooth devices on Linux, macOS, and Windows. It’s like having a Bluetooth detective in your terminal! 🕵️‍♂️

---

## 🚀 Overview

### 🛠️ `scan_bluetooth.sh`
The star of the show! 🌟 This script is your trusted companion for scanning active Bluetooth devices on **Linux** and **macOS**.

---

## 💡 Features

✨ **Logging**: Keep your logs neat and tidy in `bluetooth_scan.log` (timestamps included!).  
✨ **User Feedback**: Get console feedback with cool colored messages and symbols like `[+]`, `[-]`, and `[!]`.  
✨ **OS Detection**: Smart enough to know whether you’re on Linux or macOS. 🧠  
✨ **Bluetooth Scanning**: Uses the tools of the trade: `bluetoothctl` (Linux) and `system_profiler` (macOS).  
✨ **Manufacturer Detective**: Categorizes devices by their MAC address prefixes. Sherlock would be proud! 🕵️  
✨ **Extra Details**: Shows RSSI (signal strength) and device type for Linux scans.  
✨ **Scan Intervals Menu**: Offers flexible scanning intervals—30 seconds, 3 minutes, 10 minutes, or go full throttle with continuous scanning! 🔄

---

## 🧐 Script Details

### 🧩 Functions Breakdown
Here’s what the script is packing under the hood:

- **`log`**: Writes messages (with timestamps!) to `bluetooth_scan.log`.  
- **`info`**: Displays *important updates* (you’ll never feel left out).  
- **`success`**: Cheers you on with success messages! 🎉  
- **`error`**: Catches problems and handles them gracefully. 😅  
- **`check_dependencies`**: Makes sure your system has all the tools it needs. 🛠️  
- **`identify_manufacturer`**: Plays matchmaker between MAC addresses and manufacturers.  
- **`scan_linux`**: Works its magic on Linux. 🐧  
- **`scan_macos`**: Does its thing on macOS. 🍎  
- **`show_menu`**: A friendly menu for choosing scan intervals.  
- **`get_interval`**: Translates your choice into seconds (because math).  
- **`scan_based_on_os`**: Figures out your OS and runs the right scan.  
- **`main`**: The brains of the operation—handles the entire workflow. 🧠

---

## 🛠️ Usage

### ✅ Prerequisites

- A Linux or macOS system.  
- Make sure Bluetooth is enabled (you can’t scan ghosts 👻).

### 🏃‍♂️ How to Run

1. Open your terminal (don’t forget admin privileges!).  
2. Navigate to the script’s directory.  
3. Run this magic command:  
   ```bash
   ./scan_bluetooth.sh
