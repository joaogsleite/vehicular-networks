
from devices.car.components.sensors import breathalyzer, fitbit, mindwave
import devices.car.components.car.alerts as alert


def state():
    data = sensors()
    if data['alcohol'] < 0.2 \
        and 50 < data['pulse'] < 100 \
            and data['attention'] < 0.5:
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


