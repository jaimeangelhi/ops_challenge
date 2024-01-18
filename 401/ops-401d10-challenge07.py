#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge07.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/17/24
# Purpose:                      Encrypt/Decrypt file or message pt II
# Additional Source             ChatGPT (https://chat.openai.com/share/4f010740-a3d4-43c7-84de-8e3062ae4941)

from cryptography.fernet import Fernet  # Import the Fernet class for symmetric encryption
import os  # Import os module for interacting with the operating system
import zipfile  # Import zipfile module for file compression

def generate_key():
    return Fernet.generate_key()  # Generate a new symmetric encryption key

def load_key():
    return generate_key()  # In real applications, implement a secure method to load an existing key

def encrypt_file(file_path, key):
    f = Fernet(key)  # Create a Fernet object with the provided encryption key
    with open(file_path, 'rb') as file:  # Open the target file in binary read mode
        file_data = file.read()  # Read the file data
    encrypted_data = f.encrypt(file_data)  # Encrypt the file data using Fernet
    with open(file_path, 'wb') as file:  # Open the file again in binary write mode
        file.write(encrypted_data)  # Write the encrypted data back to the file

def decrypt_file(file_path, key):
    f = Fernet(key)  # Create a Fernet object with the provided encryption key
    with open(file_path, 'rb') as file:  # Open the file in binary read mode
        encrypted_data = file.read()  # Read the encrypted data
    decrypted_data = f.decrypt(encrypted_data)  # Decrypt the data using Fernet
    with open(file_path, 'wb') as file:  # Open the file in binary write mode
        file.write(decrypted_data)  # Write the decrypted data back to the file

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):  # Traverse the directory tree
        for file in files:  # Iterate over each file in the directory
            file_path = os.path.join(root, file)  # Join the directory path and file name
            encrypt_file(file_path, key)  # Encrypt the file

def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):  # Traverse the directory tree
        for file in files:  # Iterate over each file in the directory
            file_path = os.path.join(root, file)  # Join the directory path and file name
            decrypt_file(file_path, key)  # Decrypt the file

def main():
    key = load_key()  # Load or generate the encryption key
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a directory\n4. Decrypt a directory\n> ")  # Prompt the user to choose an operation mode

    if mode == '1' or mode == '2':
        file_path = input("Enter the file path: ")  # Prompt for the file path
        if mode == '1':
            encrypt_file(file_path, key)  # Encrypt the specified file
        else:
            decrypt_file(file_path, key)  # Decrypt the specified file

    elif mode == '3' or mode == '4':
        directory_path = input("Enter the directory path: ")  # Prompt for the directory path
        if mode == '3':
            encrypt_directory(directory_path, key)  # Encrypt all files in the specified directory
        else:
            decrypt_directory(directory_path, key)  # Decrypt all files in the specified directory

if __name__ == "__main__":
    main()  # Execute the main function if the script is run as the main program
