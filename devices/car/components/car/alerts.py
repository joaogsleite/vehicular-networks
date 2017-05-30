
from datetime import datetime, timedelta
import threading
from time import sleep
import RPi.GPIO as GPIO

DELTA = timedelta(0, 1*60)
GPIO.setmode(GPIO.BCM)


class Alert:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.isActive = False
        self.running = True
        self.last = datetime.now()
        GPIO.setup(self.pin, GPIO.OUT)

    def active(self):
        print 'Alert: ' + self.name
        self.last = datetime.now()
        if not self.isActive:
            self.isActive = True
            GPIO.output(self.pin, True)
            thread = threading.Thread(target=self.reset, args=())
            thread.start()

    def shutdown(self):
        self.running = False

    def reset(self):
        while datetime.now() - self.last < DELTA and self.running:
            sleep(5)
        GPIO.output(self.pin, False)
        self.isActive = False


def init():
    global a1
    global a2
    global a3
    a1 = Alert(7, "blow")
    a2 = Alert(5, "driver is not well")
    a3 = Alert(6, "danger nearby")



def shutdown():
    global a1
    global a2
    global a3
    a1.shutdown()
    a2.shutdown()
    a3.shutdown()


def driver_not_well():
    global a2
    a2.active()


def nearby_danger():
    global a3
    a3.active()


def blow(ok):
    global a1
    if ok:
        a1.active()
    else:
        a1.shutdown()
