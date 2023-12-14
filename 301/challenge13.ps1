# Script Name:                  challenge13.ps1
# Author:                       jai.me.angel.hi
# Date of latest revision:      12/13/2023
# Purpose:                      Create a Powershell script that performs these operations on separate lines.
# Additional sources            ChatGPT

# Define user attributes
$FirstName = "Franz"
$LastName = "Ferdinand"
$Username = "ferdi"
$Title = "TPS Reporting Lead"
$Department = "TPS Department"
$Office = "Springfield, OR"
$Email = "ferdi@GlobeXpower.com"

# Set the password for the new user
$Password = "P@ssw0rd"  # Change this to a secure password

# Specify the OU where the user will be created
$UserOU = "OU=Users,DC=example,DC=com"  # Update with your actual AD structure

# Specify the OU where the group will be created
$GroupOU = "OU=Groups,DC=example,DC=com"  # Update with your actual AD structure

# Specify the parent OU where the new OU will be created
$ParentOU = "OU=NewOUs,DC=example,DC=com"  # Update with your actual AD structure

# Create the user
New-ADUser -SamAccountName $Username -UserPrincipalName "$Username@yourdomain.com" -GivenName $FirstName -Surname $LastName -Title $Title -Department $Department -Office $Office -EmailAddress $Email -AccountPassword (ConvertTo-SecureString -AsPlainText $Password -Force) -Enabled $true -Path $UserOU

# Create a new group
New-ADGroup -Name "TPSGroup" -GroupScope Global -GroupCategory Security -Path $GroupOU

# Create a new organizational unit (OU)
New-ADOrganizationalUnit -Name "TPS" -Path $ParentOU
