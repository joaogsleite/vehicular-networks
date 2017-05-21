
from datetime import datetime, timedelta
from time import sleep
import RPi.GPIO as GPIO

DELTA = timedelta(0, 1*60)
GPIO.setmode(GPIO.BOARD)


class Alert:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.active = False
        self.last = datetime.now()
        GPIO.setup(self.pin, GPIO.OUT)

    def active(self):
        print 'Alert: ' + self.name
        self.last = datetime.now()
        if not self.active:
            self.active = True
            GPIO.output(self.pin, True)
            self.reset()

    def reset(self):
        while datetime.now() - self.last < DELTA:
            sleep(5)
        GPIO.output(self.pin, False)
        self.active = False


a2 = Alert(2, "driver is not well")
a3 = Alert(3, "danger nearby")


def driver_not_well():
    a2.active()


def nearby_danger():
    a3.active()