$LogFile = "bluetooth_scan.log"

function Log {
    param ($Level, $Message)
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}

function Info {
    param ($Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}

function Success {
    param ($Message)
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}

function ErrorMsg {
    param ($Message)
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}

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

# Entry point
Info "Starting Bluetooth scan..."
Scan-Bluetooth
Success "Scan complete. Log saved to $LogFile"
