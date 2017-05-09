import json
import socket

socket_receive = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 4173
rsu = []

def received(message):
    socket_receive.bind(('::',port))
    while True:
        data, address = s_recv.recvfrom(1024)
        msg = json.loads(data)

        if msg['type'] == 3:
            rsu.append(msg)
            print rsu
