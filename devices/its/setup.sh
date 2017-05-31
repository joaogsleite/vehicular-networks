#!/bin/bash

# Configuration
its_number="100"

# Ad-hoc setup
# =========================
#sudo cp /etc/network/interfaces /etc/network/interfaces.old
sudo chmod 777 /etc/network/interfaces
cat > /etc/network/interfaces <<- ENDINT

auto eth0
iface eth0 inet6 static
    address fc02::$its_number
    netmask 64
ENDINT

#sudo ifdown wlan0
#sudo ifup wlan0
sudo ifdown eth0
sudo ifup eth0

# Install dependencies
# =========================
#sudo apt-get update

# Setup startup
# =========================
sudo cp /etc/rc.local /etc/rc.local.old

exec 2> /tmp/rc.local.log       # send stderr from rc.local to a log file
exec 1>&2                       # send stdout to the same log file
set -x                          # tell sh to display commands before execution

cat > /etc/rc.local <<- ENDRC

python /home/pi/rv-project/devices/its/main.py &

#ENDRC
