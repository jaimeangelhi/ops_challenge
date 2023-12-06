#!/usr/bin/env python3

# Script Name:                  challenge6.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/5/2023
# Purpose:                      Bash in Python
# Additional Source             ChatGPT


import os

# Declare three variables
user_name = os.getenv('USER')  # Get the current username
ip_address_command = 'ip a'     # Command to retrieve IP address information
hardware_info_command = 'lshw -short'  # Command to retrieve hardware information

# Print the username using the whoami command
print(f"Current user: {user_name}")

# Execute and print the result of the 'ip a' command
ip_result = os.popen(ip_address_command).read()
print(f"IP Address Information:\n{ip_result}")

# Execute and print the result of the 'lshw -short' command
hardware_result = os.popen(hardware_info_command).read()
print(f"Hardware Information:\n{hardware_result}")

