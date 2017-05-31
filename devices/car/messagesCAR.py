
import devices.car.components.car.gps as location
import devices.car.controllers.driver as driver
import time
import json

from shared.communication import send
from shared.security.rsa import cipher


def car2car(myip):
    print 'sending msg v2v: driver state'
    send({
        'type':     1,
        'carID':    myip,
        'location': location.get(),
        'state':    driver.state(),
        'time':     int(time.time())
    }, "all")


def car2rsu(myip):
    print 'sending msg v2i: sensors data'
    sensors = json.dumps(driver.sensors())
    sensors = cipher(sensors)
    send({
        'type':     2,
        'carID':    myip,
        'location': location.get(),
        'state':    driver.state(),
        'sensors':  sensors,
        'time':     int(time.time())
    }, "all")
