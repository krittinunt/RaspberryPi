#!/usr/bin/python3
# by krittinunt@gmail.com

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [26, 19, 13, 6, 5, 21, 20, 16]

for i in range(8):
	GPIO.setup(LED[i], GPIO.OUT)
	
GPIO.setwarnings(False)

try:
	n = 0
	while True:
		if n >= 8:
			n = 0
		for i in range(8):
			if i == n:
				GPIO.output(LED[i], True)
			else:
				GPIO.output(LED[i], False)
		sleep(0.5)
		n += 1
		
finally:
	GPIO.cleanup()
