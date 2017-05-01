import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import time

time_to_sleep = 2
pin_default = 12                          
GPIO.setmode(GPIO.BOARD)

ON = 1
OFF = 0
 
#Define pin 12 as output
GPIO.setup(pin_default, GPIO.OUT)
 
def ledon(pin_led = pin_default):
    GPIO.output(pin_led, ON)
    return

def ledoff(pin_led = pin_default):
    GPIO.output(pin_led, OFF)
    return
 
while(True):      
  ledon()
  time.sleep(time_to_sleep)
  ledoff()
  time.sleep(time_to_sleep)
