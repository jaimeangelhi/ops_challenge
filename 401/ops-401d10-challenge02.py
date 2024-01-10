#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge02.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/9/24
# Purpose:                      Uptime sensor in python
# Additional Source             ChatGPT (https://chat.openai.com/share/758f5906-5687-4aa4-909b-7f34235e180f)



import os  # Import the 'os' module for operating system dependent functionality
import time  # Import the 'time' module for time-related tasks
import subprocess  # Import the 'subprocess' module to execute shell commands
import datetime  # Import the 'datetime' module for date and time related functions

# Define the function 'ping_host', which will ping an IP address and return True if the host is reachable, False otherwise
def ping_host(ip_address):
    """
    Ping an IP address and return True if the host is reachable, False otherwise.
    """
    try:
        # Set the ping parameter depending on the operating system (-n for Windows, -c for others)
        param = '-n 1' if os.name == 'nt' else '-c 1'
        # Execute the ping command for the given IP address
        response = subprocess.run(['ping', param, ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Return True if the ping command was successful (returncode 0), False otherwise
        return response.returncode == 0
    except Exception as e:
        # Print any exceptions that occur during the ping process
        print(f"An error occurred: {e}")
        return False

# Define the main function, which will be the entry point of our program
def main(target_ip):
    log_file = "uptime_log.txt"  # Set the name of the log file

    while True:  # Start an infinite loop
        # Check if the target IP is up (Network Active) or down (Network Inactive)
        status = "Network Active" if ping_host(target_ip) else "Network Inactive"
        # Get the current date and time
        timestamp = datetime.datetime.now()
        # Prepare the log entry string
        log_entry = f"{timestamp} {status} to {target_ip}\n"
        
        # Print the log entry to the console
        print(log_entry, end="")

        # Open the log file and append the log entry
        with open(log_file, "a") as file:
            file.write(log_entry)
        
        time.sleep(2)  # Wait for 2 seconds before the next loop iteration

# This block checks if the script is being run directly (and not imported as a module)
if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Set the default target IP address
    main(target_ip)  # Call the main function with the target IP address
