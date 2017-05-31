import socket
import json
from time import time

PORT = 4173

session = None

def setup():
    global session
    print "creating socket..."
    session = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)


def server_setup():
    global session
    print "creating socket..."
    session = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    session.bind(('', PORT))


def send(msg, ip):
    if ip == "all":
        ip = "ff02::1"
    msg = json.dumps(msg)
    print msg
    try:
        session.sendto(msg, (ip, PORT))
    except:
        print 'error sending message'

def receive():
    data, address = session.recvfrom(1024)
    print 'received message: '+data
    data = json.loads(data)
    if int(time()) - int(data['time']) > 60:
        return None
    else:
        return data


def shutdown():
    global session
    print 'closing socket...'
    try:
        session.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Close socket'
