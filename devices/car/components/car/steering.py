
import os

steering = 0
throttle = 0
brake = 0


def get():
    # return last steering value read from steering wheel
    global steering
    return steering


def update():
    # read real value from steering wheel
    global steering
    global throttle
    global brake


    # TODO: @tiago melhorar esta merda
    command = 'timeout 0.1s jstest --normal /dev/input/js0'
    output = os.popen(command).read()
    line = output.split('Axes:')[-1]

    steering = int(line.split('0:')[1].split('1:')[0])
    throttle = int(line.split('1:')[1].split('2:')[0])
    brake = int(line.split('2:')[1].split('3:')[0])


def update(st, th, br):
    # set value for demonstration
    global steering
    global throttle
    global brake
    steering = st
    throttle = th
    brake = br
