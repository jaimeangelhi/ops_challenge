#!/bin/bash

# Script Name:                  challenge03.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      10/27/2023
# Purpose:                      displays running processes, asks the user for a PID, then kills the process with that PID.
# Additional sources            ChatGpt  (https://chat.openai.com/c/fd00dbf0-139a-40d3-8d4f-9bc8ccfe61ed)     


# Declaration of variables

# Declaration of functions


# Main

while true
do
   
    clear
    echo "Running Processes:"
    ps aux


    read -p "Enter the PID of the process to kill (or Ctrl + C to exit): " pid

  
    if [[ "$pid" =~ ^[0-9]+$ ]]; then
       
        if kill -9 "$pid" &> /dev/null; then
            echo "Process with PID $pid has been killed."
        else
            echo "Unable to kill process with PID $pid."
        fi
    else
        echo "Invalid PID. Please enter a valid numeric PID."
    fi

    read -p "Press Enter to continue..."
done

# End
