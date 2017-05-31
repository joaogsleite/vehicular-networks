
from devices.car.components.sensors import breathalyzer, fitbit, mindwave
import devices.car.components.car.alerts as alert

import devices.car.components.car.steering as steering


def state():
    if breathalyzer.danger() or fitbit.danger() or mindwave.danger() or steering.danger():
        print 'driver state: danger'
        return 'danger'
    else:
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
