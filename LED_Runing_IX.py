#!/usr/bin/python3
# by krittinunt@gmail.com
from threading import Thread
from random import randrange	# randrange gives you an integral value
from random import uniform		# uniform gives you a floating-point value
from time import sleep
import RPi.GPIO as GPIO

#define varible
DELAY_START = 0
DELAY_STOP = 0.75
PIN_LED = [26, 19, 13, 6, 5, 21, 20, 16]
LED1_Control = False
LED2_Control = False
LED3_Control = False
LED4_Control = False
LED5_Control = False
LED6_Control = False
LED7_Control = False
LED8_Control = False

#init system
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in PIN_LED:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, False)

print('Press CTRL+C to exit')

def LED1Blink():
    print('LED 1 Runing...')
    while LED1_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[0], not GPIO.input(PIN_LED[0]))
    print('LED 1 Stop')

def LED2Blink():
    print('LED 2 Runing...')
    while LED2_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[1], not GPIO.input(PIN_LED[1]))
    print('LED 2 Stop')

def LED3Blink():
    print('LED 3 Runing...')
    while LED3_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[2], not GPIO.input(PIN_LED[2]))
    print('LED 3 Stop')

def LED4Blink():
    print('LED 4 Runing...')
    while LED4_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[3], not GPIO.input(PIN_LED[3]))
    print('LED 4 Stop')
        
def LED5Blink():
    print('LED 5 Runing...')
    while LED5_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[4], not GPIO.input(PIN_LED[4]))
    print('LED 5 Stop')
        
def LED6Blink():
    print('LED 6 Runing...')
    while LED6_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[5], not GPIO.input(PIN_LED[5]))
    print('LED 6 Stop')
        
def LED7Blink():
    print('LED 7 Runing...')
    while LED7_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[6], not GPIO.input(PIN_LED[6]))
    print('LED 7 Stop')
        
def LED8Blink():
    print('LED 8 Runing...')
    while LED8_Control:
        sleep(uniform(DELAY_START, DELAY_STOP))
        GPIO.output(PIN_LED[7], not GPIO.input(PIN_LED[7]))
    print('LED 8 Stop')

try:	
	try:
		task_1 = Thread(target=LED1Blink)
		task_2 = Thread(target=LED2Blink)
		task_3 = Thread(target=LED3Blink)
		task_4 = Thread(target=LED4Blink)
		task_5 = Thread(target=LED5Blink)
		task_6 = Thread(target=LED6Blink)
		task_7 = Thread(target=LED7Blink)
		task_8 = Thread(target=LED8Blink)
		
		LED1_Control = True
		LED2_Control = True
		LED3_Control = True
		LED4_Control = True
		LED5_Control = True
		LED6_Control = True
		LED7_Control = True
		LED8_Control = True
		
		task_1.start()
		sleep(0.5)
		task_2.start()
		sleep(0.5)
		task_3.start()
		sleep(0.5)
		task_4.start()
		sleep(0.5)
		task_5.start()
		sleep(0.5)
		task_6.start()
		sleep(0.5)
		task_7.start()
		sleep(0.5)
		task_8.start()
		
		#Return whether the thread is alive
		#print (task_1.isAlive())
		#sleep(5)
		#ok = False
		#sleep(3)
		#print (task_1.isAlive())
		#sleep(5)
		#ok = True
		#task_1 = Thread(target=led0Control)
		#task_1.start()
		#sleep(3)
		#print (task_1.isAlive())
		
		
	except Exception as e:
		print(e)
	
	while True:
		pass

finally:
	GPIO.cleanup()
	
	
