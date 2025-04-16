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
        print(cstr("Scan stopped by user.", Colors.WARNING))
    await scanner.stop()
    print(cstr(f"[*] Scan complete. {len(found_devices)} device(s) logged.", Colors.OKCYAN))


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

        print(cstr(f"Summary:", Colors.UNDERLINE))
        for idx, d in enumerate(sorted_devices, 1):
            print(f"{idx:03d}. {d['address']:18} {d['name']:24}  RSSI: {d['rssi']:>4}  {d['manufacturer_data']}")

    else:
        print(cstr("No devices matched your filters.", Colors.WARNING))

    print(cstr("Done. Happy sniffing! 🛰️", Colors.OKGREEN))


if __name__ == "__main__":
    main()
