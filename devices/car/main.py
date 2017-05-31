import signal
from threading import Thread
from time import sleep
import sys

import devices.car.controllers.nearby as nearby
import devices.car.components.sensors.breathalyzer as breathalyzer
import devices.car.components.car.alerts as alerts
import devices.car.components.main as components
import shared.communication as communication
import messagesCAR as messages

running = False
thread1 = None
thread2 = None
MYIP = None


def sending_msgs():
    global running
    global MYIP

    while running:
        while running and not components.pre_test:
            print 'sending messages...'
            messages.car2car(MYIP)
            messages.car2rsu(MYIP)
            sleep(5)
        sleep(1)


def waiting_msgs():
    global running

    while running:
        try:
            msg = communication.receive()
                if msg['carID'] == MYIP:
                    continue

            print 'new message received: ' + str(msg)


            if msg['type'] == 3:
                nearby.add(msg)
            elif msg['type'] == 6:
                for car in msg['cars']:
                    print 'new nearby car'
                    nearby.add(car)
        except Exception,e:
            print "Error receiving msg"
            print e


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


if __name__ == "__main__":

    MYIP = sys.argv[1]
    # start car components (reading values)
    if sys.argv[2] == 'primary':
        print 'PRIMARY CAR'
        try:
            if sys.argv[3] is not None:
                components.mock_gsp = True
                print ">>> gps simulation active"
        except:
            components.mock_gsp = False
            print ">>> no gps simulation"
        components.start()
    else:
        print 'SECONDARY CAR'
        components.pre_test = False
        print ">>> no sensors"
        alerts.init()

    # setup messages module
    print "binding sockets..."
    communication.setup()
    print "complete"

    # decision block running
    running = True
    thread1 = Thread(target=sending_msgs, args=())
    thread1.start()

    # waiting messages
    thread2 = Thread(target=waiting_msgs, args=())
    thread2.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
