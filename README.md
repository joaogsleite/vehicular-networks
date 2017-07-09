
# Vehicular Networks project

Vehicular ad hoc network project to monitor and share driver state

## Setup

#### Flash multiple raspberry pi 3 SD Cards

* Download Raspbian Lite

```
https://www.raspberrypi.org/downloads/raspbian/
```

* Flash micro SD Card

```
# check sdcard disk number
diskutil list

# unmount sdcard
diskutil unmountDisk /dev/diskn

# replace n with disk number
sudo dd bs=1m if=path_of_your_image.img of=/dev/rdiskn
```

* Enable SSH Access

```
touch /Volumes/boot/ssh
```


### SSH into flashed raspberry pi

* Plug in ethernet cable

* Locate `raspberrypi.local` domain

* SSH

```
$ ssh pi@raspberrypi.local
passwd: raspberry
```

* You can now copy ssh keys and alias


---


## Deploy code


### OBU

* Edit `deploy.sh` on this project's root folder

```
IP="<your-raspberry-ip>"
```

* Run script with args = CODE

* Code should be deployed to raspberry



## Create RSA keys for nodes encrypted communication (needed for sensors data sharing)

* Chosse a raspberry with code deployed

* Go to `shared/security`

* Run rsa.py

```
python rsa.py
```

* Copy generated `private.key` and `public.key` to other raspberries on the same folder



## Run project on each raspberry

* Edit `setup.sh` on each device folder to reflect choose ip address

* Run `setup.sh` on each device folder (OBU, RSU or Center-ITS)

> internet access is needed to install dependencies

    * You can share your laptop internet connection by ethernet to the raspberry pi

* Run last command in `setup.sh` to start project (python)
