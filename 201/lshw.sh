#!/bin/bash

# Script Name:                  lshw
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/1/2023
# Purpose:                      Displays sys info to screen about Computer Name, CPU, RAM, DISPLAY ADAPTER, and NETWORK ADAPTER
# Additional Sources:           Class Repo GitHub; Class review Demo - Roger Huba, Marcus Nogueira, Ian Bennett


# Declaration of variables


# Declaration of functions


# Main
figlet "jaha"
echo ""
echo "Evaluating this computer..."
echo -e "Computer Name:\n\n "$(lshw | grep "" -m1)
echo -e "CPU:\n\n "$(lshw | grep "*-cpu" -A 5)
echo -e "RAM:\n\n "$(lshw | grep "*-memory" -A 3)
echo -e "Display Adapter:\n\n "$(lshw | grep "*-display" -A 10)
echo -e "Network Adapter:\n\n "$(lshw | grep "*-network" -A 15)
echo "Evaluation complete."


# End
