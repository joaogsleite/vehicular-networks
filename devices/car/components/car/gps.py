
latitude = 0
longitude = 0
altitude = 0


def get():
    # return last location value read from gps
    global latitude
    global longitude
    global altitude
    return {
        'latitude': latitude,
        'longitude': longitude,
        'altitude': altitude,
    }


def update():
    # read real value from gps
    global latitude
    global longitude
    global altitude

    with open('/dev/ttyACM0', 'r') as f:
        for line in iter(f.readline, ''):
            if line.split(',')[0] == '$GPGGA':
                lat_deg = float(line.split(',')[2]) // 100
                lat_min = float(line.split(',')[2]) % 100
                lat_sec = float(line.split(',')[2]) % 1
                lat_fac = 1
                if line.split(',')[3] == 'S':
                    lat_fac = -1

                lon_deg = float(line.split(',')[4]) // 100
                lon_min = float(line.split(',')[4]) % 100
                lon_sec = float(line.split(',')[4]) % 1
                lon_fac = 1
                if line.split(',')[5] == 'W':
                    lon_fac = -1

                latitude = lat_fac * (lat_deg + ((lat_min + (lat_sec / 60)) / 60))
                longitude = lon_fac * (lon_deg + ((lon_min + (lon_sec / 60)) / 60))
                altitude = float(line.split(',')[9])


def read():
    # read real value from gps
    global latitude
    global longitude
    global altitude

    with open('/home/pi/rv-project/devices/car/components/car/gps.txt', 'r') as f:
        for line in iter(f.readline, ''):
            seconds = line.split(',')[0]
            latitude = line.split(',')[1]
            longitude = line.split(',')[2]
            altitude = line.split(',')[3]


def set(lat, lng, alt):
    # set value for demonstration
    global latitude
    global longitude
    global altitude
    latitude = lat
    longitude = lng
    altitude = alt
