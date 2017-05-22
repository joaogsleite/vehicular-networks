
import threading
from time import sleep

from devices.car.components.car import gps, steering
from sensors import mindwave, fitbit, breathalyzer

running = False


def run_in_background():

    mindwave.init()

    while running:
        print 'Updating values from car components'

        gps.update()
        steering.update()
        mindwave.update()
        fitbit.update()
        breathalyzer.update()

        sleep(1)


def stop():
    global running
    running = False


def start():
    global running
    running = True
    thread = threading.Thread(target=run_in_background(), args=())
    thread.start()
