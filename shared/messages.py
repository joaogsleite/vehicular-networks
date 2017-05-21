
import devices.car.components.car.gps as location
import devices.car.controllers.driver as driver
import devices.rsu.cars as cars

from communication import my_id, send
from security.rsa import cipher


def car2car():
    send({
        'type':     1,
        'carID':    my_id(),
        'location': location.get(),
        'state':    driver.state(),
    })


def car2rsu():
    sensors = cipher(driver.sensors())
    send({
        'type':     2,
        'carID':    my_id(),
        'location': location.get(),
        'state':    driver.state(),
        'sensors':  sensors,
    })


def rsu2cars():
    send({
        'type':     3,
        'rsuID':    my_id(),
        'cars':     cars.list()
    })


def rsu2its(car, state, sensors):
    send({
        'type':     4,
        'rsuID':    my_id(),
        'carID':    car,
        'state':    state,
        'sensors':  sensors,
    })


def its2rsu(car, feedback):
    feedback = cipher(feedback)
    send({
        'type':     5,
        'itsID':    my_id(),
        'carID':    car,
        'feedback': feedback,
    })


def rsu2car(feedback):
    send({
        'type':     6,
        'rsuID':    my_id(),
        'feedback': feedback,
    })
