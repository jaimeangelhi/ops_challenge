#!/usr/bin/env python3

# Script Name:                  challenge10.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/8/2023
# Purpose:                      Create, Append, Print, Delete
# Additional Source             ChatGPT

# Creating a new .txt file
file_name = "example.txt"

with open(file_name, "w") as file:
    # Appending three lines to the file
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Reading and printing the first line
with open(file_name, "r") as file:
    first_line = file.readline()
    print("First Line:", first_line)

# Deleting the .txt file
import os

os.remove(file_name)
print(f"{file_name} deleted.")
