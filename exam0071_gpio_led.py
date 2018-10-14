'''
...153p.
...step.01.set the GPIO pin of LED to OUTPUT.
   step.02.command LED ON/OFF.
   step.03.change the time of LED ON/OFF.
   image : https://drive.google.com/open?id=1MUPB7gOiEPrCHQ6sPxCs-Pu_MVILZeB-
   
'''

import RPi.GPIO as GPIO
import time

# Pin definitions
led_pin = 12

# Suppress warnings
#GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

  
try:
    # Blink forever
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)
      
  
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    GPIO.cleanup()  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit   
    print("GPIO cleanup...")