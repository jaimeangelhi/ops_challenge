# Assign Static IP and DNS
$ipAddress = "192.168.100.111" # Change to your desired IP
$subnetMask = "255.255.255.0" # Change to your subnet mask
$gateway = "192.168.100.1" # Change to your gateway
$dns = "192.168.100.123" # Change to your DNS server IP

New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress $ipAddress -PrefixLength 24 -DefaultGateway $gateway
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses $dns

# Rename the Server
$newName = "tikidemo" # Change to your desired server name
Rename-Computer -NewName $newName
Restart-Computer -Force

# Install AD-Domain-Services
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Import-Module ADDSDeployment

# Create AD Forest, OUs, and Users
$domainName = "mecatech.com" # Change to your desired domain name
$adminPassword = ConvertTo-SecureString "P@ssword123" -AsPlainText -Force # Change to your desired password
Install-ADDSForest -DomainName $domainName -SafeModeAdministratorPassword $adminPassword
# Note: Script will reboot the server and continue

# Additional OU and User Creation scripts go here

# Configure as DNS Server and Domain Controller
# Additional configuration scripts go here

# Integration into Existing Network
# Scripts or commands specific to your network infrastructure
