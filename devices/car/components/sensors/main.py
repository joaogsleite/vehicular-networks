from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

mindwaveDataPointReader = MindwaveDataPointReader()
# connect to the mindwave mobile headset...
mindwaveDataPointReader.start()
# read one data point, data point types are specified in  MindwaveDataPoints.py'
while True:
    dataPoint = mindwaveDataPointReader.readNextDataPoint()
    if dataPoint.__class__.__name__ == 'AttentionDataPoint':
        print dataPoint
