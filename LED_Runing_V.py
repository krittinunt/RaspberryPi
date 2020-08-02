#!/usr/bin/python3
# by krittinunt@gmail.com

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [26, 19, 13, 6, 5, 21, 20, 16]
db_table = ['10000001', '01000010', '00100100', '00011000']

for i in range(8):
	GPIO.setup(LED[i], GPIO.OUT)
	
GPIO.setwarnings(False)

try:
	while True:
		for n in range(len(db_table)):
			data = db_table[n]
			for i in range(8):
				if data[i] == '1':
					GPIO.output(LED[i], True)
				else:
					GPIO.output(LED[i], False)
			sleep(0.5)
		for n in range(len(db_table) - 2, 0, -1):
			data = db_table[n]
			for i in range(8):
				if data[i] == '1':
					GPIO.output(LED[i], True)
				else:
					GPIO.output(LED[i], False)
			sleep(0.5)
		
finally:
	GPIO.cleanup()
