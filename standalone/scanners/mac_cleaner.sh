#!/bin/bash

# Path to the file containing the list of MAC addresses
MAC_LIST_FILE="./master_mac_list.txt"

# Output file
OUTPUT_FILE="cleaned_mac_list.txt"

# Read the MAC addresses, remove duplicates, sort them, and save to the output file
sort -u "$MAC_LIST_FILE" > "$OUTPUT_FILE"

echo "Cleaned MAC addresses have been saved to $OUTPUT_FILE"
