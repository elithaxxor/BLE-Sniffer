Here's a revamped version of your GitHub README.md that incorporates graphics, enhances readability, and adds a more engaging layout:

```markdown
# 📡 Bluetooth Sniffer Script

![Bluetooth Sniffer](https://example.com/bluetooth_sniffer_image.png) <!-- Replace with actual image link -->

This repository contains a Python script called `sniff_my_ble.py`, designed to scan for active Bluetooth devices, retrieve additional information, and log the data into an SQLite database. The script runs continuously and supports graceful termination via a hotkey.

---

## 📚 Overview

### ✨ Features

- **Bluetooth Device Scanning**: Efficiently scans nearby Bluetooth devices using the `bluetooth` module.
- **Vendor Identification**: Identifies manufacturers based on MAC address prefixes (OUIs).
- **Additional Device Information**: Retrieves extra information with the `bluetoothctl` command.
- **Database Logging**: Logs detailed info about discovered devices in an SQLite database.
- **Log File Management**: Maintains only the 3 most recent log files.
- **Concurrency**: Utilizes threading for simultaneous scanning and data fetching.
- **Graceful Shutdown**: Easily terminated using a hotkey (`cmd+c` on macOS).

---

## 🛠️ Script Details

### 🗂️ Directory Structure

```plaintext
standalone/
└── scanners/
    ├── logs/                  # Directory for log files
    ├── sniff_my_ble.py        # Bluetooth sniffer script
    └── bluetooth_devices.db   # SQLite database file
```

### 🗄️ SQLite Database Setup

The script initializes an SQLite database (`bluetooth_devices.db`) and creates a `devices` table to store scanned device information.

### 📜 Logging Setup

The script generates a `logs` directory for log files, naming each file with a timestamp for uniqueness and retaining only the 3 most recent logs.

### 🔍 Vendor Lookup Class

The `VendorLookup` class maps MAC address prefixes to vendor names, providing a lookup method based on MAC addresses.

### 📖 Functions Overview

- **`setup_logging`**
  
  Sets up logging configuration. Here's how it looks:
  
  ```python
  def setup_logging():
      ...
  ```

- **`get_extra_info`**

  Gathers extra device information:
  
  ```python
  def get_extra_info(mac):
      ...
  ```

- **`scan_devices`**

  Performs Bluetooth scanning and logs the details:
  
  ```python
  def scan_devices():
      ...
  ```

- **`scanning_loop`**

  Runs scans at 5-minute intervals:
  
  ```python
  def scanning_loop():
      ...
  ```

- **`quit_program`**

  Gracefully terminates the program:
  
  ```python
  def quit_program():
      ...
  ```

### 🚀 Main Execution Block

The main block sets up the quitting hotkey, starts the scanning loop, and ensures the thread remains active:

```python
if __name__ == "__main__":
    ...
```

---

## 🔧 Usage

### 🗒️ Prerequisites

- Python 3.x
- Bluetooth functionality enabled on your machine
- Required Python packages:
  
  ```bash
  pip install pybluez keyboard
  ```

### ▶️ Running the Script

1. Open a terminal with appropriate privileges.
2. Navigate to the directory containing `sniff_my_ble.py`.
3. Execute the script:

   ```bash
   python sniff_my_ble.py
   ```

### 📁 Log File Insights

Log files are stored in the `logs` directory, each named with a timestamp. The contents include timestamps and detailed scan results.

### 💻 Example Output

```plaintext
2025-03-24 17:45:10 - DEBUG - Starting Bluetooth scan...
2025-03-24 17:45:18 - DEBUG - Found 2 device(s).
...
```

### ⚠️ Error Handling

The script includes comprehensive error handling to log any issues encountered during the Bluetooth scanning process and while retrieving additional information.

---

This repository aims to provide a robust and maintainable script for efficiently scanning and logging Bluetooth device data. Explore and enhance your Bluetooth management experience! 🚀

![Bluetooth Diagram](https://example.com/bluetooth_diagram.png) <!-- Replace with actual diagram link -->
```

### Key Changes Made:
1. **Added Graphics**: Placeholder links for images and diagrams to enhance visual appeal.
2. **Emojis**: Used emojis to make headings and features more engaging.
3. **Clearer Structure**: Sections are visually and contextually separated for easy navigation.
4. **Sample Code Sections**: Highlighted with syntax for better readability.
5. **Encouraging Language**: A more motivational tone to invite users to explore the repository.

Feel free to replace image links with actual graphics related to your project!
