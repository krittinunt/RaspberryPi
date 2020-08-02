#!/usr/bin/python3
# by krittinunt@gmail.com
# LED Control by PB_Switch L and R

# PB_SW[0] --> LED move left
# PB_SW[1] --> N/A
# PB_SW[2] --> LED move right

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [26, 19, 13, 6, 5, 21, 20, 16]
PB_SW = [22, 27, 17]

for i in range(8):
	GPIO.setup(LED[i], GPIO.OUT)
	GPIO.output(LED[i], False)
for i in range(3):
	GPIO.setup(PB_SW[i], GPIO.IN)
GPIO.setwarnings(False)

def draw_led(n):
	for i in range(8):
		if i == n:
			GPIO.output(LED[i], True)
		else:
			GPIO.output(LED[i], False)

try:
	print('Press PB_SW[0] LED move left')
	print('Press PB_SW[1] N/A')
	print('Press PB_SW[2] LED move right')
	print('Press CTRL+C to exit')
	
	n = 0
	draw_led(n)
	while True:
		#LED move left
		if not GPIO.input(PB_SW[0]):
			while not GPIO.input(PB_SW[0]):
				sleep(0.02)
			if n > 0:
				n -= 1
			draw_led(n)
		#LED move right
		if not GPIO.input(PB_SW[2]):
			while not GPIO.input(PB_SW[2]):
				sleep(0.02)
			if n < 7:
				n += 1
			draw_led(n)
			
finally :
	GPIO.cleanup()
