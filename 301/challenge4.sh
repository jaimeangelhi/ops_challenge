#!/bin/bash

# Script Name:                  challenge4.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/30/2023
# Purpose:                      To create a bash script that launches a menu system with the following options:Hello world (prints “Hello world!” to the screen), Ping self (pings this computer’s loopback address), IP info (print the network adapter information for this computer), Exit. Next, the user input should be requested. The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected. Use a loop to bring up the menu again after the request has been executed.
# Additional Source             ChatGPT


while true; do
    # Display menu options
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # Request user input
    read -p "Enter your choice (1-4): " choice

    # Evaluate user input with a conditional statement
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1  # Ping the loopback address
            ;;
        3)
            ifconfig  # Display network adapter information
            ;;
        4)
            echo "Exiting the menu system. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    # Add a newline for better readability
    echo
done
