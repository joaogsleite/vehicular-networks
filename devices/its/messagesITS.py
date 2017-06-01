import time

from shared.communication import send
from shared.security.rsa import cipher

def its2rsu(car, feedback):
    print 'sending msg its2rsu'
    feedback = cipher(feedback)
    send({
        'type':     5,
        'itsID':    "fc02::1001",
        'carID':    car,
        'feedback': feedback,
        'time':     int(time.time())
    }, 'fc01::101')
