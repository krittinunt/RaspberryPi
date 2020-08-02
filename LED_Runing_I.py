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
	while True:
		for i in range(8):
			GPIO.output(LED[i], True)
			sleep(0.5)
		for i in range(8):
			GPIO.output(LED[i], False)
			sleep(0.5)
		
finally:
	GPIO.cleanup()
