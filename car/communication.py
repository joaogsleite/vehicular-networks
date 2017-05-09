import signal
import sys

import socket
import time
import threading
import json

from gps import getLocation

running = True

def recv():
    while running:
        print "receiving..."
        #data, address = s_recv.recvfrom(10)
        print "received:", data

def send():
    while running:
        print "sending..."
        #s_send.sendto("I'm alive", ("FF02::1",port))
        time.sleep(5)

thread_recv = threading.Thread(target = recv, args = ())
thread_recv.start()
thread_send = threading.Thread(target = send, args = ())
thread_send.start()


def signal_handler(signal, frame):
    print('Closing sockets...')

    global running
    global s_recv
    global s_send

    running = False

    try:
        socket_receive.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Socket_receive closed'

    try:
        socket_send.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Socket_send closed'

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
