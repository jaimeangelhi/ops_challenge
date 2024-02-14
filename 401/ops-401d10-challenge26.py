#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge26.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      2/12/24
# Purpose:                      Event Logging Tool Part 1 of 3
# Additional Source             ChatGPT (https://chat.openai.com/c/d31349d6-b489-4c84-be05-e12fb3bff629), Class Demo

# Import necessary libraries
import subprocess  # Used for executing system commands
import logging  # Used for logging

# Configure logging to write to a file with the desired level and format
logging.basicConfig(filename='pentest_log.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to ping a host
def ping_host(host):
    """
    This function pings a given host to check its availability.
    :param host: IP address or domain to ping
    """
    try:
        # Ping command with count set to 1 for Linux/Mac and Windows
        command = ['ping', '-c', '1', host] if subprocess.os.name == 'posix' else ['ping', '-n', '1', host]

        # Execute the ping command
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if ping was successful
        if response.returncode == 0:
            logging.info(f"Successfully pinged {host}")
            print(f"Success: {host} is reachable.")
        else:
            logging.warning(f"Failed to ping {host}")
            print(f"Warning: {host} is not reachable.")
    except Exception as e:
        # Log any errors that occur during the ping process
        logging.error(f"Error pinging {host}: {str(e)}")
        print(f"Error: Could not ping {host} due to an exception.")

# Example usage
if __name__ == "__main__":
    # Host to be pinged
    host = 'google.com'  # You can change this to any host you wish to ping
    # Call the ping function
    ping_host(host)
