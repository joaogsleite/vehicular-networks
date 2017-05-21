
import socket
import json

ALL = "FF02::1"
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
    hostname = socket.gethostname()
    return hostname.split("fd87:9ef2:9e19:34e1:", 2)[1]


def receive():
    data, address = session.recvfrom(1024)
    return json.loads(data)


def shutdown():
    try:
        session.shutdown(socket.SHUT_RDWR)
    except socket.error:
        print 'Error closing socket!'
