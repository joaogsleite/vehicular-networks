
import devices.car.components.car.gps as location
import devices.car.controllers.driver as driver
import devices.rsu.cars as cars
import time
import json

from communication import my_id, send
from security.rsa import cipher


def car2car():
    print 'sending msg v2v: driver state'
    send({
        'type':     1,
        'carID':    my_id(),
        'location': location.get(),
        'state':    driver.state(),
        'time':     int(time.time())
    })


def car2rsu():
    print 'sending msg v2i: sensors data'
    sensors = json.dumps(driver.sensors())
    sensors = cipher(sensors)
    send({
        'type':     2,
        'carID':    my_id(),
        'location': location.get(),
        'state':    driver.state(),
        'sensors':  sensors,
        'time':     int(time.time())
    })


def rsu2cars():
    print 'sending msg i2v: other cars'
    send({
        'type':     3,
        'rsuID':    my_id(),
        'cars':     cars.list(),
        'time':     int(time.time())
    })


def rsu2its(car, state, sensors):
    print 'sending msg i2c: sensors data'
    send({
        'type':     4,
        'rsuID':    my_id(),
        'carID':    car,
        'state':    state,
        'sensors':  sensors,
        'time':     int(time.time())
    })


def its2rsu(car, feedback):
    print 'sending msg c2i: feedback'
    feedback = cipher(feedback)
    send({
        'type':     5,
        'itsID':    my_id(),
        'carID':    car,
        'feedback': feedback,
        'time':     int(time.time())
    })


def rsu2car(feedback):
    print 'sending msg i2v: feedback'
    send({
        'type':     6,
        'rsuID':    my_id(),
        'feedback': feedback,
        'time':     int(time.time())
    })
