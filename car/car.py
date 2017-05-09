import json
import socket

from alert import alertLedReceiveDanger, alertLedReceiveNormal

socket_receive = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 4173

rsu_messages = []

def received(message):
    socket_receive.bind(('::',port))
    while True:
        data, address = s_recv.recvfrom(1024)
        msg = json.loads(data)
        if msg['type'] == 1:
            if msg['driverState'] != "normal":
                alertLedReceiveDanger()
            else:
                alertLedReceiveNormal()
        else if msg['type'] == 5:
            rsu_messages.append(msg)
            print rsu_messages
