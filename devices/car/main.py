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
pre_test = False
thread1 = None
thread2 = None
MYIP = None


def sending_msgs():
    global running
    global MYIP
    while running:
        print 'sending messages...'
        messages.car2car(MYIP)
        messages.car2rsu(MYIP)
        sleep(5)


def waiting_msgs():
    global running
    global pre_test

    while pre_test:
        alerts.blow(True)
        for i in range(20):
            breathalyzer.update()

        if not breathalyzer.danger():
            pre_test = False
            alerts.blow(False)

    while running:
        try:
            print 'waiting for messages...'
            msg = communication.receive()
            print 'new message received: ' + msg
            if msg is not None:
                print "Time exceeded"
            elif msg['type'] == 3:
                nearby.add(msg)
            elif msg['type'] == 6:
                for car in msg['cars']:
                    print 'new nearby car'
                    nearby.add(car)
        except:
            print "Error receiving msg"


if __name__ == "__main__":

    MYIP = sys.argv[1]
    # start car components (reading values)
    if sys.argv[2] == 'primary':
        print 'PRIMARY CAR'
        if sys.argv[3] is not None:
            components.mock_gsp = True
        pre_test = True
        components.start()
    else:
        print 'SECONDARY CAR'
        pre_test = False
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
