#!/bin/bash


# Configuration
rsu_number="0:0:0:1"


# Ad-hoc setup
# =========================
cp /etc/network/interfaces /etc/network/interfaces.old

cat > /etc/network/interfaces <<- ENDINT
auto wlan0
iface wlan0 inet6 static
     address fd87:9ef2:9e19:34e1:$rsu_number
     netmask 64
     wireless-channel 6
     wireless-essid VehicularNet
     wireless-mode ad-hoc
ENDINT
sudo ifdown wlan0
sudo ifup wlan0


# Install dependencies
# =========================
sudo apt-get update


# Setup startup
# =========================
cp /etc/rc.local /etc/rc.local.old

cat > /etc/rc.local <<- ENDRC

python /home/pi/rv-project/devices/rsu/main.py &

ENDRC
