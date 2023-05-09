#!/snap/bin/pwsh

&"$PSScriptroot\configure_powershell.ps1"

$theOrg = Get-IntersightOrganizationOrganization -Name CLUS

$theCLUStag = Initialize-IntersightMoTag -Key "CLUS2023" -Value "Devnet-1061"
$theLanguagetag = Initialize-IntersightMoTag -Key "Language" -Value "Powershell"

New-IntersightNtpPolicy `
    -Name "powershell" `
    -Description "This is an NTP policy created with Powershell" `
    -Organization $theOrg `
    -Enabled $true `
    -NtpServers @("1.1.1.1", "2.2.2.2") `
    -Tags @($theCLUStag, $theLanguagetag) `
    -Timezone AmericaPhoenix
