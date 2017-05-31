
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
    to_add = True
    for item in cars:
        if car['carID'] == item['carID']:
            to_add = False
            item['location'] = car['location']
            item['date'] = int(time.time())
            break

    if to_add:
        cars.append({
            'carID'     : car['carID'],
            'location'  : car['location'],
            'date'      : int(time.time()),
        })

