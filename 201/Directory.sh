#!/bin/bash

# Script Name:                  Directory
# Author:                       Jai.me.angel.hi
# Date of latest revision:      10/26/2023
# Purpose:                      Create an array directory
# Additional Source             ChatGPT (https://chat.openai.com/share/245ae3ec-6ba5-42fa-ae6b-15ec21d25730)


# Create four directories
mkdir dir1 dir2 dir3 dir4

# Put the names of the directories in an array
directories=("dir1" "dir2" "dir3" "dir4")

# Loop through the array and create a new .txt file in each directory
for dir in "${directories[@]}"; do
    touch "$dir/file.txt"
    echo "File created in $dir"
done
