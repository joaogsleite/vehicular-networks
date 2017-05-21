
import signal
from threading import Thread
from time import sleep

import devices.car.controllers.nearby as nearby

import devices.car.components.main as components
import shared.communication as communication
import shared.messages as messages

running = False


def run_in_background():
    while running:
        print 'decision block'
        messages.car2car()
        messages.car2rsu()
        sleep(5)


def waiting_msgs():
    while running:
        msg = communication.receive()
        if msg['type'] == 3:
            nearby.add(msg)
        if msg['type'] == 6:
            for car in msg['cars']:
                nearby.add(car)


if __name__ == "__main__":

    # start car components (reading values)
    components.start()

    # setup messages module
    communication.setup()

    # decision block running
    running = True
    thread1 = Thread(target=run_in_background(), args=())
    thread1.start()

    # waiting messages
    thread2 = Thread(target=waiting_msgs(), args=())
    thread2.start()


def signal_handler(signal, frame):
    global running
    running = False
    communication.shutdown()

signal.signal(signal.SIGINT, signal_handler)
signal.pause()






