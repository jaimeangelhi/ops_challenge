#!/bin/bash


# Script Name:                  challenge5.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/1/2023
# Purpose:                      Print to the screen the file size of the log files before compression, compress the contents of the log files listed below to a backup directory, clear the contents of the log file, print to screen the file size of the compressed file, and compare the size of the compressed files to the size of the original log files
# Additional Source             ChatGPT

# Set the backup directory
backup_dir="/var/log/backups"

# Ensure the backup directory exists
mkdir -p "$backup_dir"

# Get the current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Define the log files
log_files=("/var/log/syslog" "/var/log/wtmp")

# Print original file sizes
echo "Original file sizes before compression:"
for log_file in "${log_files[@]}"; do
    file_size=$(du -h "$log_file" | cut -f1)
    echo "$log_file: $file_size"
done

# Compress log files to backup directory
for log_file in "${log_files[@]}"; do
    # Construct the backup file name with timestamp
    backup_file="$backup_dir/$(basename "$log_file")-$timestamp.zip"
    
    # Compress the log file
    gzip -c "$log_file" > "$backup_file"
    
    # Clear the contents of the original log file
    > "$log_file"
    
    # Print compressed file size
    compressed_size=$(du -h "$backup_file" | cut -f1)
    echo "Compressed file size for $backup_file: $compressed_size"
done

# Print original and compressed file sizes for comparison
echo "Comparison of file sizes:"
for log_file in "${log_files[@]}"; do
    original_size=$(du -h "$log_file" | cut -f1)
    compressed_file="$backup_dir/$(basename "$log_file")-$timestamp.zip"
    compressed_size=$(du -h "$compressed_file" | cut -f1)
    
    echo "Original $log_file size: $original_size"
    echo "Compressed $compressed_file size: $compressed_size"
done
