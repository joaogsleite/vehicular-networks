
import threading

from devices.car.components.car import gps, steering
from sensors import mindwave, fitbit, breathalyzer

running = False


def update_in_background():

    while running:
        print 'Updating values from car components'

        gps.update()
        steering.update()

        mindwave.update()
        fitbit.update()
        breathalyzer.update()


def stop():
    global running
    running = False


def start():
    global running
    running = True
    thread = threading.Thread(target=update_in_background(), args=())
    thread.start()
