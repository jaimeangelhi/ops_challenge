#!/bin/bash

# Script Name:                  challenge3.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/29/2023
# Purpose:                      To create a bash script that: change the permissions of files in the specified directory, display the contents and permissions, and create a log file with a record of the actions taken. Additionally, it will display each file changed one by one with a slight delay between each file.
# Additional Source             ChatGPT



# Prompt user for input directory path
read -p "Enter the directory path: " directory

# Prompt user for input permissions number
read -p "Enter the permissions number (e.g., 777): " permissions

# Log file
log_file="change_permissions_log.txt"

# Function to change permissions and log actions
change_permissions() {
    for file in "$directory"/*; do
        if [ -f "$file" ]; then
            echo "Changing permissions of $file to $permissions"
            chmod "$permissions" "$file"
            echo "Changed permissions of $file to $permissions" >> "$log_file"
            echo "File: $file, Permissions: $permissions"
            sleep 0.5  # Introducing a slight delay between each file changed
        fi
    done
}

# Check if the directory exists
if [ -d "$directory" ]; then
    cd "$directory" || exit 1

    # Perform the actions and log them
    change_permissions

    # Display directory contents and permissions
    echo -e "\nDirectory Contents:"
    ls -l
    echo -e "\nPermissions Settings:"
    stat -c "%A %n" *
else
    echo "Error: Directory not found."
fi

# Display log file location
echo -e "\nLog file created: $log_file"
