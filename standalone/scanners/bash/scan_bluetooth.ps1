<#
.SYNOPSIS
Scans for active Bluetooth devices and logs the results.

.DESCRIPTION
This script scans for active Bluetooth devices using PowerShell's `Get-PnpDevice` cmdlet. It logs the results, provides both console and file outputs, and includes improved error handling and modularity.
#>

# Log file path (can be configured through an environment variable)
$LogFile = $env:LOG_FILE_PATH -or "bluetooth_scan.log"

function Log {
    param (
        [ValidateNotNullOrEmpty()]
        [string]$Level,

        [ValidateNotNullOrEmpty()]
        [string]$Message
    )
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}

function Info {
    param ([string]$Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}

function Success {
    param ([string]$Message)
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}

function ErrorMsg {
    param ([string]$Message)
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}

function Get-BluetoothDevices {
    <#
    .SYNOPSIS
    Retrieves a list of active Bluetooth devices.

    .DESCRIPTION
    This function uses `Get-PnpDevice` to retrieve Bluetooth devices with a status of 'OK'. If an error occurs, it logs the error and returns an empty array.

    .OUTPUTS
    Array of devices or an empty array in case of failure.
    #>
    try {
        Get-PnpDevice -Class Bluetooth -Status OK
    } catch {
        ErrorMsg "Failed to retrieve Bluetooth devices: $_.Exception.Message"
        return @()
    }
}

function Scan-Bluetooth {
    <#
    .SYNOPSIS
    Scans for active Bluetooth devices and logs the results.

    .DESCRIPTION
    This function retrieves active Bluetooth devices, logs the results, and provides feedback to the console.
    #>
    try {
        Info "Scanning Bluetooth devices using Get-PnpDevice..."
        $devices = Get-BluetoothDevices

        if ($devices.Count -eq 0) {
            ErrorMsg "No active Bluetooth devices found."
        } else {
            foreach ($device in $devices) {
                $name = $device.FriendlyName
                $id = $device.InstanceId
                $manufacturer = $device.Manufacturer
                Success "Found: $name ($id) - Manufacturer: $manufacturer"
            }
        }
    } catch {
        ErrorMsg "Error scanning Bluetooth devices: $_.Exception.Message"
    } finally {
        Info "Finished scanning for Bluetooth devices."
    }
}

# Entry Point
Info "Starting Bluetooth scan..."
Scan-Bluetooth
Success "Scan complete. Log saved to $LogFile"
