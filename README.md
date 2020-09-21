# EnumerationTools
## Tools for recon on domains and servers

### Get-HostInfo
A very useful rubber-ducky esque script that swipes a bunch of host info. Currently, it returns:
*	WiFi Passwords in plaintext
*	Drives, available space and whether or not they're encrypted
*	TCP connections
*	Other misc host info

# Got some lines from: https://chrishales.wordpress.com/2018/01/03/powershell-password-one-liners/

### SubScanner 
Scan a domain for the instance of up to 10,000 subdomains and return all of the connected domains

#### Dependencies
*	requests

Domains from: https://github.com/danielmiessler/RobotsDisallowed


### BlackListCheck
Checks a list of IP's against a variety of blacklists, then uploads results into a pretty json file. 
Working on adding more blacklists to check against, but for now it checks AbuseIPDB and SpamCop.
There is also a section for VirusTotal that is being worked on ATM, but you need a premo API key for that.


### BannerYank
#### About
Banner Yank is a banner grab attack aggregator WIP.
As of now, BannerYank performs the following recon attacks:
*	Telnet
*	Wget
*	Curl
*	Nmap
*	Dmitry
*	WhatWeb

#### Dependencies
All of the tools mentioned in the above section

#### TO DO LIST
My goals for the future of this application are to build on the potential possibilities it provides as a
vulnerability scanner. This includes:
*	Adding more tools
*	Increasing the verbosity of the program
*	Being able to spot and report on common vulnerabilities found during banner grabs
		*	And creating a system for reporting these vulnerabilites
*	Overall just making the application more useful

#### Notes
As of now, the application operates as a simple OSINT tool. Use it as a stoneturner, it will help when you're
unsure if you've checked everything.

Want to get involved? Help? Got a tool to suggest? Just want to make a comment?
Please contact me here: *baconmcdrums@gmail.com*

Big thank you to this article:
https://securitytrails.com/blog/banner-grabbing



# constantly a w.i.p
