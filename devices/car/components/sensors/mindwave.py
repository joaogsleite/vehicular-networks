from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

mindwaveDataPointReader = None
attention = []
buffer_index = 0


def init():
    global mindwaveDataPointReader
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()


def update():
    global mindwaveDataPointReader
    global attention
    global buffer_index
    dataPoint = mindwaveDataPointReader.readNextDataPoint()
    if dataPoint.__class__.__name__ == 'AttentionDataPoint':
        value = str(dataPoint)
        number = value.split('Attention Level: ')[1]
        attention[buffer_index] = int(number)
        buffer_index += 1
        if buffer_index == 20:
            buffer_index = 0

def get():
    # return last alcohol value read from mindwave
    global attention
    return attention


def danger():
    global attention
    med = sum(attention) / 20
    return med < 20


def set(value):
    # set value for demonstration
    global attention
    attention = value
