#!/bin/bash


# Configuration
rsu_number="101"


# Ad-hoc setup
# =========================
sudo cp /etc/network/interfaces /etc/network/interfaces.old
cat > /etc/network/interfaces <<- ENDINT

auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
iface eth0 inet6 static
    address fc02::101
    netmask 64

auto wlan0
iface wlan0 inet6 static
     address fc01::101
     netmask 64
     wireless-channel 6
     wireless-essid VehicularNet
     wireless-mode ad-hoc

ENDINT
sudo ifdown eth0
sudo ifup eth0
sudo ifdown wlan0
sudo ifup wlan0


# NTP
sudo chmod 777 /etc/ntp.conf
sudo cp /etc/ntp.conf /etc/ntp.conf.old
cat > /etc/ntp.conf <<- ENDCONF

server fc02::1001

ENDCONF



# Install dependencies
# =========================
sudo apt-get update


# Run program
# =========================
sudo service ntp stop
sudo ntpdate fc02::1001

PYTHONPATH="/home/pi/rv-project" python /home/pi/rv-project/devices/rsu/main.py "fc02::101"

