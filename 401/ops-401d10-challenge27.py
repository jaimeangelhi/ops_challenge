#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge27.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      2/13/24
# Purpose:                      Event Logging Tool Part 2 of 3
# Additional Source             ChatGPT (https://chat.openai.com/share/b2d9b17e-9c27-47f0-bf23-7b35734a19cf), Class Demo


import logging
from logging.handlers import RotatingFileHandler

# Configure the logger
logger = logging.getLogger('MyLogger')  # Create a logger named 'MyLogger'
logger.setLevel(logging.DEBUG)  # Set the minimum log level to debug, so all messages are logged

# Create a log file handler with rotation
log_file_handler = RotatingFileHandler(
    'my_log.log',  # Name of the log file
    maxBytes=1024,  # Maximum size of a log file in bytes before it is rotated (1KB for this example)
    backupCount=3,  # Number of backup files to keep
)

# Create a formatter and set the format for log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file_handler.setFormatter(formatter)  # Apply the formatter to the file handler

# Add the file handler to the logger
logger.addHandler(log_file_handler)

# Example usage of the logger
try:
    # Your code here. Replace this line with your actual function/method calls.
    logger.info('This is an info message')
    
    # Induce an error for demonstration
    1 / 0  # This will cause a ZeroDivisionError
    
except Exception as e:
    logger.error('An error occurred: %s', str(e))  # Log the error

# Confirm that logging is working by looking at the log file ('my_log.log')
