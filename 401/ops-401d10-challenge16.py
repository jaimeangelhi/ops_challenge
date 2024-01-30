#!/usr/bin/env python3

# Script Name:                  ops-401d10-challenge16.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      1/29/24
# Purpose:                      Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Additional Source             ChatGPT, Class Demo

import time
import re

# Reads a word list from the given file path.
def read_word_list(file_path):
    word_list = []
    try:
        with open(file_path, 'r') as file:
            word_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return word_list

# Mode 1: Offensive; Dictionary Iterator
def dictionary_iterator():
    words = read_word_list('rockyou_sample.txt')
    for word in words:
        print(word)
        time.sleep(0.5)  # Delay between words, fulfilling the delay requirement.

# Mode 2: Defensive; Password Recognized
def password_recognized(password):
    words = read_word_list('rockyou_sample.txt')
    if password in words:
        print("The password is recognized in the word list.")
    else:
        print("The password is not in the word list.")

# Mode 3: Defensive; Password Complexity
def password_complexity_check(password):
    # Complexity requirements
    min_length = 8
    min_upper = 2
    min_numbers = 2
    min_symbols = 1

    # Check each complexity requirement
    length_check = len(password) >= min_length
    upper_check = len(re.findall(r'[A-Z]', password)) >= min_upper
    number_check = len(re.findall(r'[0-9]', password)) >= min_numbers
    symbol_check = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) >= min_symbols

    # Report each requirement's status
    print(f"Password length requirement met: {length_check}")
    print(f"Capital letter requirement met: {upper_check}")
    print(f"Number requirement met: {number_check}")
    print(f"Symbol requirement met: {symbol_check}")

    # Indicate overall success if all requirements are met
    if all([length_check, upper_check, number_check, symbol_check]):
        print("SUCCESS: The password meets all complexity requirements.")

def main():
    print("Select Mode: \n1. Dictionary Iterator \n2. Password Recognized \n3. Password Complexity")
    mode = input("Enter mode number: ")

    # Execute the selected mode
    if mode == '1':
        dictionary_iterator()
    elif mode == '2':
        password = input("Enter the password to check: ")
        password_recognized(password)
    elif mode == '3':
        password = input("Enter the password to check for complexity: ")
        password_complexity_check(password)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
