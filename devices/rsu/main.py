import signal
import sys

import cars
from threading import Thread
from time import sleep

import shared.communication as communication
import messagesRSU as messages

running = False
MYIP = str(sys.argv[1])

def run_in_background():
    while running:
        messages.rsu2cars(myip)


def waiting_msgs():
    while running:
        msg = communication.receive()
        if msg == None:
            print "Time exceeded"
        elif msg['type'] == 2:
            cars.add(msg)
            if msg['state'] == 'danger':
                messages.rsu2its(msg['carID'], msg['state'], msg['sensors'], MYIP)
        elif msg['type'] == 5:
            messages.rsu2car(msg['feedback'], msg['carID'], MYIP)


if __name__ == "__main__":

    # setup messages module
    communication.setup()

    # decision block running
    running = True

    # waiting messages
    thread1 = Thread(target=waiting_msgs(), args=())
    thread1.start()

    thread2 = Thread(target=run_in_background(), args=())
    thread2.start()


def signal_handler(signal, frame):
    global running
    running = False
    communication.shutdown()

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
