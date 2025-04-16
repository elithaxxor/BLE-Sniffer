#!/bin/bash

LOG_FILE="bluetooth_scan.log"

# Colors
GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
RESET="\033[0m"

log() {
    echo -e "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

info() {
    echo -e "${YELLOW}[!] $1${RESET}"
    log "[!] $1"
}

success() {
    echo -e "${GREEN}[+] $1${RESET}"
    log "[+] $1"
}

error() {
    echo -e "${RED}[-] $1${RESET}"
    log "[-] $1"
}

scan_linux() {
    success "Using bluetoothctl to scan for devices on Linux..."
    bluetoothctl power on &>/dev/null
    bluetoothctl scan on &>/dev/null &
    sleep 5
    bluetoothctl devices | while read -r line; do
        mac=$(echo "$line" | awk '{print $2}')
        name=$(echo "$line" | cut -d ' ' -f 3-)
        [[ -n "$mac" ]] && success "Found: $mac ($name)"
    done
    bluetoothctl scan off &>/dev/null
}

scan_macos() {
    success "Using system_profiler to list Bluetooth devices on macOS..."
    system_profiler SPBluetoothDataType | grep -E "Address:|Name:" | while read -r line; do
        [[ $line == *"Address:"* ]] && mac=$(echo "$line" | awk '{print $2}')
        [[ $line == *"Name:"* ]] && name=$(echo "$line" | cut -d ':' -f2- | xargs)
        [[ -n "$mac" && -n "$name" ]] && success "Found: $mac ($name)"
    done
}

main() {
    echo -e "${YELLOW}[!] Starting Bluetooth scan...${RESET}"
    log "Starting Bluetooth scan..."

    case "$(uname)" in
        "Linux")
            scan_linux
            ;;
        "Darwin")
            scan_macos
            ;;
        *)
            error "Unsupported OS: $(uname)"
            exit 1
            ;;
    esac

    success "Scan complete. Log saved to $LOG_FILE"
}

main
