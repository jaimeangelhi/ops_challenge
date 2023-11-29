#!/bin/bash

# Script Name:                  challenge2.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/28/2023
# Purpose:                      To create a bash script that: Copies /var/log/syslog to the current working directory and appends the current date and time to the filename
# Additional Sources            ChatGPT (https://chat.openai.com/share/0b222bfd-b4b8-427d-a792-61ffdccaa9a1)

# Define the source and destination filenames
source_file="/var/log/syslog"
current_date=$(date +"%Y%m%d_%H%M%S")
destination_file="challenge1${current_date}.sh"

# Copy the syslog file to the current working directory
cp "$source_file" "$destination_file"

# Display a message indicating the operation is complete
echo "Syslog copied to: $destination_file"
