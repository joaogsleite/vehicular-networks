
import time

cars = []


def list():
    global cars
    for i, car in enumerate(cars):
        if int(time.time()) - int(car['date']) > 60:
            cars.pop(i)

    return cars


def add(car):
    global cars
    cars.append({
        'carID'     : car['carID'],
        'location'  : car['location'],
        'date'      : int(time.time()),
    })
