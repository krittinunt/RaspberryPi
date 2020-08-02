#!/usr/bin/python3
# by krittinunt@gmail.com

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [26, 19, 13, 6, 5, 21, 20, 16]
db_table = ['10000001', '01000010', '00100100', '00011000', '00000000',
            '10000001', '11000011', '11100111', '11111111', '00000000',
            '11000000', '00000011', '00011000', '01111110', '11111111',
            '10000000', '01000000', '00100000', '00010000', '00001000',
            '00000100', '00000010', '00000001', '11111111', '00000000']
delay_table = [0.2, 0.4, 0.6, 0.8, 1,
               1, 0.8, 0.6, 0.4, 0.2,
               0.5, 0.3, 0.5, 0.3, 0.7,
               0.2, 0.7, 0.4, 0.9, 1,
               0.8, 0.3, 0.6, 0.7, 0.5]

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
			sleep(delay_table[n])
		
finally:
	GPIO.cleanup()
