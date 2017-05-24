#!/bin/bash


# Configuration
car_number="0:0:0:1"


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


# Install dependencies
# =========================
sudo apt-get update
sudo apt-get install jstest-gtk #steering
sudo apt-get install pi-bluetooth libbluetooth-dev python-bluetooth #bluetooth
sudo apt-get install bluetooth bluez python-bluez #bluetooth
sudo apt-get install build-essential python-dev python-smbus #breathlyzer


# Setup startup
# =========================
cp /etc/rc.local /etc/rc.local.old

cat > /etc/rc.local <<- ENDRC

python /home/pi/rv-project/devices/car/main.py &

ENDRC
