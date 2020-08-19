#!/bin/bash

#	This program is meant to be somewhat of a timesaver, as well as a stone turner.
#	If you're running this as a sysadmin, I probably don't need to tell you this, but most of these banners
#	can be changed to throw off anyone using any of these commands.
#
#	As stated in the help, this is a very noisey program. I'm working on a version for passive grabs, but until
#	that is done, know that this program will set off alarms on any competent IDS.
#	If you'd like to help or get involved with making this project better, or just have general recommendations, please email me at baconmcdrums@gmail.com. 
#	Be safe!

HOST_IP=$1
HOST_PORT=$2

echo "
 _____ _____ _____ _____ _____ _____    __ __ _____ _____ _____ 
| __  |  _  |   | |   | |   __| __  |  |  |  |  _  |   | |  |  |
| __ -|     | | | | | | |   __|    -|  |_   _|     | | | |    -|
|_____|__|__|_|___|_|___|_____|__|__|    |_| |__|__|_|___|__|__|

Version 1.0 // Updated August 3, 2020
contact: baconmcdrums@gmail.com
"

# Help Argument
if [[ $1 == 'help' ]]; then
	echo "
~ BannerYank is a banner attack command aggregator. 
~ It launches some very noisey attacks all at once and spits all the information back to you. 
~ Please keep this in mind if you're trying to work silently.
	
~ USAGE: banneryank [IP] [PORT]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	return 1
fi

if [[ -n $HOST_IP ]]; then
	printf "Beginning banner attack with host $HOST_IP "
else
	echo "BannerYank usage: banneryank [TARGET IP] [TARGET PORT]"	
	return 1
fi

if [[ -n $HOST_PORT ]]; then
	echo "and port $HOST_PORT."
else
	echo "BannerYank usage: banneryank [TARGET IP] [TARGET PORT]"	
	return 1
fi

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Telnet Scan"
#TELNET
telnet $HOST_IP $HOST_PORT


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Wget Scan"
#WGET
wget $HOST_IP -q -S


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Curl Scan"
#CURL
curl -s -I $HOST_IP | grep -e "Server: "


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Nmap Banner Scans"
nmap -sV --script=banner $HOST_IP
echo "Perform extra version scan on ALL ports with nmap? (y/n) ((SIGNIFICANTLY SLOWER)): "
#NMAP
while true;
do
	read -r -p "(y or n): " response
	if [[ $response =~ ^[yY]$ ]]
	then
		nmap -sV --version-intensity 5 $HOST_IP -p 0-65535
		break
	else
		break
	fi
done

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Netcat Scan"
nc -v $HOST_IP $HOST_PORT

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "DMitry"
echo "This tool is added for redundency in the case it catches something that nmap does not."
dmitry -bp $HOST_IP

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "WhatWeb Scan"
whatweb http://$HOST_IP
