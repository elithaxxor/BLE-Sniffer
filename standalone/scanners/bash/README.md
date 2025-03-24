
```markdown
# Bluetooth Scanner Script

This repository contains scripts designed to scan for active Bluetooth devices on various operating systems (Linux, macOS, and Windows). The scripts log the results, handle errors, and provide user-friendly output.

## Overview

### `scan_bluetooth.sh`

The `scan_bluetooth.sh` script is designed to scan for active Bluetooth devices on Linux and macOS systems.

### Features

- **Logging**: Logs messages to a file named `bluetooth_scan.log` with timestamps.
- **User Feedback**: Provides feedback via the console using colored messages and symbols ([+], [-], [!]).
- **OS Detection**: Detects the operating system and runs the appropriate scan method.
- **Bluetooth Scanning**: Uses `bluetoothctl` on Linux and `system_profiler` on macOS to scan for Bluetooth devices.
- **Manufacturer Identification**: Identifies and categorizes Bluetooth devices based on MAC address prefixes using a predefined list.
- **Additional Device Details**: Retrieves additional details such as RSSI (signal strength) and device type on Linux.
- **Menu for Scan Intervals**: Allows users to choose scan intervals (30 seconds, 3 minutes, 10 minutes) or continuous scanning.

### Script Details

#### Functions

- **log**: Logs messages to `bluetooth_scan.log` with timestamps.
- **info**: Displays and logs informational messages.
- **success**: Displays and logs success messages.
- **error**: Displays and logs error messages.
- **check_dependencies**: Checks if required tools are available on the system.
- **identify_manufacturer**: Identifies the manufacturer based on the MAC address prefix.
- **scan_linux**: Scans for Bluetooth devices on Linux and retrieves additional details.
- **scan_macos**: Scans for Bluetooth devices on macOS.
- **show_menu**: Displays menu options for the user to choose the scan interval.
- **get_interval**: Maps the user’s choice to the corresponding interval in seconds.
- **scan_based_on_os**: Determines the OS and calls the appropriate scan function.
- **main**: Main function that handles the overall script logic and user input.

### Usage

#### Prerequisites

- Linux or macOS operating system.
- Bluetooth functionality enabled on the machine.

#### Running the Script

1. Open a terminal with appropriate privileges.
2. Navigate to the directory containing the `scan_bluetooth.sh` script.
3. Execute the script by running the following command:
   ```bash
   ./scan_bluetooth.sh
   ```

#### Log File

The script generates a log file named `bluetooth_scan.log` in the same directory as the script. The log file contains timestamps and details of the Bluetooth scan results.

#### Example Output

```plaintext
[!] Starting Bluetooth scan...
[+] Using bluetoothctl to scan for devices on Linux...
[+] Found: F0:99:B6:12:34:56 (Device Name) - Manufacturer: Apple, Inc. - RSSI: -40 - Type: phone
[+] Scan complete. Log saved to bluetooth_scan.log
```

## Additional Notes

- The script includes error handling to catch and log any issues encountered during the Bluetooth scan process.
- The vendor lookup is based on a predefined list of MAC address prefixes. For a production system, you may want to integrate with a dedicated MAC address lookup service or database.

## PowerShell Script (`scan_bluetooth.ps1`)

The repository also includes a PowerShell script for scanning Bluetooth devices on Windows machines. Refer to the [`standalone/scanners/winsuck/README.md`](standalone/scanners/winsuck/README.md) for details on the PowerShell script.

---

This repository aims to provide robust scripts for scanning and logging Bluetooth device data efficiently and maintainably.
```
