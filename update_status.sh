#!/bin/sh
#
# Update Script for SpaceAPI - https://github.com/openlab-aux/spaceapi
# You obviously need to change the token and the WLAN Interface(s).

count=$( (iwinfo wlan0-1 assoclist; iwinfo wlan1 assoclist) | grep SNR | wc -l)
echo $count
wget -q "http://api.openlab-augsburg.de/spacecgi.py?token=lolnope&update_device_count=$count" -O /dev/null
