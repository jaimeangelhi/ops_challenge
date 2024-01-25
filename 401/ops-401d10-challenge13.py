#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge13.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/24/24
# Purpose:                      Network Security Tool with Scapy Part 3 of 3
# Additional Source             ChatGPT (https://chat.openai.com/share/20e34574-cfc0-43ef-b426-5d83e6e3c8e1)

# Import necessary modules from Scapy
from scapy.all import IP, TCP, ICMP, sr1, sr, RandShort, send
import sys

# Function to scan a single port on a given IP address
def scan_port(ip, port):
    # Create a SYN packet with a random source port and the specified destination port
    packet = IP(dst=ip)/TCP(sport=RandShort(), dport=port, flags="S")
    # Send the packet and wait for a response
    response = sr1(packet, timeout=1, verbose=0)

    # Determine the status of the port based on the response
    if response is None:
        return "Filtered or Dropped"  # No response received
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            # Port is open, send a RST packet to close the connection
            rst_packet = IP(dst=ip)/TCP(sport=RandShort(), dport=port, flags="R")
            send(rst_packet, verbose=0)
            return "Open"
        elif response.getlayer(TCP).flags == 0x14:
            return "Closed"  # Port is closed
    else:
        return "Non-TCP response received"  # Non-TCP packet received

# Function to ping a host to check its responsiveness
def ping_host(ip):
    # Create an ICMP echo request packet
    packet = IP(dst=ip)/ICMP()
    # Send the packet and wait for a response
    response = sr1(packet, timeout=1, verbose=0)
    # Return True if a response is received, indicating the host is up
    return response is not None

# Function to perform a port scan on a responsive host
def port_scan(ip):
    # Define the range of ports to scan
    port_list = range(80, 443, 221)
    # List to store open ports
    open_ports = []
    # Scan each port in the defined range
    for port in port_range:
        status = scan_port(ip, port)
        # Add port to list if it is open
        if status == "Open":
            open_ports.append(port)
    # Return the list of open ports
    return open_ports

# Main function
def main():
    # Prompt for target IP address (Requirement: Prompt user for an IP address)
    target_ip = input("Enter target IP address: ")

    # Ping the host and proceed if it is responsive (Requirement: Ping an IP address)
    if ping_host(target_ip):
        print(f"Host {target_ip} is up. Starting port scan...")
        # Perform port scan if the host is responsive (Requirement: Call the port scan function if the host is responsive)
        open_ports = port_scan(target_ip)
        # Print the results of the port scan (Requirement: Print the output to the screen)
        if open_ports:
            print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
        else:
            print(f"No open ports found on {target_ip}.")
    else:
        # Inform the user if the host is down or not responding
        print(f"Host {target_ip} is down or not responding to pings.")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
