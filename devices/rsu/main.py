import signal

import cars
from threading import Thread
from time import sleep

import shared.communication as communication
import messagesRSU as messages

running = False
MYIP = "fc02::1"
thread1 = None
thread2 = None


def run_in_background():
    global running
    global MYIP

    while running:
        messages.rsu2cars(myip)
        sleep(5)


def waiting_msgs():
    global running

    while running:
        print
        msg = communication.receive()
        if msg is None:
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
    thread1 = Thread(target=waiting_msgs, args=())
    thread1.start()

    thread2 = Thread(target=run_in_background, args=())
    thread2.start()


def signal_handler(signal, frame):
    global running
    running = False
    communication.shutdown()

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
