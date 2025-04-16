# BLE-Sniffer+Scanner || Standalone 🛰️🔎
**Skelaton Outlined Below Changelog**

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


**enterprise-ready skeleton, ready for deeper protocol handling!**
**see below for other details**

# 📦 `utils.py`

```python
# utils.py
"""
Utility module for BLE-Sniffer Standalone.
Handles formatting, file exports, color output, logging, and filtering.
"""

import datetime
import csv
from typing import List, Dict, Optional, Callable
import sys

# ===== Color Output for Terminal =====
class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def supports_color() -> bool:
    if sys.platform == 'win32':
        return False  # (Windows color support is iffy unless via colorama)
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

USE_COLOR = supports_color()


def cstr(txt, style):
    """Return colored string if terminal supports it"""
    if USE_COLOR:
        return f"{style}{txt}{Colors.ENDC}"
    else:
        return txt


# ===== MAC and Data Formatting =====
def format_mac(mac: str) -> str:
    return mac.upper().replace("-", ":").replace("_", ":")


def human_time(ts: Optional[float] = None) -> str:
    if ts is None:
        ts = datetime.datetime.now().timestamp()
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def truncate_hex(data: bytes, max_len=16) -> str:
    """Show bytes as hex; compact representation for printing"""
    if not data:
        return ""
    s = data[:max_len].hex().upper()
    if len(data) > max_len:
        s += f"...({len(data)} bytes)"
    return s


def decode_name(device, adv_data) -> str:
    name = getattr(device, "name", None)
    if not name:
        name = getattr(adv_data, "local_name", None)
    if not name:
        name = "<unknown>"
    return name


# ===== CSV and File Export =====
def write_csv(devices: List[Dict], filename: str, fields: Optional[List[str]] = None) -> None:
    """Write results to CSV."""
    if not devices:
        return
    if fields is None:
        fields = list(devices[0].keys())
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(devices)


def write_log(lines: List[str], filename: str) -> None:
    """Save plain text log report."""
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "
")


# ===== Filtering =====
def fuzzy_match(text: str, patterns: List[str]) -> bool:
    """
    Simple utility for substring match against a list of patterns (MAC, name etc).
    """
    if not patterns:
        return True  # no filter, always match
    return any(pattern.lower() in text.lower() for pattern in patterns)


# ===== Manufacturer Data Pretty Print =====
def prettify_manufacturer(manuf: dict) -> str:
    """Human-readable manufacturer data description (where available)"""
    if not manuf:
        return ""
    parts = []
    for k, v in manuf.items():
        s = f"0x{k:04X}: {truncate_hex(bytes(v))}"
        parts.append(s)
    return "; ".join(parts)


# ===== Logging (for developers/tests) =====
def debug(msg: str):
    ts = human_time()
    print(cstr(f"[DEBUG {ts}] {msg}", Colors.OKCYAN))

def warn(msg: str):
    ts = human_time()
    print(cstr(f"[WARNING {ts}] {msg}", Colors.WARNING))
```

---

# 🛰️ `ble_sniffer.py`

