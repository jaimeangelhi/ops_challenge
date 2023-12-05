#!/usr/bin/env python3

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
