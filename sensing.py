#!/usr/bin/env python
import RPi.GPIO as GP
GP.setmode(GP.BCM)
GP.setup(18,GP.IN)



print(GP.input(18))
try:
	while True:
		value = GP.input(18)
#	if(value != GP.input(18)):
		value = GP.input(18)
		if value == 0:
#	print(GP.input(18)
			print'NIGHTTIME'	
		else:	
#			print(GP.input(18)
			print'DAYTIME'
except KeyboardInterrupt:
	pass
GP.cleanup()
