import json
import socket
import time
from security import decipher, cipher

socket_receive = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 4173
nearby_cars = []
centerITS_feedback = []
var_time = 400

def getTime():
    return time.asctime(time.localtime(time.time()))

def checkTimes():
    while i < len(nearby_cars):
        elapsed = (getTime() - msg['time'])
        if elapsed > var_time:
            nearby_cars.pop(i)
        else:
            continue

def received(message):
    socket_receive.bind(('::',port))
    while True:
        data, address = s_recv.recvfrom(1024)
        msg = json.loads(data)
        checkTimes()

        if msg['type'] == 2:
            new_msg = decipher(msg['controllers'])
            start_time = getTime()
            msg['controllers'] = new_msg
            msg['time'] = start_time
            nearby_cars.append(msg)
            print nearby_cars

        if msg['type'] == 4:
            centerITS_messages.append(msg)
            print centerITS_messages
        else:
            continue
