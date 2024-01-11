#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge03.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/10/24
# Purpose:                      Uptime sensor in python emailed
# Additional Source             ChatGPT (https://chat.openai.com/share/758f5906-5687-4aa4-909b-7f34235e180f)

#import statements
import os  # Import the 'os' module to interact with the operating system
import time  # Import the 'time' module for time-related tasks
import subprocess  # Import the 'subprocess' module to execute system commands
import datetime  # Import the 'datetime' module to work with dates and times
import smtplib  # Import the 'smtplib' module to send emails using SMTP
from email.mime.text import MIMEText  # Import MIMEText to create text-based email parts
from email.mime.multipart import MIMEMultipart  # Import MIMEMultipart to create multipart/mixed email messages

# 'send_email' function
def send_email(sender_email, sender_password, recipient_email, subject, message, use_cloud_service=False):
    """
    Send an email with the specified subject and message.
    Optionally, use a cloud mailer service.
    """
    if use_cloud_service:
        pass  # Placeholder for cloud mail service code
    else:
        msg = MIMEMultipart()  # Create a multipart/mixed email message
        msg['From'] = sender_email  # Set the sender's email address
        msg['To'] = recipient_email  # Set the recipient's email address
        msg['Subject'] = subject  # Set the email's subject

        msg.attach(MIMEText(message, 'plain'))  # Attach the message text to the email

        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail's SMTP server
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Log in to the SMTP server
        text = msg.as_string()  # Convert the MIMEMultipart message to a string
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()  # Terminate the SMTP session

# 'ping_host' function
def ping_host(ip_address):
    """
    Ping an IP address and return True if the host is reachable, False otherwise.
    """
    try:
        param = '-n 1' if os.name == 'nt' else '-c 1'  # Set ping command parameters based on OS
        response = subprocess.run(['ping', param, ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Run the ping command
        return response.returncode == 0  # Return True if ping succeeds (returncode 0)
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any exceptions
        return False  # Return False if an exception occurs

# 'append_to_event_log' Function
def append_to_event_log(event_log, timestamp, event_code, ip_address, description):
    """
    Append an event to the event log.
    """
    with open(event_log, "a") as file:
        file.write(f"{timestamp}, {event_code}, {ip_address}, {description}\n")  # Write the event details to the log file

# 'main' function
def main(target_ip, sender_email, sender_password, recipient_email):
    log_file = "uptime_log.txt"  # Define the uptime log file name
    event_log = "event_log.txt"  # Define the event log file name
    previous_status = None  # Initialize previous status as None

    while True:  # Start an infinite loop
        current_status = "Network Active" if ping_host(target_ip) else "Network Inactive"  # Check the current network status
        timestamp = datetime.datetime.now()  # Get the current timestamp
        log_entry = f"{timestamp} {current_status} to {target_ip}\n"  # Prepare the log entry
        
        print(log_entry, end="")  # Print the log entry to console
        with open(log_file, "a") as file:  # Write the log entry to the uptime log file
            file.write(log_entry)

        if previous_status is not None and previous_status != current_status:  # Check if the status has changed
            event_code = "STATUS_CHANGE"  # Define the event code for status change
            event_description = f"Status changed from {previous_status} to {current_status}"  # Prepare the event description
            append_to_event_log(event_log, timestamp, event_code, target_ip, event_description)  # Log the event

            subject = f"Status Changed for {target_ip}"  # Email subject for status change
            email_message = f"{event_description} at {timestamp}"  # Prepare the email message
            send_email(sender_email, sender_password, recipient_email, subject, email_message)  # Send the notification email

        previous_status = current_status  # Update the previous status
        time.sleep(2)  # Wait for 2 seconds before next iteration

#Script execution block
if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")  # Ask for target IP address

    sender_email = os.getenv('BURNER_EMAIL_ADDRESS', input("Enter your email address for sending notifications: "))  # Get or ask for sender email
    sender_password = os.getenv('BURNER_EMAIL_PASSWORD', input("Enter your email password: "))  # Get or ask for sender email password
    recipient_email = input("Enter the recipient email address for notifications: ")  # Ask for recipient email

    main(target_ip, sender_email, sender_password, recipient_email)  # Execute the main function with the given parameters
