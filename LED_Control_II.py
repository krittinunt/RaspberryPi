#!/usr/bin/python3
# by krittinunt@gmail.com
# LED Control by PWM 100Hz use sleep

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [26, 19, 13, 6, 5, 21, 20, 16]

for i in range(8):
	GPIO.setup(LED[i], GPIO.OUT)
	GPIO.output(LED[i], False)
GPIO.setwarnings(False)

try:
	control_input = True
	while control_input:
		try:
			n_pwm = input('Enter %PWM [0-100] : ')
			n_pwm = int(n_pwm)
			if n_pwm >=0 and n_pwm <= 100:
				tp = n_pwm/10000
				ts = 0.01-tp
				print('LED bright [', n_pwm, '%]')
				print('Press CTRL+C to exit')
				control_input = False
			else:
				print('[Error] : Please Enter %PWM [0-100] only')
				
		except ValueError as e:
			print('[Error] : ', e)
		
	while True:
		for i in range(8):
			GPIO.output(LED[i], True)
		sleep(tp)
		for i in range(8):
			GPIO.output(LED[i], False)
		sleep(ts)
		
finally :
	GPIO.cleanup()
