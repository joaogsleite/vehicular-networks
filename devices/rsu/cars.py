
from datetime import datetime, timedelta

DELTA = timedelta(0, 1*60)

cars = []


def list():
    global cars
    for i, car in enumerate(cars):
        if datetime.now() - car['date'] < DELTA:
            cars.pop(i)

    return cars


def add(car):
    global cars
    cars.append({
        'carID'     : car['carID'],
        'location'  : car['location'],
        'date'      : datetime.now(),
    })
