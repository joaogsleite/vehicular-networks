
import signal
from threading import Thread
from time import sleep
import sys

import devices.car.controllers.nearby as nearby
import devices.car.components.car.alerts as alerts
import devices.car.components.main as components
import shared.communication as communication
import shared.messages as messages

running = False
thread1 = None
thread2 = None


def sending_msgs():
    global running
    while running:
        messages.car2car()
        messages.car2rsu()
        sleep(5)


def waiting_msgs():
    print
    global running
    while running:
        try:
            msg = communication.receive()
            if msg is not None:
                print "Time exceeded"
            elif msg['type'] == 3:
                nearby.add(msg)
            elif msg['type'] == 6:
                for car in msg['cars']:
                    nearby.add(car)
        except:
            print "Error receiving msg"


if __name__ == "__main__":

    # start car components (reading values)
    if sys.argv[0] == 'primary':
        components.start()
    else:
        alerts.init()

    # setup messages module
    communication.setup()

    # decision block running
    running = True
    thread1 = Thread(target=sending_msgs, args=())
    thread1.start()

    # waiting messages
    thread2 = Thread(target=waiting_msgs, args=())
    thread2.start()


def signal_handler(signal, frame):
    print "Closing program..."

    global running
    global thread1
    global thread2

    running = False


    print "Stop sensors updates..."
    components.stop()

    print "Closing communication threads..."
    thread1.join()
    communication.shutdown()
    thread2.join()


signal.signal(signal.SIGINT, signal_handler)
signal.pause()
