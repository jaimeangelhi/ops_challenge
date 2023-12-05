#!/usr/bin/env python3

# Script Name:                  challenge7.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/5/2023
# Purpose:                      Directory Creation
# Additional Source             ChatGPT

# Import libraries
import os

# Declaration of functions
def generate_directory_structure(user_path):
    for (root, dirs, files) in os.walk(user_path):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files==")
        print(files)

# Declaration of variables
user_input = input("Enter the directory path: ")

# Main
generate_directory_structure(user_input)
