$LogFile = "bluetooth_scan.log"

# Logging function
function Log {
    param ($Level, $Message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}

# Info message function
function Info {
    param ($Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}

# Success message function
function Success {
    param ($Message)
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}

# Error message function
function ErrorMsg {
    param ($Message)
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}

# Modified Scan-Bluetooth function
function Scan-Bluetooth {
    try {
        Info "Scanning Bluetooth devices..."
        $devices = Get-PnpDevice -Class Bluetooth -Status OK

        if ($devices.Count -eq 0) {
            ErrorMsg "No active Bluetooth devices found."
        } else {
            foreach ($device in $devices) {
                # Gather additional properties with fallbacks
                $name = $device.FriendlyName
                $id = $device.InstanceId
                $manufacturer = if ($device.Manufacturer) { $device.Manufacturer } else { "N/A" }
                $hardwareID = if ($device.HardwareID) { $device.HardwareID -join ", " } else { "N/A" }
                $status = $device.Status
                $description = if ($device.Description) { $device.Description } else { "N/A" }

                # Create a detailed log message
                $logMessage = "Found: $name | ID: $id | Manufacturer: $manufacturer | HardwareID: $hardwareID | Status: $status | Description: $description"
                Success $logMessage
            }
        }
    } catch {
        ErrorMsg "Error scanning Bluetooth devices: $_"
    }
}

# Execute the scan
Scan-Bluetooth
