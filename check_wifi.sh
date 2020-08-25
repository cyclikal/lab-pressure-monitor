# Make this script executable (sudo chmod +x check_wifi.sh)
# Add the line below to the pi user's crontab (sudo crontab -e)
# */10 * * * * sudo /home/pi/check_wifi.sh


#!/bin/bash

GATEWAY=10.10.1.2

ping -c2 ${GATEWAY} > /dev/null

if [ $? = 0 ]
then
    sudo ifconfig wlan0 down
    sudo ifconfig wlan0 up
fi
