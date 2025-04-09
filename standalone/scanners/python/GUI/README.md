# 🔍 BLE-Sniffer: Command Line Interface

<div align="center">
  <img src="https://img.shields.io/badge/Bluetooth-LE-blue?style=for-the-badge&logo=bluetooth&logoColor=white" alt="Bluetooth LE"/>
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x"/>
  <img src="https://img.shields.io/badge/Security-Research-red?style=for-the-badge&logo=shield&logoColor=white" alt="Security Research"/>
  <img src="https://img.shields.io/badge/IoT-Analysis-green?style=for-the-badge&logo=iobroker&logoColor=white" alt="IoT Analysis"/>
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/username/BLE-Sniffer/main/assets/ble-sniffer-logo.png" alt="BLE Sniffer Logo" width="300"/>
</p>

> 📡 **BLE-Sniffer** is a powerful Bluetooth Low Energy scanning and analysis tool that helps security researchers, IoT developers, and network administrators discover, monitor, and analyze BLE devices in their vicinity.

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🧰 Requirements](#-requirements)
- [🚀 Installation](#-installation)
- [🎮 Usage Guide](#-usage-guide)
- [🔍 Scanning Modes](#-scanning-modes)
- [📊 Output Options](#-output-options)
- [📈 Data Analysis](#-data-analysis)
- [⚙️ Advanced Configuration](#️-advanced-configuration)
- [📱 Device Examples](#-device-examples)
- [🔐 Security Considerations](#-security-considerations)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🌟 Overview

**BLE-Sniffer** (`sniff_my_ble.py`) is a sophisticated command-line utility designed to scan, detect, and analyze Bluetooth Low Energy (BLE) devices in your environment. Built with Python and leveraging the powerful `bluepy` library, this tool provides comprehensive insights into BLE device characteristics, advertisements, signal strengths, and more.

<p align="center">
  <img src="https://raw.githubusercontent.com/username/BLE-Sniffer/main/assets/terminal-demo.gif" alt="Terminal Demo" width="700"/>
</p>

Whether you're conducting security research, developing IoT applications, or simply curious about BLE devices around you, BLE-Sniffer offers an easy-to-use interface with powerful scanning capabilities and detailed output options.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Comprehensive Scanning** | Detects all advertising BLE devices in range |
| 📡 **Signal Strength Analysis** | Monitors and reports RSSI values for proximity estimation |
| 🆔 **Device Identification** | Captures device names, MAC addresses, and manufacturer data |
| 📊 **Service Discovery** | Identifies advertised GATT services and characteristics |
| 📝 **Detailed Logging** | Multiple verbosity levels with customizable output |
| 📂 **Export Capabilities** | Save results as JSON, CSV, or plain text |
| 🔄 **Continuous Monitoring** | Track BLE devices over time with timestamps |
| 🔋 **Battery-Efficient** | Optimized scanning to minimize host device power consumption |
| 🧩 **Filter Options** | Target specific devices by name, address, or service UUID |
| 🎨 **Colorized Output** | Enhanced terminal visualization for better readability |

---

## 🧰 Requirements

### Hardware Requirements

- **Bluetooth 4.0+ adapter** with BLE support
- **Linux-based system** (Raspberry Pi, Ubuntu, Debian, etc.)
- **USB port** (if using external Bluetooth adapter)

### Software Requirements

- **Python 3.6+**
- **Bluepy library** (>=1.3.0)
- **Linux packages**: `bluez`, `bluez-utils`, `python3-dev`, `libbluetooth-dev`
- **Root privileges** (for BLE scanning functions)

---

## 🚀 Installation

### Step 1: Install System Dependencies

```bash
# For Debian/Ubuntu/Raspberry Pi OS
sudo apt update
sudo apt install -y python3-pip python3-dev build-essential libglib2.0-dev libbluetooth-dev bluez bluez-tools
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/username/BLE-Sniffer.git
cd BLE-Sniffer/standalone/scanners/python/CLI
```

### Step 3: Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

### Step 4: Verify Bluetooth Functionality

```bash
# Check if Bluetooth adapter is recognized
hciconfig

# Enable Bluetooth adapter if needed
sudo hciconfig hci0 up
```

### Step 5: Run a Test Scan

```bash
sudo python3 sniff_my_ble.py --scan-time 5
```

<details>
<summary>📦 <b>Dependencies explained</b></summary>

```
bluepy>=1.3.0     # Core Bluetooth LE library
pybluez>=0.23     # Alternative Bluetooth library
colorama>=0.4.4   # For terminal color output
argparse>=1.4.0   # Command line argument parsing
tqdm>=4.62.3      # Progress bar visualization
pyyaml>=6.0       # Configuration file parsing
```
</details>

---

## 🎮 Usage Guide

### Basic Command

```bash
sudo python3 sniff_my_ble.py
```

### Command-Line Options

```bash
sudo python3 sniff_my_ble.py [OPTIONS]
```

<details>
<summary>🔧 <b>Available options</b></summary>

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-t, --scan-time SECONDS` | Duration of scan in seconds (default: 10) |
| `-i, --interface INTERFACE` | Bluetooth interface to use (default: hci0) |
| `-o, --output FILE` | Output file for scan results |
| `-f, --format {text,json,csv}` | Output format (default: text) |
| `-v, --verbose` | Increase output verbosity |
| `-q, --quiet` | Suppress non-essential output |
| `-n, --name NAME` | Filter devices by name (substring match) |
| `-a, --address MAC` | Filter by Bluetooth MAC address |
| `-s, --service UUID` | Filter by service UUID |
| `-r, --rssi RSSI` | Filter by minimum RSSI value (e.g., -70) |
| `-c, --continuous` | Run in continuous scanning mode |
| `-d, --delay SECONDS` | Delay between continuous scans (default: 1) |
| `--passive` | Use passive scanning (less detection, more battery efficient) |
| `--active` | Use active scanning (default) |
| `--no-color` | Disable colored output |
| `--sort {name,rssi,address}` | Sort results by specified field |
| `--monitor DEVICE` | Continuously monitor a specific device |
| `--resolve-names` | Attempt to resolve device names (slower) |
| `--raw` | Show raw advertisement data |
</details>

### Example Commands

```bash
# Basic scan for 30 seconds
sudo python3 sniff_my_ble.py -t 30

# Save results to JSON file
sudo python3 sniff_my_ble.py -o scan_results.json -f json

# Filter devices by name
sudo python3 sniff_my_ble.py -n "Fitbit" -v

# Monitor a specific device continuously
sudo python3 sniff_my_ble.py --monitor "XX:XX:XX:XX:XX:XX" -c

# Find only nearby devices with strong signal
sudo python3 sniff_my_ble.py -r -60

# Scan for devices with a specific service
sudo python3 sniff_my_ble.py -s "1812" -v
```

---

## 🔍 Scanning Modes

BLE-Sniffer offers multiple scanning modes to suit different needs:

### 1. 🔦 Standard Scan

```bash
sudo python3 sniff_my_ble.py -t 10
```

A quick scan that identifies advertising BLE devices in range, showing basic information like addresses, names, and signal strength.

### 2. 🔄 Continuous Monitoring

```bash
sudo python3 sniff_my_ble.py -c -d 2
```

Continuously scans for devices, updating the display as new devices are discovered or existing devices update their advertisements. Great for tracking devices over time.

### 3. 🎯 Target-Specific Monitoring

```bash
sudo python3 sniff_my_ble.py --monitor "XX:XX:XX:XX:XX:XX" -v
```

Focuses on a single device, providing detailed information about its advertisements, signal strength changes, and other dynamics.

### 4. 🔋 Passive Scanning

```bash
sudo python3 sniff_my_ble.py --passive
```

Less intrusive scanning that doesn't request additional information from devices. Better for battery life and stealth, but provides less detailed information.

### 5. 💪 Active Scanning (Default)

```bash
sudo python3 sniff_my_ble.py --active
```

Requests additional information from advertising devices, providing more complete data at the cost of being more detectable and using more power.

---

## 📊 Output Options

### Terminal Output

The CLI provides rich, colorized terminal output showing:

- 📱 Device names and MAC addresses
- 📶 Signal strength (RSSI) with visual indicators
- 🔑 Advertised services and UUID information
- 🏭 Manufacturer data (when available)
- 🔋 Battery levels (if provided by device)

```
[2023-04-09 15:42:17] 📱 Device: Fitbit Charge 5 (XX:XX:XX:XX:XX:XX)
  📶 Signal: -67 dBm [███████░░░] (Good)
  🏭 Manufacturer: Fitbit Inc.
  🔑 Services: 0x180F (Battery), 0x180D (Heart Rate)
  🔋 Battery: 72%
```

### File Exports

BLE-Sniffer can export data in multiple formats:

#### JSON Output
```json
{
  "timestamp": "2023-04-09T15:42:17",
  "devices": [
    {
      "name": "Fitbit Charge 5",
      "address": "XX:XX:XX:XX:XX:XX",
      "rssi": -67,
      "manufacturer_data": "0006000D19D891B301",
      "services": ["0x180F", "0x180D"],
      "connectable": true,
      "first_seen": "2023-04-09T15:42:10",
      "last_seen": "2023-04-09T15:42:17"
    }
  ]
}
```

#### CSV Output
```
timestamp,name,address,rssi,manufacturer,services,connectable
2023-04-09T15:42:17,Fitbit Charge 5,XX:XX:XX:XX:XX:XX,-67,Fitbit Inc.,0x180F|0x180D,true
```

---

## 📈 Data Analysis

The BLE-Sniffer provides several methods to analyze the data it collects:

### RSSI-Based Proximity Estimation

```python
def estimate_distance(rssi):
    """Roughly estimate distance based on RSSI value."""
    if rssi >= -50:
        return "Very close (< 1m)"
    elif rssi >= -65:
        return "Close (1-3m)"
    elif rssi >= -80:
        return "Medium (3-10m)"
    else:
        return "Far (10m+)"
```

### Manufacturer Data Parsing

```python
def parse_manufacturer_data(manufacturer_bytes):
    """Parse manufacturer-specific data from advertisement."""
    # Implementation details from sniff_my_ble.py
```

### Device Classification

Based on advertised services and manufacturer data, BLE-Sniffer can often identify device types:

- 🎧 **Audio devices** (headphones, speakers)
- 💓 **Health devices** (heart rate monitors, fitness trackers)
- 🔑 **Proximity/security devices** (key finders, smart locks)
- 🏠 **Smart home devices** (thermostats, lights, sensors)

---

## ⚙️ Advanced Configuration

### Configuration File

BLE-Sniffer supports YAML configuration files for advanced settings:

```yaml
# config.yaml
bluetooth:
  interface: hci0
  active_scan: true
  scan_interval: 1.28
  scan_window: 1.28

scanning:
  default_duration: 10
  continuous_delay: 1
  passive_mode: false
  resolve_generic_names: true
  
output:
  format: "text"
  file: null
  color_enabled: true
  progress_bar: true
  timestamp_format: "%Y-%m-%d %H:%M:%S"

filters:
  name: null
  address: null
  service: null
  rssi_min: -100
  manufacturer_id: null
```

Use your configuration file with:

```bash
sudo python3 sniff_my_ble.py --config config.yaml
```

### Custom Plugin Development

The script includes hooks for custom plugins to extend its functionality:

```python
# Example of extending with a custom plugin
class MyCustomPlugin:
    def __init__(self):
        self.name = "Custom BLE Analyzer"
        
    def process_device(self, device):
        # Custom analysis logic
        pass
        
    def report(self):
        # Custom reporting logic
        pass
```

---

## 📱 Device Examples

BLE-Sniffer can detect a wide range of devices:

### 🎧 Audio Devices

```
[2023-04-09 15:45:23] 📱 Device: Bose QuietComfort Earbuds (XX:XX:XX:XX:XX:XX)
  📶 Signal: -58 dBm [████████░░] (Very Good)
  🏭 Manufacturer: Bose Corporation
  🔑 Services: 0x1108 (Audio Source), 0x110B (Audio Sink)
  🔋 Battery: 85%
```

### 💓 Health & Fitness

```
[2023-04-09 15:46:12] 📱 Device: Polar H10 (XX:XX:XX:XX:XX:XX)
  📶 Signal: -72 dBm [██████░░░░] (OK)
  🏭 Manufacturer: Polar Electro Oy
  🔑 Services: 0x180D (Heart Rate)
```

### 🏠 Smart Home

```
[2023-04-09 15:47:05] 📱 Device: Eve Thermo (XX:XX:XX:XX:XX:XX)
  📶 Signal: -84 dBm [████░░░░░░] (Weak)
  🏭 Manufacturer: Eve Systems
  🔑 Services: 0x1800 (Generic Access), 0x1801 (Generic Attribute)
```

---

## 🔐 Security Considerations

### Required Privileges

⚠️ BLE-Sniffer requires root/administrator privileges to access the Bluetooth hardware layer:

```bash
sudo python3 sniff_my_ble.py
```

### Ethical Usage

⚠️ This tool should only be used for:
