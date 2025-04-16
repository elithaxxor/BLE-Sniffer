""" This Python script acts as a BLE (Bluetooth Low Energy) Standalone Sniffer that scans for BLE advertisement packets """ 

import asyncio
from bleak import BleakScanner
import argparse
from utils import format_mac, human_time, write_csv, truncate_hex

# Global list to store found devices during the scan
found_devices = []

# Function to parse command-line arguments
def parse_args():
    """
    Parses command-line arguments for the BLE sniffer script.

    Available arguments:
    - --duration: Duration of the BLE scan (in seconds).
    - --output: Filename to save results in CSV format.
    - --verbose: Enables detailed output, including manufacturer data.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="BLE Standalone Sniffer -- Scans BLE Advertisement Packets."
    )
    parser.add_argument("--duration", type=int, default=30, help="Duration to scan (seconds). Default: 30")
    parser.add_argument("--output", type=str, help="CSV file to save scan results.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output (shows manufacturer data, etc.)")
    return parser.parse_args()

# Function to handle each discovered BLE device
def handle_device(device, adv_data, verbose=False):
    """
    Callback function to process and log information about a discovered BLE device.

    Args:
        device (bleak.backends.device.BLEDevice): The discovered BLE device.
        adv_data (bleak.backends.scanner.AdvertisementData): Advertisement data from the BLE device.
        verbose (bool): Whether to include detailed output, e.g., manufacturer data.
    """
    # Format the device's address and gather relevant information
    address = format_mac(device.address)
    name = device.name or adv_data.local_name or "<unknown>"
    timestamp = human_time()
    rssi = device.rssi
    manuf = adv_data.manufacturer_data

    # Format manufacturer data (if available) into a readable string
    manuf_str = "; ".join(
        [f"0x{k:04X}: {truncate_hex(bytes(v))}" for k, v in manuf.items()]
    ) if manuf else ""

    # Generate output string for the device
    output = f"[{timestamp}] {address} | {name:20} | RSSI: {rssi:>4}"
    if verbose and manuf:
        output += f" | Manuf: {manuf_str}"

    # Print the device information to the console
    print(output)

    # Append the device details to the global list for later use
    found_devices.append({
        "timestamp": timestamp,
        "address": address,
        "name": name,
        "rssi": rssi,
        "manufacturer_data": manuf_str,
    })

# Asynchronous function to scan BLE devices
async def scan_ble(duration=30, verbose=False):
    """
    Performs a BLE scan for a specified duration and processes discovered devices.

    Args:
        duration (int): Duration of the scan in seconds.
        verbose (bool): Whether to include detailed output, e.g., manufacturer data.
    """
    global found_devices
    found_addresses = set()  # Set to track already-seen device addresses

    # Inner callback function to handle each detected BLE device
    def detection_callback(device, adv_data):
        # Only process the device if it hasn't been seen before
        if device.address not in found_addresses:
            found_addresses.add(device.address)
            handle_device(device, adv_data, verbose)

    print(f"[*] Scanning BLE devices for {duration} seconds...")
    scanner = BleakScanner(detection_callback)  # Initialize the BLE scanner
    await scanner.start()  # Start scanning for BLE devices
    await asyncio.sleep(duration)  # Wait for the specified scan duration
    await scanner.stop()  # Stop scanning
    print(f"[*] Scanning complete. {len(found_addresses)} unique devices found.")

# Main function to execute the BLE sniffer
def main():
    """
    Main function to orchestrate the BLE scanning process, handle arguments,
    and optionally save results to a CSV file.
    """
    args = parse_args()  # Parse command-line arguments
    asyncio.run(scan_ble(args.duration, verbose=args.verbose))  # Run the BLE scan

    # Save results to a CSV file if the --output argument is provided
    if args.output:
        print(f"[*] Writing results to {args.output} ...")
        write_csv(found_devices, args.output)  # Save found devices to a CSV file
        print("[*] Done.")

# Entry point for the script
if __name__ == "__main__":
    main()
