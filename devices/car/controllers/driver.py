
from devices.car.components.sensors import breathalyzer, fitbit, mindwave
import devices.car.components.car.alerts as alert

import devices.car.components.car.steering as steering


def state():
    if breathalyzer.danger() or fitbit.danger() or mindwave.danger() or steering.danger():
        return 'danger'
    else:
        return 'ok'


def sensors():
    return {
        'alcohol':      breathalyzer.get(),
        'pulse':        fitbit.get(),
        'attention':    mindwave.get(),
    }
