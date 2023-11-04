# Script Name:                  challenge10.ps1
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/3/2023
# Purpose:                      Create a Powershell script that performs these operations on separate lines.
# Additional sources            ChatGPT (https://chat.openai.com/share/49cf46e2-4677-4c62-8028-9b6a4596126d)



# Print all active processes ordered by highest CPU time consumption
Get-Process | Sort-Object CPU -Descending | Format-Table Name, CPU -AutoSize   # This line retrieves a list of all running processes, sorts them by CPU usage in descending order, and then displays their names and CPU usage in a table format.

# Print all active processes ordered by highest Process Identification Number
Get-Process | Sort-Object ID -Descending | Format-Table Name, ID -AutoSize  # Retrieves all processes and sorts them by their Process Identification Numbers (PIDs) in descending order and displays their names and PIDs in a table.

# Print the top five active processes ordered by highest Working Set (WS(K))
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5 | Format-Table Name, WorkingSet -AutoSize #  Retrieves all processes, sorts them by their memory usage (Working Set) in descending order, selects the top 5 processes, and displays their names and memory usage in a table.

# Start a browser process (Google Chrome) and open https://owasp.org/www-project-top-ten/
Start-Process "chrome" "https://owasp.org/www-project-top-ten/"  #  Opens the Google Chrome browser and navigates to the specified URL (OWASP's Top Ten project page).

# Start Notepad ten times using a for loop
for ($i = 1; $i -le 10; $i++) {   # Using a loop, this line starts the Notepad application ten times.
    Start-Process "notepad"   # Starts the Notepad application
}    # Closes the loop

# Close all instances of Notepad
Get-Process "notepad" | ForEach-Object { $_.CloseMainWindow() }   # It retrieves all running instances of Notepad and attempts to close them using their main window.

# Kill a process (Google Chrome) by its Process Identification Number
$chromeProcess = Get-Process "chrome" | Select-Object -First 1  # Retrieves the first running instance of Google Chrome and stores it in a variable.
if ($chromeProcess -ne $null) {   # Checks if the Chrome process exists (is not null) 

    Stop-Process -Id $chromeProcess.Id   # if so, it forcefully terminates it using its Process Identification Number (PID). Be cautious with this step as it forcefully closes Chrome.
}     # Closes the loop
