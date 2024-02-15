



import logging
from scapy.all import IP, TCP, ICMP, sr1, RandShort, send
import sys

# Set up logging
logger = logging.getLogger('NetworkScanner')
logger.setLevel(logging.DEBUG)  # Log messages of all levels

# Create a file handler to log messages to a file
file_handler = logging.FileHandler('ops22.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create a stream handler for logging to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Change this to DEBUG if you want to see debug messages in the console
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Function definitions remain the same...
# Remember to replace print statements with logger calls, for example:
# print(f"Host {target_ip} is up. Starting port scan...")
# becomes
# logger.info(f"Host {target_ip} is up. Starting port scan...")

def main():
    target_ip = input("Enter target IP address: ")
    if ping_host(target_ip):
        logger.info(f"Host {target_ip} is up. Starting port scan...")
        open_ports = port_scan(target_ip)
        if open_ports:
            logger.info(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
        else:
            logger.info("No open ports found on {target_ip}.")
    else:
        logger.info(f"Host {target_ip} is down or not responding to pings.")

if __name__ == "__main__":
    main()
