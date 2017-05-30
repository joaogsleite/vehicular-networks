#!/bin/bash


# Configuration
car_number="0:0:0:1"



# Install dependencies
# =========================
sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y vim
sudo apt-get install -y python-pip

# security
sudo apt-get install -y build-essential python-dev
sudo pip install pycrypto


#steering
sudo apt-get install -y jstest-gtk

#bluetooth
sudo apt-get install -y pi-bluetooth libbluetooth-dev python-bluetooth
sudo apt-get install -y bluetooth bluez python-bluez

#breathlyzer
sudo apt-get install -y python-smbus
sudo pip install adafruit-mcp3008



# Setup startup
# =========================
cp /etc/rc.local /etc/rc.local.old

cat > /etc/rc.local <<- ENDRC

exec 2> /tmp/rc.local.log       # send stderr from rc.local to a log file
exec 1>&2                       # send stdout to the same log file
set -x                          # tell sh to display commands before execution

PYTHONPATH="/home/pi/rv-project" python /home/pi/rv-project/devices/car/main.py &

ENDRC



# Ad-hoc setup
# =========================
cp /etc/network/interfaces /etc/network/interfaces.old

cat > /etc/network/interfaces <<- ENDINT
auto wlan0
iface wlan0 inet6 static
     address fd87:9ef2:9e19:34e1:$car_number
     netmask 64
     wireless-channel 6
     wireless-essid VehicularNet
     wireless-mode ad-hoc
ENDINT
sudo ifdown wlan0
sudo ifup wlan0



# Project setup
# =========================

# bluetooth discover
sudo hciconfig hci0 piscan

# create keys for all hops
cd rv-project
python shared/security/rsa.py