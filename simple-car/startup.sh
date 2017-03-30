
# Configuration
car_number="0:0:0:2"



# Ad-hoc setup
# =========================
cp /etc/network/interfaces /etc/network/interfaces.old

cat > /etc/network/interfaces <<- ENDINT
auto wlan0
iface wlan0 inet static
     address "fd87:9ef2:9e19:34e1:$car_number"
     netmask 64
     wireless-channel 6
     wireless-essid AdHocNetwork
     wireless-mode ad-hoc
ENDINT
sudo ifdown wlan0
sudo ifup wlan0



# Install dependencies
# =========================
sudo apt-get install curl
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs



# Service start
# =========================
npm install
npm start
