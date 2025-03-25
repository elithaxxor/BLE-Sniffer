Sure! Here’s the content formatted for a `README.md` file:

```markdown
# BLE-Sniffer

Welcome to the BLE-Sniffer repository! This repository contains scripts for scanning and logging Bluetooth Low Energy (BLE) devices. The scripts are designed to detect, identify, and log information about nearby BLE devices.

## Overview

### Purpose

The primary purpose of this repository is to provide tools for scanning and logging BLE devices. These tools can be used for various applications, such as network security monitoring, device tracking, and research.

### Features

- **Bluetooth Device Scanning**: Detects and logs nearby Bluetooth devices.
- **Vendor Identification**: Identifies the manufacturer of each device based on MAC address prefixes.
- **Additional Information Retrieval**: Uses commands like `bluetoothctl` to gather extra details about devices.
- **Database Logging**: Stores detailed information about each discovered device in an SQLite database.
- **Log File Management**: Manages log files, keeping only the most recent logs and deleting older ones automatically.
- **Concurrency**: Utilizes threading to perform scans and fetch extra device information concurrently.
- **Graceful Shutdown**: Can be terminated gracefully using a hotkey.

## Repository Structure

```
standalone/
└── scanners/
    ├── logs/                  # Directory for log files
    ├── sniff_my_ble.py        # Python script for scanning BLE devices
    ├── scan_bluetooth.ps1     # PowerShell script for Windows Bluetooth scanning
    └── bluetooth_devices.db   # SQLite database file
```

## Scripts

### Python Script: `sniff_my_ble.py`

This script scans for nearby Bluetooth devices, retrieves additional information, and logs the data into an SQLite database.

#### Key Features:

- **Bluetooth Scanning**: Uses the `bluetooth` module to scan for devices.
- **Vendor Identification**: Identifies the manufacturer based on MAC address prefixes.
- **Additional Info**: Retrieves extra information using the `bluetoothctl` command.
- **Database Logging**: Logs detailed information in a SQLite database.
- **Log Management**: Creates a folder for logs and keeps only the 3 most recent log files.
- **Concurrency**: Uses threading for concurrent data fetching.
- **Graceful Shutdown**: Can be terminated using a hotkey (`cmd+c` on macOS).

### PowerShell Script: `scan_bluetooth.ps1`

This script is designed for Windows and scans for Bluetooth devices, logs the results, and handles errors. It provides user-friendly output with different message levels and colors.

#### Key Features:

- **Bluetooth Scanning**: Uses the `Get-PnpDevice` cmdlet for scanning.
- **Logging**: Logs results and errors with timestamps.
- **User Feedback**: Provides colored messages for info, success, and error.
- **Menu for Scan Intervals**: Allows users to select scan intervals or continuous scanning.

### Flask Web Application: `app.py`

This script sets up a Flask web application to display Bluetooth device logs stored in an SQLite database.

#### Key Features:

- **Web Framework**: Uses Flask to create a web interface.
- **Database Interaction**: Connects to a SQLite database to retrieve Bluetooth device logs.
- **Templates**: Renders an HTML template to display the data.

#### Detailed Breakdown:

1. **Imports**: 
   - `Flask` and `render_template` from the Flask package for web application functionality.
   - `sqlite3` for interacting with the SQLite database.

2. **Flask Application Setup**: 
   - Initializes a Flask application instance with `app = Flask(__name__)`.

3. **Database Interaction**: 
   - **`get_devices()`**: A function to retrieve all device logs from the SQLite database.
     - Connects to the `bluetooth_devices.db` database.
     - Sets the row factory to `sqlite3.Row` to access columns by name.
     - Executes a query to select all records from the `devices` table, ordered by `id` in descending order.
     - Fetches all results and closes the database connection.
     - Returns the fetched device logs.

4. **Flask Route**: 
   - **`@app.route("/")`**: Defines the root route of the web application.
     - Calls the `get_devices()` function to get device logs.
     - Renders the `index.html` template, passing the device logs to the template as a context variable named `devices`.

5. **Main Block**: 
   - Runs the Flask application in debug mode on `localhost:5000` if the script is executed directly.

#### Usage:

- **Running the Application**:
  1. Ensure you have Flask installed:
     ```bash
     pip install flask
     ```
  2. Execute the script:
     ```bash
     python app.py
     ```
  3. Open a web browser and navigate to `http://localhost:5000` to view the logged Bluetooth devices.

#### Example `index.html` Template:

The `index.html` template would typically display the device logs in a user-friendly format. Here’s an example of what it might look like:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bluetooth Device Logs</title>
</head>
<body>
    <h1>Bluetooth Device Logs</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Timestamp</th>
            <th>MAC Address</th>
            <th>Device Name</th>
            <th>Vendor</th>
            <th>Extra Info</th>
        </tr>
        {% for device in devices %}
        <tr>
            <td>{{ device.id }}</td>
            <td>{{ device.timestamp }}</td>
            <td>{{ device.mac_address }}</td>
            <td>{{ device.device_name }}</td>
            <td>{{ device.vendor }}</td>
            <td>{{ device.extra_info }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

## Log File Management

The scripts generate log files in the `logs` directory. Each log file is named with a timestamp to ensure uniqueness. The scripts keep only the 3 most recent log files and delete older ones automatically.

## Example Output

### Python Script

```plaintext
2025-03-24 17:45:10 - DEBUG - Starting Bluetooth scan...
2025-03-24 17:45:18 - DEBUG - Found 2 device(s).
2025-03-24 17:45:19 - DEBUG - Extra info for XX:XX:XX:XX:XX:XX: Device XX:XX:XX:XX:XX:XX
2025-03-24 17:45:19 - DEBUG - Logged device XX:XX:XX:XX:XX:XX (Device Name) with vendor Apple, Inc.
2025-03-24 17:45:19 - DEBUG - Extra info for YY:YY:YY:YY:YY:YY: Device YY:YY:YY:YY:YY:YY
2025-03-24 17:45:19 - DEBUG - Logged device YY:YY:YY:YY:YY:YY (Another Device) with vendor Samsung Electronics Co., Ltd.
2025-03-24 17:45:19 - DEBUG - Sleeping for 5 minutes before next scan...
```

### PowerShell Script

```plaintext
[!] Starting Bluetooth scan...
[!] Scanning Bluetooth devices using Get-PnpDevice...
[+] Found: Bluetooth Device (ID: 12345) - Manufacturer: Example Inc. - Type: Computer - RSSI: RSSI information not available in PowerShell
[+] Scan complete. Log saved to bluetooth_scan.log
```

## Error Handling

Both scripts include error handling to catch and log any issues encountered during the Bluetooth scan process and while retrieving extra device information.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests. Contributions are welcome!

---

This repository aims to provide robust tools for scanning and logging Bluetooth device data efficiently and maintainably.
```

This `README.md` provides a comprehensive overview of the `BLE-Sniffer` repository, including details about its purpose, features, scripts, usage, and example outputs.
