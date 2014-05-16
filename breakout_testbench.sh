#!/bin/sh

# /**
#  @file breakout_testbech.py
#  @author  Oscar Gomez Fuente <oscargomezf@gmail.com>
#  @ingroup iElectronic
#  @date 13/05/2014
#  @version 1.0.0
#  @section DESCRIPTION
#   test bech to check GPIOs.
#	GPIO 23 -> output led green
#	GPIO 24 -> output led green
#	GPIO 18 -> pwm output led green
#	GPIO 4 -> clk output buzzer
#	GPIO 25 -> input switch
#  */ 

#Test GPIO23 OUT 
echo 23 > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio23/direction
echo 1 > /sys/class//gpio/gpio23/value
sleep 1
echo 0 > /sys/class/gpio/gpio23/value
echo 23 > /sys/class/gpio/unexport
sleep 1

#Test GPIO24 OUT
echo 24 > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio24/direction
echo 1 > /sys/class//gpio/gpio24/value
sleep 1
echo 0 > /sys/class/gpio/gpio24/value
echo 24 > /sys/class/gpio/unexport
sleep 1

#Test GPIO25 INPUT
echo 25 > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio25/direction
echo "Press the button to check it"
value=1
while [ "$value" != "0" ]
do
	value=$(cat /sys/class/gpio/gpio25/value)
done
echo "Button pressed sucessful"
echo 25 > /sys/class/gpio/unexport

#Test GPIO18 OUT 
echo 18 > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio18/direction
echo 1 > /sys/class//gpio/gpio18/value
sleep 1
echo 0 > /sys/class/gpio/gpio18/value
echo 18 > /sys/class/gpio/unexport

#Test GPIO4 OUT
echo 4 > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio4/direction
echo 1 > /sys/class//gpio/gpio4/value
sleep 1
echo 0 > /sys/class/gpio/gpio4/value
echo 4 > /sys/class/gpio/unexport

