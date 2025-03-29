
```markdown
# 🔍 Bluetooth Scanner Script

Welcome to the **Bluetooth Scanner Script** repository! 🎉 This is your one-stop solution for scanning active Bluetooth devices on Linux, macOS, and Windows. It’s like having a Bluetooth detector in your pocket! 📱

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
    ```

---

## 🌐 PHP Backend Server

To store and retrieve scanned Bluetooth device data, you can set up a PHP backend server.

### ✅ Prerequisites

- A web server with PHP support (e.g., Apache, Nginx).
- SQLite installed on your server.

### 🛠️ Setup

1. **Create the SQLite Database:**

   ```bash
   sqlite3 bluetooth_devices.db <<EOF
   CREATE TABLE devices (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       timestamp TEXT,
       mac_address TEXT,
       device_name TEXT,
       vendor TEXT,
       extra_info TEXT
   );
   EOF
   ```

2. **Create the PHP Backend Script (`backend.php`):**

   ```php
   <?php
   header("Content-Type: application/json");

   $method = $_SERVER['REQUEST_METHOD'];
   $db_file = dirname(__FILE__) . "/bluetooth_devices.db";

   try {
       $db = new PDO("sqlite:$db_file");
       $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
   } catch (Exception $e) {
       echo json_encode(["error" => $e->getMessage()]);
       exit;
   }

   switch ($method) {
       case 'GET':
           getDevices($db);
           break;
       case 'POST':
           addDevice($db);
           break;
       default:
           echo json_encode(["error" => "Invalid request method"]);
           break;
   }

   function getDevices($db) {
       $query = "SELECT * FROM devices ORDER BY timestamp DESC";
       $stmt = $db->prepare($query);
       $stmt->execute();
       $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
       echo json_encode($result);
   }

   function addDevice($db) {
       $data = json_decode(file_get_contents('php://input'), true);
       if (!isset($data['mac_address']) || !isset($data['device_name']) || !isset($data['vendor'])) {
           echo json_encode(["error" => "Missing required fields"]);
           return;
       }

       $query = "INSERT INTO devices (timestamp, mac_address, device_name, vendor, extra_info)
                 VALUES (:timestamp, :mac_address, :device_name, :vendor, :extra_info)";
       $stmt = $db->prepare($query);
       $stmt->execute([
           ':timestamp' => date('Y-m-d\TH:i:s'),
           ':mac_address' => $data['mac_address'],
           ':device_name' => $data['device_name'],
           ':vendor' => $data['vendor'],
           ':extra_info' => $data['extra_info'] ?? ''
       ]);

       echo json_encode(["success" => "Device added successfully"]);
   }
   ?>
   ```

3. **Create the HTML File (`index.html`) to Display Data:**

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Bluetooth Device Scanner</title>
       <link rel="stylesheet" href="styles.css">
   </head>
   <body>
       <h1>Bluetooth Device Scanner</h1>
       <div id="device-list">
           <h2>Scanned Devices</h2>
           <table>
               <thead>
                   <tr>
                       <th>Timestamp</th>
                       <th>MAC Address</th>
                       <th>Device Name</th>
                       <th>Vendor</th>
                       <th>Extra Info</th>
                   </tr>
               </thead>
               <tbody id="devices">
                   <!-- Data will be populated here -->
               </tbody>
           </table>
       </div>
       <script src="script.ts"></script>
   </body>
   </html>
   ```

4. **Create the TypeScript File (`script.ts`) to Fetch and Display Data:**

   ```typescript
   interface Device {
       timestamp: string;
       mac_address: string;
       device_name: string;
       vendor: string;
       extra_info: string;
   }

   document.addEventListener("DOMContentLoaded", () => {
       fetchDevices();
   });

   function fetchDevices(): void {
       fetch("backend.php")
           .then(response => response.json())
           .then((data: Device[]) => {
               const devicesTable = document.getElementById("devices");
               if (devicesTable) {
                   devicesTable.innerHTML = "";
                   data.forEach(device => {
                       const row = document.createElement("tr");
                       row.innerHTML = `
                           <td>${device.timestamp}</td>
                           <td>${device.mac_address}</td>
                           <td>${device.device_name}</td>
                           <td>${device.vendor}</td>
                           <td>${device.extra_info}</td>
                       `;
                       devicesTable.appendChild(row);
                   });
               }
           })
           .catch(error => console.error("Error fetching devices:", error));
   }
   ```

5. **Create Optional Stylesheet (`styles.css`):**

   ```css
   body {
       font-family: Arial, sans-serif;
       margin: 20px;
   }

   h1 {
       text-align: center;
   }

   #device-list {
       margin-top: 20px;
   }

   table {
       width: 100%;
       border-collapse: collapse;
   }

   th, td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: left;
   }

   th {
       background-color: #f2f2f2;
   }
   ```

### 🏃‍♂️ How to Run the Server

1. Place `backend.php`, `index.html`, `script.ts`, and `styles.css` in your web server’s root directory.
2. Ensure the SQLite database file `bluetooth_devices.db` is in the same directory as `backend.php`.
3. Start your web server and navigate to `index.html` in your browser to view the scanned Bluetooth devices.

---

Now you have a fully functional Bluetooth scanner script with a PHP backend server and a front-end interface to display the data!
```
