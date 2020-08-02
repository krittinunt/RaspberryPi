#!/usr/bin/python3
# by krittinunt@gmail.com
# LED Control by Software

from time import sleep
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [26, 19, 13, 6, 5, 21, 20, 16]
status = ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']

for i in range(8):
	GPIO.setup(LED[i], GPIO.OUT)
	GPIO.output(LED[i], False)
GPIO.setwarnings(False)
		
try:
	while True:
		os.system("clear")
		print('---- LED Control by krittinunt@gmail.com ----------------')
		print('=========================================================')
		print('| LED0 | LED1 | LED2 | LED3 | LED4 | LED5 | LED6 | LED7 |')
		print('|-------------------------------------------------------|')
		print('| ', status[0], ' ',
		      '| ', status[1], ' ',
		      '| ', status[2], ' ',
		      '| ', status[3], ' ',
		      '| ', status[4], ' ',
		      '| ', status[5], ' ',
		      '| ', status[6], ' ',
		      '| ', status[7], '  |')
		print('---------------------------------------------------------')
		
		# Control input
		control_input = True
		while control_input:
			try:
				n_led = input('Enter LED number [0-7]: ')
				n_led = int(n_led)
				if n_led >= 0 and n_led <= 7:
					control_input = False
				else:
					print('[Error] : Please Enter LED number 0-7 only')
			except ValueError as e:
				print('[Error] : ', e)
				print('Press enter to continue')
		
		control_input = True
		while control_input:
			logic = input('Change status to \'H\' or \'L\' : ')
			if logic == 'L' or logic == 'l':
				GPIO.output(LED[n_led], False)
				status[n_led] = 'L'
				control_input = False
			elif logic == 'H' or logic == 'h':
				GPIO.output(LED[n_led], True)
				status[n_led] = 'H'
				control_input = False
			else :
				print('[Error] : Please Enter status to \'H\' or \'L\' only')
		
finally:
	GPIO.cleanup()
