
import threading
from time import sleep

from devices.car.components.car import gps, steering, alerts
from sensors import mindwave, fitbit, breathalyzer

running = False
thread = None
pre_test = True
mock_gsp = False


def run_in_background():

    global running
    global pre_test

    try:
        print 'starting mindwave...'
        mindwave.init()
    except:
        print "Error init mindwave"

    try:
        print 'starting alert leds...'
        alerts.init()
    except:
        print "Error init alerts"

    try:
        print 'starting breathalyzer...'
        breathalyzer.init()
    except:
        print "Error init breathalyzer"

    while pre_test:
        print 'blow test stated!'
        alerts.blow(True)
        for i in range(20):
            print i + 1
            breathalyzer.update()

        if breathalyzer.danger() is False:
            print 'blow test complete!'
            alerts.blow(False)
            pre_test = False

    while running:
        print 'Updating values from car components'

        try:
            if mock_gsp:
                gps.read()
            else:
                gps.update()
        except:
            print "No GPS"

        try:
            steering.update()
        except:
            print "No steering"

        try:
            mindwave.update()
        except:
            print "No mindwave"

        try:
            fitbit.update()
        except:
            "No fitbit"

        try:
            breathalyzer.update()
        except:
            "No breathlyzer"

        sleep(1)

    alerts.shutdown()


def stop():
    global running
    global thread
    global pre_test
    print 'stoping sensors reading data...'
    running = False
    pre_test = False
    thread.join()


def start():
    global thread
    global running
    running = True
    print 'starting sensors background thread...'
    thread = threading.Thread(target=run_in_background, args=())
    thread.start()
