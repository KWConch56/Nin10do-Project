#Nin10do Script#
#Created by Daniël Spies - December 2014#
#The script operates the stepper motor and the USB leds#

from subprocess import call
import RPi.GPIO as gpio
from time import sleep

#Setmode Broadcom SOC Channel#
gpio.setmode(gpio.BCM)
gpio.setwarnings (False)

#Shutdown function:#
def shutdown(pin):
        LedUit()
	global klep_stand
	if (klep_stand == 1):
		KlepDicht()
		klep_stand = klep_stand -1
	else:
		print "afsluiten" 
		
#Main loop (do nothing until interrupt)#
def Loop():
	while True:		
		sleep(0.007)
		
#Blinking function for the Leds on startup#
def LedBlink():
	for i in range(4):
		for halfstep in range(9):
			for pin in range(4):
				gpio.output(ledpin[pin], seqcw[halfstep][pin])
			sleep(0.15)
            
#Opening the cover#
def KlepOpen():
	LedAan()
	for i in range(48):
		for halfstep in range(9):
			for pin in range(4):
				gpio.output(Controlpin[pin], seqcw[halfstep][pin])
			sleep(0.007)
	

#Closing the cover#
def KlepDicht():
	LedUit()
	for i in range(48):
		for halfstep in range(9):
			for pin in range(4):
				gpio.output(Controlpin[pin], seqccw[halfstep][pin])
			sleep(0.007)
			
#Defines the state of the cover (open or closed)#
def Klep(channel):
	global klep_stand
	if (klep_stand == 1):
		KlepDicht()
		klep_stand = klep_stand -1
	else:
		KlepOpen()
		klep_stand = klep_stand +1
		
#Turn on all the led's#
def LedAan():
	for pin in ledpin:
		gpio.output(pin,1)
	sleep(0.007)
	
#Turn off all the led's#
def LedUit():
	for pin in ledpin:
		gpio.output(pin,0)
	sleep(0.007)

	   
		
#Define GPIO pins and start-up state#
ledpin = [11,13,19,26]
Controlpin = [9,10,27,17]
start = 1

#Setting GPIO (stepper motor) pins to OUTPUT and 0 state#
for pin in Controlpin:
	gpio.setup(pin,gpio.OUT)
	gpio.output(pin,0)

#Setting GPIO (led) pins to OUTPUT and 0 state#
for pin in ledpin:
	gpio.setup(pin,gpio.OUT)
	gpio.output(pin,0)

#Setting for ATX Raspi powerboard#
gpio.setup(7, gpio.IN)

#Setting for cover button#
gpio.setup(25, gpio.IN, pull_up_down=gpio.PUD_UP)

#Arrays for stepper motor and leds#
seqcw  = [[1,0,0,0], 
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
        [1,0,0,1],
	[0,0,0,0]]

seqccw = [[0,0,0,1], 
	[0,0,1,1],
	[0,0,1,0],
	[0,1,1,0],
	[0,1,0,0],
	[1,1,0,0],
        [1,0,0,0],
	[1,0,0,1],
	[0,0,0,0]]

#Interrupt functions for ATX Raspi and cover# 
gpio.add_event_detect(25, gpio.FALLING, callback=Klep, bouncetime=400) 
gpio.add_event_detect(7, gpio.RISING, callback=shutdown, bouncetime=3000)

#Startup script opening cover and activates led blink function#
while (start == 1): 
	KlepOpen()
	klep_stand = 1
	LedBlink()
	sleep(1)
	LedAan()
	start = 0

Loop()



