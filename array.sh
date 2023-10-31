#!/bin/bash

# Script Name:                  array.sh
# Author Name:                  jai.me.angel.hi
# Date of latest revision:      10.26.2023
# Purpose:                      Demo array
# Execution:                    bash array.sh or ./array.sh chmod -x array.sh
# Additional Sources:           X


target_directoy="/home/jaha/ops-reading-notes"

if [ -d "$target_directory" ]; then 
    mapfile -t files_and_directories < <(find "$target_directory" -maxdepth 1 -type d -o -type f)

    for item in "${files_and_directories[@]}"; do
        echo "item"
    done
else
    echo "Target directory does not exist."
fi 


