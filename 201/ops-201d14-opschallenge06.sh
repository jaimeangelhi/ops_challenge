#!/bin/bash

# Script Name:                  ops-201d14-opschallenge06.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/12/2023
# Purpose:                      defines array of file/directory, loops through array to see if file exists, and creates and adds to the array if not.

#Additional Resources      ChatGPT (https://chat.openai.com/share/1cee371c-742f-44fb-84fc-4337cc7252b9)


# Define an array of file and directory paths
paths=("example_file.txt" "example_directory")

# Loop through each path in the array
for path in "${paths[@]}"; do
    # Check if the path exists
    if [ -e "$path" ]; then
        echo "$path exists."
    else
        # If it doesn't exist, create it
        if [ -f "$path" ]; then
            touch "$path"
            echo "File $path created."
        elif [ -d "$path" ]; then
            mkdir "$path"
            echo "Directory $path created."
        else
            echo "Invalid path: $path"
        fi
    fi
done