```python
# ble_sniffer.py
"""
BLE-Sniffer Standalone - Comprehensive BLE Advertisement Sniffer
Features:
- Scan BLE advertisements/passive scans
- Filter by MAC, name/substrings, or RSSI
- Log to CSV, plaintext, or just print
- Optional: Save extended Bluetooth info & manufacturer data
- Cross-platform: Linux/Mac/Windows (where supported by bleak)
"""

import asyncio
import argparse
from typing import List, Dict

from utils import (
    cstr, Colors, human_time, format_mac, decode_name, prettify_manufacturer,
    write_csv, write_log, fuzzy_match, debug, warn
)

try:
    from bleak import BleakScanner
except ImportError:
    print("ERROR: bleak module not found. Install with 'pip install bleak'")
    exit(1)

found_devices: List[Dict] = []
raw_log_lines: List[str] = []
EXTRA_FIELDS = ["address", "name", "timestamp", "rssi", "manufacturer_data", "details"]


def parse_args():
    parser = argparse.ArgumentParser(
        description="🔎 BLE Standalone Sniffer: Scan, filter, and log BLE-advertised devices"
    )
    parser.add_argument("--duration", type=int, default=30, help="Scan duration in seconds (default 30)")
    parser.add_argument("--mac", nargs="+", help="MAC address(es) (substring, case-insensitive) to filter")
    parser.add_argument("--name", nargs="+", help="Device name(s) (substring, case-insensitive) to filter")
    parser.add_argument("--min-rssi", type=int, default=None, help="Minimum RSSI threshold to include")
    parser.add_argument("--output", type=str, help="CSV file to write the device log")
    parser.add_argument("--log", type=str, help="TXT file to write text log")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print details per device")
    parser.add_argument("--unique", action="store_true", help="Only print/log each detected address once (default)")
    parser.add_argument("--repeat", action="store_true", help="Log every sighting (use with care!)")
    parser.add_argument("--details", action="store_true", help="Print full advertisement details (raw dump)")
    parser.add_argument("--sort", choices=["rssi", "time"], default="rssi", help="Sort output by RSSI or time")
    parser.add_argument("--no-color", action="store_true", help="Disable colored terminal output")
    parser.add_argument("--test", action="store_true", help="Print test record and exit (for debugging)")
    return parser.parse_args()


address_seen = set()

def log_and_print_device(device, adv_data, args):
    """
    Handles logging, filtering, printing one found device.
    Adds to found_devices and/or raw_log_lines as appropriate.
    """
    global address_seen
    address = format_mac(device.address)
    name = decode_name(device, adv_data)
    timestamp = human_time()
    rssi = getattr(device, "rssi", -999)
    manufacturer_data = getattr(adv_data, "manufacturer_data", {})
    details = f"{adv_data}" if args.details else ""
    manuf_str = prettify_manufacturer(manufacturer_data)
    record = {
        "timestamp": timestamp,
        "address": address,
        "name": name,
        "rssi": rssi,
        "manufacturer_data": manuf_str,
        "details": details,
    }

    # Filtering logic
    if args.mac and not fuzzy_match(address, args.mac):
        return
    if args.name and not fuzzy_match(name, args.name):
        return
    if args.min_rssi is not None and rssi < args.min_rssi:
        return
    if args.unique and address in address_seen and not args.repeat:
        return

    # Logging
    if args.unique and not args.repeat:
        address_seen.add(address)
    found_devices.append(record)

    # Text log line
    if args.verbose or args.details or manuf_str:
        line = f"[{timestamp}] {cstr(address, Colors.OKBLUE)} ▼ {cstr(name, Colors.BOLD)} RSSI:{rssi:>4} {cstr(manuf_str, Colors.OKCYAN)}"
        if details:
            line += f"
     Details: {details}"
    else:
        line = f"[{timestamp}] {address} {name} RSSI:{rssi}"

    print(line)
    raw_log_lines.append(line)

def demo_log():
    print("Sample device log output:")
    print(" " + "-"*70)
    print("[2024-04-13 21:27:32] 60:AB:32:EF:EA:41 ▼ SensorTag V12        RSSI:-41 0x1234: AB12CDEF...(22 bytes)")
    print(" " + "-"*70)

async def scan_ble(args):
    """Run BLE scan loop using bleak."""
    global found_devices, address_seen, raw_log_lines
    found_devices.clear()
    raw_log_lines.clear()
    address_seen.clear()
    seen_count = 0

    def detection_callback(device, adv_data):
        nonlocal seen_count
        log_and_print_device(device, adv_data, args)
        seen_count += 1

    print(cstr(f"
[*] BLE Sniffer: scanning {args.duration}s ...", Colors.OKGREEN))
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    try:
        await asyncio.sleep(args.duration)
    except KeyboardInterrupt:
        print(cstr("
Scan stopped by user.", Colors.WARNING))
    await scanner.stop()
    print(cstr(f"
[*] Scan complete. {len(found_devices)} device(s) logged.
", Colors.OKCYAN))


def sort_results(devices, sort_by="rssi"):
    if sort_by == "time":
        return sorted(devices, key=lambda d: d.get("timestamp", ""))
    return sorted(devices, key=lambda d: int(d.get("rssi", -999)), reverse=True)

def main():
    args = parse_args()
    if args.no_color:
        global USE_COLOR
        USE_COLOR = False

    if args.test:
        demo_log()
        exit(0)

    # Show search/filter info
    print(cstr("BLE Sniffer: Launching...", Colors.HEADER))
    print(cstr(f"Duration: {args.duration} sec | Filters: MAC={args.mac or '-'} NAME={args.name or '-'} MinRSSI={args.min_rssi or '-'}", Colors.OKCYAN))

    asyncio.run(scan_ble(args))

    if found_devices:
        # Sort results (rssi descending by default)
        sorted_devices = sort_results(found_devices, args.sort)
        if args.output:
            write_csv(sorted_devices, args.output)
            print(f"[*] Results written to {args.output}")
        if args.log:
            write_log(raw_log_lines, args.log)
            print(f"[*] Log lines written to {args.log}")

        print(cstr(f"
Summary:", Colors.UNDERLINE))
        for idx, d in enumerate(sorted_devices, 1):
            print(f"{idx:03d}. {d['address']:18} {d['name']:24}  RSSI: {d['rssi']:>4}  {d['manufacturer_data']}")

    else:
        print(cstr("No devices matched your filters.", Colors.WARNING))

    print(cstr("
Done. Happy sniffing! 🛰️
", Colors.OKGREEN))


if __name__ == "__main__":
    main()
```

---

# 🔥 **Features Demonstrated**

- **Dual Output:**  
  Print to terminal (with colors, details, and logs), CSV for spreadsheet, plain text for logs.
- **Filters:**  
  By MAC, partial MAC, name, RSSI threshold. Handy for focused research/devices in a crowd.
- **Advanced Logging:**  
  Every packet or unique devices only. Optionally show raw advertisement details for researchers.
- **Sorting:**  
  Sort results by RSSI or by first seen.
- **Coloured Terminal Output:**  
  Auto-detection (disable with `--no-color`). Each info type gets a different hue.
- **Easy Extensions:**  
  Add more fields & parsing for new protocols, extra columns in CSV, etc.
- **Demo Mode:**  
  `--test` flag prints example logs (no hardware needed).

---

# 💡 Usage Examples

Scan for everything, show detailed output, log to CSV:

```sh
python ble_sniffer.py --duration 45 --output scan.csv -v
```

Find only nearby devices called “Sensor,” RSSI > -70, and log all sightings:

```sh
python ble_sniffer.py --name Sensor --min-rssi -70 --repeat --output sensors.csv
```

No colors (for Windows), sort by time, log to plaintext:

```sh
python ble_sniffer.py --no-color --log ble_scan.txt --sort time
```

