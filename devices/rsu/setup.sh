#!/bin/bash


# Configuration
rsu_number="1"


# Ad-hoc setup
# =========================
#cp /etc/network/interfaces /etc/network/interfaces.old

cat > /etc/network/interfaces <<- ENDINT

auto eth0
iface eth0 inet6 static
    address fd87:9ef2:9e19:34e2:0:0:0:1
    netmask 64
ENDINT
sudo ifdown eth0
sudo ifup eth0

#cat > /etc/network/interfaces <<- ENDINT
#auto wlan0
#iface wlan0 inet6 static
#     address fd87:9ef2:9e19:34e1:$rsu_number
#     netmask 64
#     wireless-channel 6
#     wireless-essid VehicularNet
#     wireless-mode ad-hoc
#ENDINT
#sudo ifdown wlan0
#sudo ifup wlan0


# Install dependencies
# =========================
#sudo apt-get update


# Setup startup
# =========================
#cp /etc/rc.local /etc/rc.local.old

#cat > /etc/rc.local <<- ENDRC

#exec 2> /tmp/rc.local.log       # send stderr from rc.local to a log file
#exec 1>&2                       # send stdout to the same log file
#set -x                          # tell sh to display commands before execution
PYTHONPATH="/home/pi/rv-project" python /home/pi/rv-project/devices/rsu/main.py

ENDRC
