$LogFile = "bluetooth_scan.log"

function Log {
    param ($Level, $Message)
    # Log message with timestamp
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}

function Info {
    param ($Message)
    # Display and log informational message
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}

function Success {
    param ($Message)
    # Display and log success message
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}

function ErrorMsg {
    param ($Message)
    # Display and log error message
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}

function Scan-Bluetooth {
    try {
        Info "Scanning Bluetooth devices using Get-PnpDevice..."
        # Retrieve active Bluetooth devices
        $devices = Get-PnpDevice -Class Bluetooth -Status OK

        if ($devices.Count -eq 0) {
            # No devices found
            ErrorMsg "No active Bluetooth devices found."
        } else {
            # Iterate over found devices and log each one
            foreach ($device in $devices) {
                $name = $device.FriendlyName
                $id = $device.InstanceId
                Success "Found: $name ($id)"
            }
        }
    } catch {
        # Log any errors encountered during the scan
        ErrorMsg "Error scanning Bluetooth devices: $_"
    }
}

function Show-Menu {
    # Display menu options to the user
    Write-Host "Choose scan interval:"
    Write-Host "1. Scan every 30 seconds"
    Write-Host "2. Scan every 3 minutes"
    Write-Host "3. Scan every 10 minutes"
    Write-Host "4. Continuous scan"
    Write-Host "5. Exit"
}

function Get-Interval {
    param ($choice)
    # Map user choice to corresponding interval in seconds
    switch ($choice) {
        1 { return 30 }
        2 { return 180 }
        3 { return 600 }
        4 { return 0 }
        default { return -1 }
    }
}

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
        # Continuous scan with 30-second interval
        while ($true) {
            Scan-Bluetooth
            Start-Sleep -Seconds 30
        }
    } elseif ($choice -eq 5) {
        # Exit the script
        Write-Host "Exiting..."
        break
    } else {
        Info "Starting Bluetooth scan every $interval seconds..."
        # Scan at specified interval
        while ($true) {
            Scan-Bluetooth
            Start-Sleep -Seconds $interval
        }
    }
    break
}

Success "Script terminated. Log saved to $LogFile"
