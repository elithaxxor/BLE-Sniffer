# Bluetooth Scanner Script

$LogFile = "bluetooth_scan.log"

# MAC address prefix to manufacturer mapping
$MAC_PREFIXES = @{
    "F0:99:B6" = "Apple, Inc."
    "28:FF:3C" = "Apple, Inc."
    "D0:D0:03" = "Samsung Electronics Co., Ltd."
    "08:FD:0E" = "Samsung Electronics Co., Ltd."
    "CC:05:77" = "Huawei Technologies Co., Ltd."
    "30:FB:B8" = "Huawei Technologies Co., Ltd."
    "00:14:22" = "Dell Inc."
    "04:0E:3C" = "HP Inc."
    "00:68:EB" = "HP Inc."
    "10:C5:95" = "Lenovo"
    "98:93:CC" = "LG Electronics Inc."
    "F0:BF:97" = "Sony Corporation"
    "98:E8:FA" = "Nintendo Co., Ltd."
    "80:C5:E6" = "Microsoft Corporation"
    "58:CB:52" = "Google, Inc."
    "68:DB:F5" = "Amazon Technologies Inc."
    "A4:45:19" = "Xiaomi Communications Co., Ltd."
    "A0:91:A2" = "OnePlus Electronics (Shenzhen) Co., Ltd."
    "18:02:AE" = "Vivo Mobile Communication Co., Ltd."
    "D8:1E:DD" = "Guangdong Oppo Mobile Telecommunications Corp., Ltd."
    "24:46:C8" = "Motorola Mobility LLC (Lenovo)"
    "BC:C3:42" = "Panasonic Communications Co., Ltd."
    "1C:5A:6B" = "Philips Electronics Nederland BV"
    "00:01:24" = "Acer Incorporated"
    "04:92:26" = "ASUSTek COMPUTER INC."
}

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

function Identify-Manufacturer {
    param ($MAC)
    $prefix = $MAC.Substring(0, 8)
    return $MAC_PREFIXES[$prefix] -or "Unknown"
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
                $manufacturer = Identify-Manufacturer $id
                Success "Found: $name ($id) - Manufacturer: $manufacturer"
            }
        }
    } catch {
        ErrorMsg "Error scanning Bluetooth devices: $_"
    }
}

function Show-Menu {
    Write-Host "Choose scan interval:"
    Write-Host "1. Scan every 30 seconds"
    Write-Host "2. Scan every 3 minutes"
    Write-Host "3. Scan every 10 minutes"
    Write-Host "4. Continuous scan"
    Write-Host "5. Exit"
}

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
