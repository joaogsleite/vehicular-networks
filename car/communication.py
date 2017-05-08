import signal
import sys

import socket
import time
import threading

port=4173
running = True

s_recv = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s_send = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

def recv():
    s_recv.bind(('::',port))
    while running:
        print "receiving..."
        data, address = s_recv.recvfrom(10)
        print "received:", data

def send():
    while running:
        print "sending..."
        print running
        s_send.sendto("I'm alive", ("FF02::1",port))
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
        s_recv.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Socket_receive closed'

    try:
        s_send.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Socket_send closed'

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
