
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader


mindwaveDataPointReader = None
attention = 0


def init():
    global mindwaveDataPointReader
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()


def update():
    global mindwaveDataPointReader
    global attention
    dataPoint = mindwaveDataPointReader.readNextDataPoint()
    if dataPoint.__class__.__name__ == 'AttentionDataPoint':
        value = str(dataPoint)
        number = value.split('Attention Level: ')[1]
        attention = int(number)


def get():
    # return last alcohol value read from mindwave
    global attention
    return attention


def set(value):
    # set value for demonstration
    global attention
    attention = value
