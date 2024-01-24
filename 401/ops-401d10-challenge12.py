#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge12.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/23/24
# Purpose:                      Network Security Tool with Scapy Part 2 of 3
# Additional Source             ChatGPT (https://chat.openai.com/share/20e34574-cfc0-43ef-b426-5d83e6e3c8e1)

# Importing necessary libraries from Scapy and Python's standard library
from scapy.all import IP, TCP, ICMP, sr1, sr, RandShort, send
from ipaddress import ip_network
import sys

# Function to scan a single port on a given IP address
def scan_port(ip, port):
    # Create a SYN packet with a random source port and the specified destination port
    packet = IP(dst=ip)/TCP(sport=RandShort(), dport=port, flags="S")
    # Send the packet and wait for a response
    response = sr1(packet, timeout=1, verbose=0)

    # Check if no response was received
    if response is None:
        print(f"Port {port}: No response (Filtered or Dropped)")
    # Check if the response has a TCP layer
    elif response.haslayer(TCP):
        # If the response is a SYN-ACK, port is open
        if response.getlayer(TCP).flags == 0x12:  
            # Send a RST packet to close the connection
            rst_packet = IP(dst=ip)/TCP(sport=RandShort(), dport=port, flags="R")
            send(rst_packet, verbose=0)
            print(f"Port {port}: Open (Connection closed)")
        # If the response is a RST-ACK, port is closed
        elif response.getlayer(TCP).flags == 0x14:  
            print(f"Port {port}: Closed")
    # If the response is not a TCP packet
    else:
        print(f"Port {port}: Non-TCP response received")

# Function to perform an ICMP Ping Sweep
def icmp_ping_sweep(network):
    # Convert CIDR notation to a list of IP addresses
    addresses = ip_network(network, strict=False)
    online_hosts = 0  # Counter for online hosts

    # Iterate through all addresses in the network
    for host in addresses.hosts():
        # Send an ICMP echo request to the host
        resp = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        # Check if there's no response
        if resp is None:
            print(f"Host {host} is down or unresponsive.")
        # Check if the response has an ICMP layer
        elif resp.haslayer(ICMP):
            # Check for specific ICMP type and code indicating ICMP blocking
            if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print(f"Host {host} is actively blocking ICMP traffic.")
            else:
                # Any other ICMP response indicates the host is online
                print(f"Host {host} is responding.")
                online_hosts += 1
    # Print the total number of online hosts
    print(f"\nTotal online hosts: {online_hosts}")

# Main function of the script
def main():
    # User menu to choose between TCP Port Range Scanner and ICMP Ping Sweep
    choice = input("Choose the mode: \n1. TCP Port Range Scanner\n2. ICMP Ping Sweep\nEnter choice (1 or 2): ")
    
    # If user chooses TCP Port Range Scanner
    if choice == '1':
        # Prompt for target IP address
        target_ip = input("Enter target IP address: ")
        # Define port range to scan
        port_range = range(20, 1025)  # Can be customized
        # Scan each port in the range
        for port in port_range:
            scan_port(target_ip, port)
    # If user chooses ICMP Ping Sweep
    elif choice == '2':
        # Prompt for network address in CIDR notation
        network = input("Enter network address with CIDR (e.g., 10.10.0.0/24): ")
        # Perform ICMP Ping Sweep on the provided network
        icmp_ping_sweep(network)
    # If user makes an invalid choice
    else:
        print("Invalid choice")
        sys.exit(1)

# Check if the script is the main program and not an imported module
if __name__ == "__main__":
    main()  # Execute the main function
