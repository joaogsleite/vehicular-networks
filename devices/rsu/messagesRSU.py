import cars
import time
import json

from communication import send

def rsu2cars(myip):
    print 'sending msg i2v: other cars'
    send({
        'type':     3,
        'rsuID':    myip,
        'cars':     cars.list(),
        'time':     int(time.time())
    }, "all")


def rsu2its(car, state, sensors, myip):
    print 'sending msg i2c: sensors data'
    send({
        'type':     4,
        'rsuID':    myip,
        'carID':    car,
        'state':    state,
        'sensors':  sensors,
        'time':     int(time.time())
    }, "fc02::1")

def rsu2car(feedback, ip, myip):
    print 'sending msg i2v: feedback'
    send({
        'type':     6,
        'rsuID':    myip,
        'feedback': feedback,
        'time':     int(time.time())
    }, ip)
