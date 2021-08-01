#!/bin/bash

# Move ssh to specified port, 
#	then redirect all port 22 traffc to honepot port (2222)

port=$1

echo "Changing ssh to port $port"

# Create backup
date_format=`date +%Y_%m_%d:%H:%M:%S`
cp /etc/ssh/sshd_config /etc/ssh/sshd_config_$date_format

semanage port -a -t ssh_port_t -p tcp $port

# Change sshd_config file to point ssh to your port
sed -i 's/#Port 22/Port $port/' /etc/ssh/sshd_config

# Add port to public zone, this redirects all port 22 traffic to honeypot port
firewall-cmd --add-port=$port/tcp --permanent
firewall-cmd --remove-service=ssh --permanent
firewall-cmd --zone=public --permanent --add-forward-port=port=22:proto=tcp:toport=2222
firewall-cmd --reload

systemctl restart sshd

# Grep netstat to confirm changes
netstat -tunl | grep $port
