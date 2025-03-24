
```markdown
# Bluetooth Scanner Script

This repository contains a PowerShell script `scan_bluetooth.ps1` designed to scan for active Bluetooth devices on a Windows machine. The script logs the results, handles errors, and provides user feedback via the console.

## Overview

The `scan_bluetooth.ps1` script performs the following tasks:
- Scans for active Bluetooth devices using the `Get-PnpDevice` cmdlet.
- Logs the scan results and any errors to a log file.
- Provides console output with different levels of messages (info, success, error).
- Allows the user to choose scan intervals or perform continuous scanning via a menu.

## Features

- **Logging**: All scan results and messages are logged with timestamps.
- **User Feedback**: Messages are displayed in the console with different colors to indicate their type (info, success, error).
- **Menu for Scan Intervals**: Users can select scan intervals of 30 seconds, 3 minutes, 10 minutes, or continuous scanning.
- **Error Handling**: The script includes error handling to catch and log any issues encountered during the Bluetooth scan process.

## Script Details

### Functions

#### `Log`
Logs messages to the log file with a timestamp.

```powershell
function Log {
    param ($Level, $Message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}
```

#### `Info`
Displays and logs informational messages.

```powershell
function Info {
    param ($Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}
```

#### `Success`
Displays and logs success messages.

```powershell
function Success {
    param ($Message)
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}
```

#### `ErrorMsg`
Displays and logs error messages.

```powershell
function ErrorMsg {
    param ($Message)
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}
```

#### `Scan-Bluetooth`
Performs the Bluetooth scan and logs the results. If no Bluetooth devices are found, it logs an error message.

```powershell
function Scan-Bluetooth {
    try {
        Info "Scanning Bluetooth devices using Get-PnpDevice..."
        $devices = Get-PnpDevice -Class Bluetooth -Status OK

        if ($devices.Count -eq 0) {
            ErrorMsg "No active Bluetooth devices found."
        } else {
            foreach ($device in $devices) {
                $name = $device.FriendlyName
                $id = $device.InstanceId
                Success "Found: $name ($id)"
            }
        }
    } catch {
        ErrorMsg "Error scanning Bluetooth devices: $_"
    }
}
```

#### `Show-Menu`
Displays menu options for the user to choose the scan interval.

```powershell
function Show-Menu {
    Write-Host "Choose scan interval:"
    Write-Host "1. Scan every 30 seconds"
    Write-Host "2. Scan every 3 minutes"
    Write-Host "3. Scan every 10 minutes"
    Write-Host "4. Continuous scan"
    Write-Host "5. Exit"
}
```

#### `Get-Interval`
Maps the user’s choice to the corresponding interval in seconds.

```powershell
function Get-Interval {
    param ($choice)
    switch ($choice) {
        1 { return 30 }
        2 { return 180 }
        3 { return 600 }
        4 { return 0 }
        default { return -1 }
    }
}
```

### Main Script Logic

The main script logic includes a loop that continuously displays the menu, processes the user's choice, and sets up the scan interval accordingly.

```powershell
# Main loop
while ($true) {
    Show-Menu
    $choice = Read-Host "Enter your choice (1-5)"
    $interval = Get-Interval $choice

    if ($interval -eq -1) {
        Write-Host "Invalid choice. Please select a valid option." -ForegroundColor Red
        continue
    } elseif ($interval -eq 0) {
        Info "Starting continuous Bluetooth scan..."
        while ($true) {
            Scan-Bluetooth
            Start-Sleep -Seconds 30
        }
    } elseif ($choice -eq 5) {
        Write-Host "Exiting..."
        break
    } else {
        Info "Starting Bluetooth scan every $interval seconds..."
        while ($true) {
            Scan-Bluetooth
            Start-Sleep -Seconds $interval
        }
    }
    break
}

Success "Script terminated. Log saved to $LogFile"
```

## Usage

### Prerequisites

- Windows operating system with PowerShell installed.
- Bluetooth functionality enabled on the machine.

### Running the Script

1. Open PowerShell with administrative privileges.
2. Navigate to the directory containing the `scan_bluetooth.ps1` script.
3. Execute the script by running the following command:
   ```powershell
   .\scan_bluetooth.ps1
   ```

### Log File

The script generates a log file named `bluetooth_scan.log` in the same directory as the script. The log file contains timestamps and details of the Bluetooth scan results.

## Example Output

```plaintext
[!] Starting Bluetooth scan...
[!] Scanning Bluetooth devices using Get-PnpDevice...
[+] Found: Bluetooth Device (ID: 12345)
[+] Scan complete. Log saved to bluetooth_scan.log
```

## Error Handling

The script includes error handling to catch and log any issues encountered during the Bluetooth scan process.

copyleft my mistakes are yours 
```

