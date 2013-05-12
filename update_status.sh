#!/bin/sh
# 
# Update Script for SpaceAPI - https://github.com/openlab-aux/spaceapi
# You obviously need to change the token and the WLAN Interface.

count=$(iwinfo wlan0-1 associnfo | grep SNR | cut -d " " -f 1 | wc -l)
echo $count
wget "http://api.openlab-augsburg.de/spacecgi.py?token=lolnope&update_device_count=$count" -O /dev/null
