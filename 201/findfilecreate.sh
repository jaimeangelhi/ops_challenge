#!/bin/bash

# Script Name:                  findfilecreate.sh
# Author:                       jai.me.angel.hi
# Date of latest revision:      10/30/2023
# Purpose:                      detects if file/directory exists, creates it if it does not exist.
# Additional sources            Class Repo on Github demo (https://github.com/codefellows/seattle-ops-201d14/blob/main/class-06/demo/demo.sh)


# Declaration of variables

file_list=("helloworld.sh" "findfilecreate.sh" "array.sh" "challenge03.sh" "printlogin.sh" "ops_challenge" "ops-reading-notes")

# Declaration of functions

is_item_in_list() {
    search_item="$1"
    for item in "${file_list[@]}"; do
        if [ "$item" == "$search_item"]; then
        return 0
        fi
    done
    return 1
}

while true; do
    read -p "Enter an item to check if it's on your file or directory list (or type 'done' to finish)" item to check

    if [ "$item_to_check" = "done" ]; then
        done
    fi

if is_item_in_list "$item_to_check"; then
    echo "Item '$item_to_check' is already on your file or directory list."
else
    read -p "'$item_to_check' is not on your list, do you want to add it? (yes/no)" add_item
    if [ "$add_item" = "yes" ]; then
        file_list+=("$item_to_check")
        echo "'$item_to_check' added to your file or directory list."

    else
        echo "'$item_to_check' is not on your file or directory list."
    fi
    done
fi
done 
    read -p "Are you ready to see your completed file or directory list? (yes/no)" show_list
        if [ "$show_list" = "yes" ]; then
            echo "Your completed file list: "
            echo "${file_list[@]}"
        else
            echo "Ok, you can check your list later."
        fi
# Main

# End

