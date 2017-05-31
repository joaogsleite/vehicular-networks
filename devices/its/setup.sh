#!/bin/bash

# Configuration
its_number="1001"


# NTP Server
sudo chmod 777 /etc/ntp-restrict.conf
sudo cp /etc/ntp-restrict.conf /etc/ntp-restrict.conf.old
cat > /etc/ntp-restrict.conf <<- ENDCONF

# Access restrictions documented in ntp.conf(5) and
# http://support.ntp.org/bin/view/Support/AccessRestrictions
# Limit network machines to time queries only

restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery

# localhost is unrestricted
restrict 127.0.0.1
restrict -6 ::1

# RV
restrict -6 fc02::/64

includefile /private/etc/ntp.conf
includefile /private/etc/ntp_opendirectory.conf

ENDCONF

# Run program
# =========================
python /home/pi/rv-project/devices/its/main.py &
