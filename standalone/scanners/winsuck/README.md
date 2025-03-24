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
