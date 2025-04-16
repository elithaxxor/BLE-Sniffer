""" provides helper functions for BLE-related tasks """

import datetime  # Importing the datetime module for working with timestamps

def format_mac(mac: str) -> str:
    """
    Format a MAC address to standard notation.
    Converts the MAC address to uppercase and replaces dashes or underscores with colons.
    
    Args:
        mac (str): The MAC address in string format.
        
    Returns:
        str: Formatted MAC address in standard notation.
    """
    return mac.upper().replace("-", ":").replace("_", ":")

def human_time(ts: float = None) -> str:
    """
    Convert a timestamp to a human-readable date and time string.
    If no timestamp is provided, the current time is used.
    
    Args:
        ts (float, optional): Unix timestamp. Defaults to None.
        
    Returns:
        str: Human-readable date and time string in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    if ts is None:  # If no timestamp is provided, use the current time
        ts = datetime.datetime.now().timestamp()
    # Convert the Unix timestamp to a human-readable format
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def write_csv(devices: list, filename: str):
    """
    Write a list of BLE device data to a CSV file.
    
    Args:
        devices (list): A list of dictionaries containing device data.
            Each dictionary should have keys: 'timestamp', 'address', 'name', 'rssi', 'manufacturer_data'.
        filename (str): The name of the CSV file to write the data to.
    """
    import csv  # Importing the CSV module for writing to CSV files
    # Define the list of keys (columns) to write in the CSV file
    keys = ['timestamp', 'address', 'name', 'rssi', 'manufacturer_data']
    # Open the file in write mode, ensuring UTF-8 encoding and no extra newline characters
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)  # Create a CSV writer with the specified fieldnames
        writer.writeheader()  # Write the header row to the CSV file
        for d in devices:  # Iterate over each device in the list
            # Write the device data to the file, ensuring missing keys are replaced with empty strings
            writer.writerow({k: d.get(k, "") for k in keys})

def truncate_hex(data: bytes, max_len=16) -> str:
    """
    Convert a byte sequence to a hexadecimal string, truncated to a maximum length.
    If the data exceeds the maximum length, append an indicator showing the total byte size.
    
    Args:
        data (bytes): The byte sequence to convert to a hexadecimal string.
        max_len (int, optional): Maximum length of the output string. Defaults to 16.
        
    Returns:
        str: Truncated hexadecimal string with an optional size indicator if truncated.
    """
    # Convert the first max_len bytes of the data to a hexadecimal string and make it uppercase
    s = data[:max_len].hex().upper()
    # If the data length exceeds max_len, append an indicator showing the total size
    if len(data) > max_len:
        s += "...(%d bytes)" % len(data)
    return s
