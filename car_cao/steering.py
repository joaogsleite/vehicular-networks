from subprocess import Popen, PIPE, STDOUT
import os

def getDirection():
	command = 'timeout 0.1s jstest --normal /dev/input/js0'
	output = os.popen(command).read()
	line = output.split('Axes:')[-1]

	steering = int(line.split('0:')[1].split('1:')[0])
	throttle = int(line.split('1:')[1].split('2:')[0])
	brake = int(line.split('2:')[1].split('3:')[0])

	return {'steering':steering, 'throttle':throttle, 'brake':brake}

#test
print getDirection()
