#!/bin/bash


# Configuration
its_number="0:0:0:1"


# Ad-hoc setup
# =========================
cp /etc/network/interfaces /etc/network/interfaces.old

cat > /etc/network/interfaces <<- ENDINT
auto wlan0
iface wlan0 inet6 static
     address fd87:9ef2:9e19:34e1:$its_number
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

exec 2> /tmp/rc.local.log       # send stderr from rc.local to a log file
exec 1>&2                       # send stdout to the same log file
set -x                          # tell sh to display commands before execution

cat > /etc/rc.local <<- ENDRC

python /home/pi/rv-project/devices/its/main.py &

ENDRC

sudo hciconfig hci0 piscan
