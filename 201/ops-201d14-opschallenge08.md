@echo off           # turns off print action of the "echo" command, so all scripts execute without displaying each command
setlocal enabledelayedexpansion          # enables delayed variable expansion, which is needed for the script to work with variable inside loops and conditional statements.

set /p sourcePath=Enter the source folder path:          # prompts user to input source folder path, storing the entered value in the 'sourcePath' variable

set /p destinationPath=Enter the destination folder path:          # prompts user to input destination folder path, the entered value is stored in 'destinationPath' variable.

if not exist "!sourcePath!\" (          # checks if specified source folder exists 
    echo Error: Source folder does not exist.          # if not, will display error message          
    goto :eof          # exits the script with 'goto :eof'
)          # closes the argument

if not exist "!destinationPath!\" (           # checks if specified destination folder exists
    echo Error: Destination folder does not exist.          # if not, will display error message
    goto :eof          # exits the script with 'goto :eof'
)          # closes the argument

robocopy "!sourcePath!" "!destinationPath!" /E          # uses the Robocopy command to copy source folder contents to destination folder. '/E' flag will copy subdirectories, as well as empty ones.

if errorlevel 8 (          # checks the error level returned by Robocopy command, if 8 or more it indicates Robocopy encountered errors during copy operation.
    echo Error: ROBOCOPY encountered errors during the copy operation.          # if errors occur during operation, displays error message
) else (          # if no errors occurred, then this argument will populate to indicate successful copy operation
    echo Copy operation completed successfully.          # if no errors occurred, then this message will display to indicate successful copy operation
)          # closes the argument

:end          #defines endpoint of the script
endlocal          # ends the local environment esetablished by 'setlocal' and restores the previous environment

additional sources: ChatGPT (https://chat.openai.com/share/7483ca4a-66ab-460c-91ee-29e4bccecfc5)
