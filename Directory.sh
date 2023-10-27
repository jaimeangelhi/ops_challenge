#!/bin/bash

# Script Name:                  Directory
# Author:                       Jai.me.angel.hi
# Date of latest revision:      10/26/2023
# Purpose:                      Create an array directory

# Declaration of variables

dirs=( dir1 dir2 dir3 dir4 )
# Declaration of functions

directory=() {
    mkdir $dirs
}

# Main
directory
touch "$dirs/textfile.txt"

# End
