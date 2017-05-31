#!/bin/bash


# Configuration
car_number="1"



# Install dependencies
# =========================
sudo apt-get update
sudo apt-get install -y git
sudo apt-get install -y vim
sudo apt-get install -y python-pip

# date sync
sudo apt-get install ntpdate

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



# Ad-hoc setup
# =========================
cp /etc/network/interfaces /etc/network/interfaces.old
sudo chmod 777 /etc/network/interfaces
cat > /etc/network/interfaces <<- ENDINT

auto lo
iface lo inet loopback
iface eth0 inet dhcp

auto wlan0
iface wlan0 inet6 static
     address fc01::$car_number
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



# Run project
# =========================
sudo service ntp stop
sudo ntpdate fc01::101

# primary
PYTHONPATH="/home/pi/rv-project" python /home/pi/rv-project/devices/car/main.py "fc01::1" "primary"

#secondary
PYTHONPATH="/home/pi/rv-project" python /home/pi/rv-project/devices/car/main.py "fc01::2" "secondary"


