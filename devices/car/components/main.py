
import threading
from time import sleep

from devices.car.components.car import gps, steering, alerts
from sensors import mindwave, fitbit, breathalyzer
import devices.car.simulator.main as simulator

running = False
thread1 = None
thread2 = None
pre_test = True
mock_gsp = False

def run_in_background():

    global running
    global pre_test

    while pre_test:
        simulator.pre_test = True
        simulator.running = True
        print 'blow test stated!'
        alerts.blow(True)
        for i in range(20):
            breathalyzer.update()
            sleep(0.5)

        if breathalyzer.danger() is False:
            print 'blow test complete!'
            alerts.blow(False)
            pre_test = False
            simulator.pre_test = False

    while running:
        simulator.running = True
        print 'Updating values from car components'

        try:
            if mock_gsp:
                gps.read()
            else:
                gps.update()
        except Exception,e:
            print "No GPS"
            print e

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
    global thread1
    global thread2
    global pre_test
    print 'stoping sensors reading data...'
    running = False
    pre_test = False
    
    try:
        thread1.join()
    except:
        print ''

    try:
        simulator.stop()
        thread2.join()
    except:
        print ''

    try:
        steering.stop()
    except:
        print ''


def start():
    global thread1
    global thread2
    global running
    running = True

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

    try:
        print 'starting steering...'
        steering.start()
    except:
        print "No steering"

    print 'starting sensors background thread...'
    thread1 = threading.Thread(target=run_in_background, args=())
    thread1.start()


    thread2 = threading.Thread(target=simulator.start, args=())
    thread2.start()


