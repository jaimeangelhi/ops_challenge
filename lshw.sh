#!/bin/bash

# Script Name:                  lshw
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/1/2023
# Purpose:                      Displays sys info to screen about Computer Name, CPU, RAM, DISPLAY ADAPTER, and NETWORK ADAPTER
# Additional Sources:           Class Repo GitHub, Class review Demo - Roger Huba


# Declaration of variables


# Declaration of functions


# Main

echo "Evaluating this computer..."
echo "Computer Name: "$(lshw | grep "" -m1)
echo "CPU: "$(lshw | grep "*-cpu" -A 5)
echo "RAM: "$(lshw | grep "*-memory" -A 3)
echo "Display Adapter: "$(lshw | grep "*-display" -A 10)
echo "Network Adapter: "$(lshw | grep "*-network" -A 15)
echo "Evaluation complete."


# End
