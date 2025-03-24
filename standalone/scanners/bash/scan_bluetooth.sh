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

check_dependencies() {
    if ! command -v bluetoothctl &>/dev/null && ! command -v system_profiler &>/dev/null; then
        error "Required tools are not available on this system."
        exit 1
    fi
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

show_menu() {
    echo -e "${YELLOW}Choose scan interval:${RESET}"
    echo "1. Scan every 30 seconds"
    echo "2. Scan every 3 minutes"
    echo "3. Scan every 10 minutes"
    echo "4. Continuous scan"
    echo "5. Exit"
}

get_interval() {
    case $1 in
        1) echo 30 ;;
        2) echo 180 ;;
        3) echo 600 ;;
        4) echo 0 ;;
        *) echo -1 ;;
    esac
}

main() {
    check_dependencies

    while true; do
        show_menu
        read -p "Enter your choice (1-5): " choice
        interval=$(get_interval $choice)

        if [ $interval -eq -1 ]; then
            error "Invalid choice. Please select a valid option."
            continue
        elif [ $interval -eq 0 ]; then
            info "Starting continuous Bluetooth scan..."
            while true; do
                scan_based_on_os
                sleep 30
            done
        elif [ $choice -eq 5 ]; then
            echo "Exiting..."
            break
        else
            info "Starting Bluetooth scan every $interval seconds..."
            while true; do
                scan_based_on_os
                sleep $interval
            done
        fi
        break
    done

    success "Script terminated. Log saved to $LOG_FILE"
}

scan_based_on_os() {
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
}

main
