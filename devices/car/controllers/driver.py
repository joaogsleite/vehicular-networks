
from devices.car.components.sensors import breathalyzer, fitbit, mindwave
import devices.car.components.car.alerts as alert

import devices.car.components.car.steering as steering


def state():
    data = sensors()
    if data['alcohol'] < 0.2 \
        or 50 < data['pulse'] < 100 \
        or data['attention'] < 20 \
        or steering.danger():
            alert.driver_not_well()
            return 'danger'
    else:
        return 'ok'


def sensors():
    return {
        'alcohol':      breathalyzer.get(),
        'pulse':        fitbit.get(),
        'attention':    mindwave.get(),
    }
