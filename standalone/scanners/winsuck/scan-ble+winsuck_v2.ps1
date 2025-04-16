<#
.SYNOPSIS
Scans for active Bluetooth devices and logs the results.

.DESCRIPTION
This script scans for active Bluetooth devices using PowerShell's `Get-PnpDevice` cmdlet.
It logs the results to both the console and a file, includes robust error handling, and offers modular and configurable options.

.PARAMETER LogFilePath
Specifies the path for the log file. Defaults to an environment variable or "bluetooth_scan.log".

.EXAMPLE
.\scan_bluetooth.ps1 -LogFilePath "C:\Logs\scan.log"

.NOTES
Ensure that the script is run on a Windows system with PowerShell and the `Get-PnpDevice` cmdlet available.
#>

param (
    [string]$LogFilePath = $env:LOG_FILE_PATH -or "bluetooth_scan.log"
)

# Set the log file path
$LogFile = $LogFilePath

# Function to log messages to a file with a timestamp and level
function Log {
    param (
        [ValidateNotNullOrEmpty()]
        [string]$Level,

        [ValidateNotNullOrEmpty()]
        [string]$Message
    )
    "$((Get-Date).ToString('yyyy-MM-dd HH:mm:ss')) - [$Level] $Message" | Out-File -Append $LogFile
}

# Function to log informational messages
function Info {
    param ([string]$Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
    Log "INFO" $Message
}

# Function to log success messages
function Success {
    param ([string]$Message)
    Write-Host "[+] $Message" -ForegroundColor Green
    Log "OK" $Message
}

# Function to log error messages
function ErrorMsg {
    param ([string]$Message)
    Write-Host "[-] $Message" -ForegroundColor Red
    Log "ERROR" $Message
}

# Function to retrieve a list of active Bluetooth devices
function Get-BluetoothDevices {
    <#
    .SYNOPSIS
    Retrieves a list of active Bluetooth devices.

    .DESCRIPTION
    This function uses `Get-PnpDevice` to retrieve Bluetooth devices with a status of 'OK'.
    If an error occurs, it logs the error and returns an empty array.

    .OUTPUTS
    Array of devices or an empty array in case of failure.
    #>
    try {
        if (-not (Get-Command Get-PnpDevice -ErrorAction SilentlyContinue)) {
            ErrorMsg "Get-PnpDevice cmdlet is not available. Please ensure the required module is installed."
            return @()
        }
        Get-PnpDevice -Class Bluetooth -Status OK
    } catch {
        ErrorMsg "Failed to retrieve Bluetooth devices: $_.Exception.Message"
        return @()
    }
}

# Function to scan for active Bluetooth devices and log the results
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
                # Safeguard against missing properties
                $name = $device.FriendlyName -or "Unknown"
                $id = $device.InstanceId -or "Unknown"
                $manufacturer = $device.Manufacturer -or "Unknown"
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
