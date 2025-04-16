"""
Utility module for BLE-Sniffer Standalone.
Handles formatting, file exports, color output, logging, and filtering.
"""

import datetime
import csv
from typing import List, Dict, Optional, Callable
import sys

# ===== Color Output for Terminal =====
class Colors:
    """
    ANSI escape codes for colored terminal output.
    Used for styling text like headers, warnings, errors, etc.
    """
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"  # Reset color
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def supports_color() -> bool:
    """
    Check if the current terminal supports colored output.
    Returns:
        bool: True if color is supported, False otherwise.
    """
    if sys.platform == 'win32':
        return False  # Windows terminals often lack color support unless using external libraries like colorama.
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

# Determine if colors should be used in the terminal
USE_COLOR = supports_color()

def cstr(txt, style):
    """
    Return a colored string if the terminal supports it.
    Args:
        txt (str): Text to be styled.
        style (str): ANSI style to apply.
    Returns:
        str: Styled or plain text based on terminal support.
    """
    if USE_COLOR:
        return f"{style}{txt}{Colors.ENDC}"
    else:
        return txt


# ===== MAC and Data Formatting =====
def format_mac(mac: str) -> str:
    """
    Format a MAC address to standard notation (uppercase with colons).
    Args:
        mac (str): Input MAC address.
    Returns:
        str: Formatted MAC address.
    """
    return mac.upper().replace("-", ":").replace("_", ":")

def human_time(ts: Optional[float] = None) -> str:
    """
    Convert a timestamp to a human-readable date and time string.
    Args:
        ts (float, optional): Unix timestamp. Defaults to current time.
    Returns:
        str: Human-readable timestamp in 'YYYY-MM-DD HH:MM:SS' format.
    """
    if ts is None:
        ts = datetime.datetime.now().timestamp()
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def truncate_hex(data: bytes, max_len=16) -> str:
    """
    Show a byte sequence as a truncated hexadecimal string.
    Args:
        data (bytes): The byte sequence to convert.
        max_len (int): Maximum number of bytes to display. Defaults to 16.
    Returns:
        str: Truncated hexadecimal string with length indicator if truncated.
    """
    if not data:
        return ""
    s = data[:max_len].hex().upper()
    if len(data) > max_len:
        s += f"...({len(data)} bytes)"
    return s

def decode_name(device, adv_data) -> str:
    """
    Extract the name of a BLE device from device or advertisement data.
    Args:
        device: BLE device object.
        adv_data: BLE advertisement data.
    Returns:
        str: Device name or '<unknown>' if unavailable.
    """
    name = getattr(device, "name", None)
    if not name:
        name = getattr(adv_data, "local_name", None)
    if not name:
        name = "<unknown>"
    return name


# ===== CSV and File Export =====
def write_csv(devices: List[Dict], filename: str, fields: Optional[List[str]] = None) -> None:
    """
    Write a list of BLE device data to a CSV file.
    Args:
        devices (list): List of dictionaries containing device data.
        filename (str): Name of the CSV file to save.
        fields (list, optional): List of fields/columns to include. Defaults to all keys in the first dictionary.
    """
    if not devices:
        return
    if fields is None:
        fields = list(devices[0].keys())  # Use keys from the first device dictionary as columns
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()  # Write column headers
        writer.writerows(devices)  # Write all device data rows

def write_log(lines: List[str], filename: str) -> None:
    """
    Save a plain text log file.
    Args:
        lines (list): List of log lines to save.
        filename (str): Name of the log file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")  # Write each line with a newline character


# ===== Filtering =====
def fuzzy_match(text: str, patterns: List[str]) -> bool:
    """
    Check if a text matches any pattern in a list (case-insensitive substring matching).
    Args:
        text (str): Text to search within.
        patterns (list): List of patterns to match against.
    Returns:
        bool: True if any pattern matches, False otherwise.
    """
    if not patterns:
        return True  # No patterns means always match
    return any(pattern.lower() in text.lower() for pattern in patterns)


# ===== Manufacturer Data Pretty Print =====
def prettify_manufacturer(manuf: dict) -> str:
    """
    Create a human-readable string representation of manufacturer data.
    Args:
        manuf (dict): Dictionary of manufacturer data.
    Returns:
        str: Formatted string with manufacturer data.
    """
    if not manuf:
        return ""
    parts = []
    for k, v in manuf.items():
        s = f"0x{k:04X}: {truncate_hex(bytes(v))}"  # Format key as hex and value as truncated hex
        parts.append(s)
    return "; ".join(parts)  # Combine all parts into a single string


# ===== Logging (for developers/tests) =====
def debug(msg: str):
    """
    Print a debug message with a timestamp.
    Args:
        msg (str): Debug message to print.
    """
    ts = human_time()
    print(cstr(f"[DEBUG {ts}] {msg}", Colors.OKCYAN))

def warn(msg: str):
    """
    Print a warning message with a timestamp.
    Args:
        msg (str): Warning message to print.
    """
    ts = human_time()
    print(cstr(f"[WARNING {ts}] {msg}", Colors.WARNING))
