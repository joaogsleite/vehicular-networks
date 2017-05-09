import socket

driverState = 'normal'
def getMyID():
    car = socket.gethostname()
    carID = car.split("fd87:9ef2:9e19:34e1:",2)[1]
    return carID

def updateDriverState():
    global driverState
    return driverState

def getDriverState():
    return driverState
