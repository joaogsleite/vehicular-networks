
import signal
from threading import Thread
from time import sleep

import cars

import shared.communication as communication
import shared.messages as messages

running = False


def run_in_background():
    while running:
        print 'decision block'
        messages.rsu2cars()
        sleep(5)


def waiting_msgs():
    while running:
        msg = communication.receive()
        if msg['type'] == 2:
            cars.add(msg)
        if msg['type'] == 5:
            messages.rsu2car(msg['feedback'])


if __name__ == "__main__":

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



