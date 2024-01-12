# Sources: ChatGPT (https://chat.openai.com/share/8381a2a1-9b01-470e-ace5-b17901006ff8)


# CIS Microsoft Windows Server 2019 Benchmark Automation Script

# Ensure you have the necessary privileges to execute these changes
# Run PowerShell as an Administrator

# 1.1.5 (L1) Configure 'Password must meet complexity requirements'
# Enabling Password Complexity
$PasswordComplexity = 1 # 1 to enable, 0 to disable
$secpolPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa"
Set-ItemProperty -Path $secpolPath -Name "PasswordComplexity" -Value $PasswordComplexity

# 18.4.3 (L1) Disable SMB v1
# Disable SMB v1 protocol
Disable-WindowsOptionalFeature -Online -FeatureName smb1protocol -NoRestart

# Output the settings to the console for verification
Write-Host "Password must meet complexity requirements policy is set to $PasswordComplexity"
Write-Host "SMB v1 protocol has been disabled"

# Reminder to restart the system if necessary
Write-Host "Remember to restart the system for the changes to take full effect"
