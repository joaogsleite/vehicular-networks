import json
import socket

from gps import getLocation
from utils import getMyID, getDriverState
from steering import getDirection
from security import decipher, cipher

socket_send = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
port = 4173

def message_1():

    msg = {}
    msg['type'] = 1
    msg['carID'] = getMyID()
    msg['location'] = getLocation()
    msg['driverState'] = getDriverState()
    socket_send.sendto(json.dump(msg), ("FF02::1",port))

def message_2():

    msg = {}
    msg['type'] = 2
    msg['carID'] = getMyID()
    msg['location'] = getLocation()
    msg['driverState'] = getDriverState()
    data = {}
    ######
    # SENSORES
    ######
    msg['controllers'] = cipher(json.dump(data))
    socket_send.sendto(json.dump(msg), ("FF02::1",port))

def message_3(car):

    msg = {}
    msg['type'] = 3
    msg['rsuID'] = getMyID()
    msg['car_cao'] = car
    socket_send.sendto(json.dump(msg), ("fd87:9ef2:9e19:34e1:0:0:0:100",port))
    #fd87:9ef2:9e19:34e1:0:0:0:100 e o endereco do centerITS(unico)

def message_4(rsu, feedback, car):

    feedback = "Pare imediatamente"
    msg = {}
    msg['type'] = 4
    msg['centerITS'] = getMyID()
    msg['rsuID'] = rsu
    msg['feedback'] = feedback
    msg['carID'] = car
    socket_send.sendto(json.dump(msg), ("FF02::1",port))

def message_5(cars):

    msg = {}
    msg['type'] = 5
    msg['rsuID'] = getMyID()
    msg['cars'] = cars
    #car_cao = {}
    #car_cao['carID'] = carID
    #car_cao['location'] = getLocation()
    #car_cao['driverState'] = driverState
    #msg['cars'].append(car_cao)
    socket_send.sendto(json.dump(msg), ("FF02::1",port))
