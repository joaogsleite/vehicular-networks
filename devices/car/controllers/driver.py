
from devices.car.components.sensors import breathalyzer, fitbit, mindwave
import devices.car.components.car.alerts as alert

import devices.car.components.car.steering as steering

import devices.car.simulator.main as simulator

already_danger = False

def state():
    global already_danger

    if already_danger:
        return 'danger'

    #if breathalyzer.danger() or fitbit.danger() or mindwave.danger() or steering.danger():
    if fitbit.danger() or mindwave.danger() or steering.danger():
        print 'driver state: danger'
        simulator.pre_test = True
        alert.driver_not_well()
        already_danger = True
        return 'danger'
    else:
        simulator.pre_test = False
        print 'driver state: ok'
        return 'ok'


def sensors():
    data = {
        'alcohol':      breathalyzer.get(),
        'pulse':        fitbit.get(),
        'attention':    mindwave.get(),
    }
    print 'sensors data: '+str(data)
    return data
