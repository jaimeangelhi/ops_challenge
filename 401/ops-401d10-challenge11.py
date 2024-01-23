#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge11.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/22/24
# Purpose:                      Network Security Tool with Scapy Part 1 of 3
# Additional Source             ChatGPT (https://chat.openai.com/share/20e34574-cfc0-43ef-b426-5d83e6e3c8e1)

pip install scapy

from scapy.all import *

# Function to scan a single port
def scan_port(ip, port):
    src_port = RandShort()  # Generate a random source port
    pkt = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S') # Create a SYN packet
    resp = sr1(pkt, timeout=2, verbose=0) # Send the packet and wait for a response

    # Check if no response was received
    if resp is None:
        print(f"Port {port} is filtered (silently dropped).")
    # If a TCP layer is present in the response
    elif resp.haslayer(TCP):
        # If the flags are 0x12 (SYN-ACK), the port is open
        if resp.getlayer(TCP).flags == 0x12: 
            # Send a RST packet to close the connection gracefully
            send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='R'), timeout=1, verbose=0)
            print(f"Port {port} is open.")
        # If the flags are 0x14 (RST-ACK), the port is closed
        elif resp.getlayer(TCP).flags == 0x14: 
            print(f"Port {port} is closed.")
    else:
        # If the response doesn't have a TCP layer, it's considered filtered
        print(f"Port {port} is filtered (silently dropped).")

# Main function
def main():
    target_ip = "192.168.1.1"  # Set the target IP address
    port_range = [22, 80, 443] # Define the port range to scan

    # Iterate over each port in the range
    for port in port_range:
        scan_port(target_ip, port) # Call the scan_port function for each port

# Entry point of the script
if __name__ == "__main__":
    main()  # Execute the main function
