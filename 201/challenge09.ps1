# Script Name:                  challenge09.ps1
# Author:                       jai.me.angel.hi
# Date of latest revision:      11/2/2023
# Purpose:                      To display various scripts and run individually
# Additional sources            ChatGPT (https://chat.openai.com/share/2b98d5e9-fb46-44b3-9696-a7544cdc46ef)

# Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt
Get-EventLog -LogName System -After (Get-Date).AddDays(-1) | Format-List | Out-File "$env:USERPROFILE\Desktop\last_24.txt"

# Output all “error” type events from the System event log to a file on your desktop named errors.txt
Get-EventLog -LogName System -EntryType Error | Format-List | Out-File "$env:USERPROFILE\Desktop\errors.txt"

# Print to the screen all events with ID of 16 from the System event log
Get-EventLog -LogName System -InstanceId 16 | Format-Table -AutoSize

# Print to the screen the most recent 20 entries from the System event log
Get-EventLog -LogName System -Newest 20 | Format-Table -AutoSize

# Print to the screen all sources of the 500 most recent entries in the System event log
Get-EventLog -LogName System -Newest 500 | Select-Object -Property Source | Format-Table -AutoSize





