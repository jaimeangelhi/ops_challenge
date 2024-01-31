#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge17.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/30/24
# Purpose:                      Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Additional Source             ChatGPT (https://chat.openai.com/share/319b6773-2998-48b0-ab57-aa7b48bd3e0d), Class Demo


import time
import paramiko

# Mode 1: Offensive; Dictionary Iterator
def mode_one(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for word in file:
                print(word.strip())
                time.sleep(1)  # Delay of 1 second between words
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Mode 4: SSH Command Execution
def ssh_connect(hostname, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)
        
        command = input("Enter the command to execute: ")
        stdin, stdout, stderr = client.exec_command(command)

        print("Output:")
        for line in stdout:
            print(line.strip())

        client.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Select a mode:\n1. Offensive; Dictionary Iterator\n4. SSH Command Execution")
    choice = input("Enter your choice (1 or 4): ")

    if choice == '1':
        file_path = input("Enter the file path for the word list: ")
        mode_one(file_path)
    elif choice == '4':
        hostname = input("Enter the server IP: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        ssh_connect(hostname, username, password)
    else:
        print("Invalid choice. Please select 1 or 4.")

if __name__ == "__main__":
    main()
