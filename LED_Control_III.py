#!/usr/bin/python3
# by krittinunt@gmail.com
# LED Control by PB_Switch

# PB_SW[0] --> All LED Off
# PB_SW[1] --> All LED On
# PB_SW[2] --> All LED toggle

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

def all_led_off():
	for i in range(8):
		GPIO.output(LED[i], False)
		
def all_led_on():
	for i in range(8):
		GPIO.output(LED[i], True)
		
def led_toggle():
	if GPIO.input(LED[0]):
		for i in range(8):
			GPIO.output(LED[i], False)
	else:
		for i in range(8):
			GPIO.output(LED[i], True)

try:
	print('Press PB_SW[0] button to led off')
	print('Press PB_SW[1] button to led on')
	print('Press PB_SW[2] button to led toggle')
	print('Press CTRL+C to exit')
	while True:
		if not GPIO.input(PB_SW[0]):
			while not GPIO.input(PB_SW[0]):
				sleep(0.02)
			all_led_off()
		if not GPIO.input(PB_SW[1]):
			while not GPIO.input(PB_SW[1]):
				sleep(0.02)
			all_led_on()
		if not GPIO.input(PB_SW[2]):
			while not GPIO.input(PB_SW[2]):
				sleep(0.02)
			led_toggle()
			
finally :
	GPIO.cleanup()
