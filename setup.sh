#!/usr/bin/env bash
set -e

echo "==== [ BLE-Sniffer Auto Installer ] ===="

# 1. Install system dependencies (Debian/Ubuntu/Raspberry Pi OS)
echo "[*] Installing system dependencies..."
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-dev build-essential libglib2.0-dev libbluetooth-dev bluez bluez-tools

# 2. Select project
echo
echo "Which BLE-Sniffer project do you want to setup and run?"
echo "1) Web Interface (Flask)"
echo "2) GUI BLE Sniffer"
echo "3) CLI BLE Sniffer"
read -rp "Enter [1/2/3]: " choice

case "$choice" in
    1)
        PROJECT_PATH="BLE_WEB"
        REQUIREMENTS="$PROJECT_PATH/requirements.txt"
        MAIN_CMD="cd BLE_WEB && flask run"
        ;;
    2)
        PROJECT_PATH="standalone/scanners/python/GUI"
        REQUIREMENTS="$PROJECT_PATH/requirements.txt"
        MAIN_CMD="cd standalone/scanners/python/GUI && python3 sniff_my_ble.py"
        ;;
    3)
        PROJECT_PATH="standalone/scanners/python/CLI"
        REQUIREMENTS="$PROJECT_PATH/requirements.txt"
        MAIN_CMD="cd standalone/scanners/python/CLI && python3 sniff_my_ble.py"
        ;;
    *)
        echo "[!] Invalid choice."
        exit 1
        ;;
esac

# 3. Set up Python environment
echo "[*] Creating Python virtual environment in .venv ..."
python3 -m venv .venv
source .venv/bin/activate

# 4. Install Python dependencies
echo "[*] Installing Python dependencies from $REQUIREMENTS ..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS"

echo "[*] Setup complete!"

# 5. Autorun
echo "[*] Running main program..."
eval "$MAIN_CMD"
