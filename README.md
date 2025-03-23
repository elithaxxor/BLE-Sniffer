Note:
– This script uses the PyBluez library, so you’ll need to install it (e.g. pip install pybluez).
– Running Bluetooth scans might require administrator privileges on your system.
– The vendor lookup here is very basic. For a production system, you may want to integrate with a dedicated MAC address lookup service or database.
------
Note: 
Overview
	•	VendorLookup Class:
Encapsulates the vendor mapping and lookup logic, making future updates or extensions easier without affecting other parts of the code.
	•	Bluetooth Scanning:
The script uses PyBluez to scan for nearby Bluetooth devices every 8 seconds and retrieves basic info such as MAC address and device name.
	•	Extra Info Retrieval:
For each discovered device, the script concurrently retrieves extra details by calling bluetoothctl info <MAC> using a ThreadPoolExecutor.
	•	Database Logging:
All device data (timestamp, MAC, name, vendor, extra info) is saved in a SQLite database named bluetooth_devices.db.
	•	Threading:
The scanning loop is run on a separate daemon thread, and concurrent threads are used for extra info retrieval, optimizing overall performance.
---
This complete build should serve as a robust starting point for scanning and logging Bluetooth device data with enhanced maintainability and performance.
