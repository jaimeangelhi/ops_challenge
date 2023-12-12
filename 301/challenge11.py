#!/usr/bin/env python3

# Script Name:                  challenge11.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/11/2023
# Purpose:                      Use Psutil to fetch system information.
# Additional Source             ChatGPT

import psutil
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_system_info():
    info = {
        'User mode time': psutil.cpu_times().user,
        'Kernel mode time': psutil.cpu_times().system,
        'Idle time': psutil.cpu_times().idle,
        'Priority processes user mode time': psutil.cpu_times().nice,
        'Time waiting for I/O': psutil.cpu_times().iowait,
        'Time servicing hardware interrupts': psutil.cpu_times().irq,
        'Time servicing software interrupts': psutil.cpu_times().softirq,
        'Time running virtual CPU for guest OS': psutil.cpu_times().steal,
        'Time spent by other OS in a virtualized environment': psutil.cpu_times().guest,
    }
    return info

def save_to_txt(info, filename='system_info.txt'):
    with open(filename, 'w') as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")

def send_email(file_path, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = 'System Information Report'

    with open(file_path, 'r') as file:
        attachment = MIMEText(file.read())
    
    attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
    msg.attach(attachment)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

if __name__ == "__main__":
    # Set your email and SMTP server details
    to_email = 'jai.me.angel.hi@gmail.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'

    # Get system information
    system_info = get_system_info()

    # Save information to a text file
    save_to_txt(system_info)

    # Send email with the text file attached
    send_email('system_info.txt', to_email, smtp_server, smtp_port, smtp_username, smtp_password)
