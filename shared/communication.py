
import socket
import json
from time import time

ALL = "FF02::1"
MYIP = "fd87:9ef2:9e19:34e1:0:0:0:1"
PORT = 4173

session = None


def setup():
    global session
    session = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)


def send(msg):
    msg = json.dumps(msg)
    try:
        session.sendto(msg, (ALL, PORT))
    except socket.error, socket.timeout:
        print 'error sending message'




def my_id():
    #hostname = socket.gethostname()
    #hostname.split("fd87:9ef2:9e19:34e1:", 2)[1]
    return MYIP


def receive():
    data, address = session.recvfrom(1024)
    data = json.loads(data)
    if int(time()) - int(data['time']) > 60:
        return None
    else:
        return data


def shutdown():
    global session
    try:
        session.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Close socket'
