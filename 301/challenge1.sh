#!/bin/bash

# Define the source and destination filenames
source_file="/var/log/syslog"
current_date=$(date +"%Y%m%d_%H%M%S")
destination_file="challenge1${current_date}.sh"

# Copy the syslog file to the current working directory
cp "$source_file" "$destination_file"

# Display a message indicating the operation is complete
echo "Syslog copied to: $destination_file"