#!/usr/bin/python

# /**
#  @file breakout_testbech.py
#  @author  Oscar Gomez Fuente <oscargomezf@gmail.com>
#  @ingroup iElectronic
#  @date 14/05/2014
#  @version 1.1.0
#  @section DESCRIPTION
#   test bech to check GPIOs.
#	GPIO 23 -> output led green
#	GPIO 24 -> output led green
#	GPIO 18 -> pwm output led green
#	GPIO 4 -> clk output buzzer
#	GPIO 25 -> input switch
#  */

import sys
import wiringpi2
from time import sleep

DELAY = 2
song = [ 659, 659, 0, 659, 523, 659, 0, 784, 0, 0, 0, 392, 0, 0, 0, 523, 0, 0, 392, 0, 0, 330 ]

def pwm_dimm(io, delay):
	pin = 18 # only supported on this pin
	io.pinMode(pin, io.PWM_OUTPUT)
	#io.pwmSetClock(2)
	#io.pwmSetRange(10)
	
	for i in range(0, 1024, 1):
		io.pwmWrite(pin, i)
		io.delay(delay)

	for i in range(1024, -1, -1):
		io.pwmWrite(pin, i)
		io.delay(delay)

def leds(io):
	#config gpios output mode
	io.pinMode(23, io.OUTPUT)
	io.pinMode(24, io.OUTPUT)
	#Check led in GPIO23
	io.digitalWrite(23, 1)
	io.delay(2000)
	io.digitalWrite(23, 0)
	#Check led in GPIO24
	io.digitalWrite(24, 1)
	io.delay(2000)
	io.digitalWrite(24, 0)

def swith(io):
	#config gpio input mode
	io.pinMode(25, io.INPUT)
	print('Please press button')
	while (io.digitalRead(25) == io.HIGH):
		io.delay(100)
	print('Button pressed')

def tone(io, song):
	pin = 4 # only supported on this pin
	io.softToneCreate(pin)

	for i in range(len(song)):
		io.softToneWrite(pin, song[i])
		io.delay(200)
	
	io.softToneWrite(pin, 0)		
	io.pinMode(pin, io.INPUT)

def clock(io, frecuency):
	pin = 4 # only supported on this pin
	io.pinMode(pin, io.GPIO_CLOCK)

	io.gpioClockSet(pin, frecuency)
	io.delay(2000)	
	io.pinMode(pin, io.INPUT)

	
#config gpios with wiringpi2 library
io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_GPIO)

#test bench leds
leds(io)
#test bench pwm led
pwm_dimm(io, DELAY)
#test bench input switch
swith(io)
#test bench tone
tone(io, song)
#test bench clock
clock(io, 5000)
