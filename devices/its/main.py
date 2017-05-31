
import signal
from threading import Thread
from time import sleep

#from shared.security.rsa import decipher
import shared.communication as communication
#import shared.messages as messages

running = False
FEEDBACK = 'Para bebado!'


def waiting_msgs():
    while running:
        msg = communication.receive()
        print "Received"
        '''
        if msg is None:
            print "Time exceeded"
        elif msg['type'] == 4:
            sensors = decipher(msg['sensors'])
            print "Message received from car "+msg['carID']
            print "Sensors data: "+sensors
            messages.its2rsu(msg['carID'], FEEDBACK)
        '''
        sleep(5)

if __name__ == "__main__":

    # setup messages module
    communication.setup()

    # waiting messages
    thread2 = Thread(target=waiting_msgs(), args=())
    thread2.start()


def signal_handler(signal, frame):
    global running
    running = False
    communication.shutdown()

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
