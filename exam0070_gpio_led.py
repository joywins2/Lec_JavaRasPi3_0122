'''
...153p.
...step.01.set the GPIO pin of LED to OUTPUT.
   step.02.command LED ON/OFF.
   step.03.change the time of LED ON/OFF.
   image : https://drive.google.com/open?id=1MUPB7gOiEPrCHQ6sPxCs-Pu_MVILZeB-
   
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
  
try:  
    GPIO.output(5, True)
    time.sleep(10)
    GPIO.output(5, False)
    time.sleep(2.5)  
    
    GPIO.output(6, True)
    time.sleep(10)
    GPIO.output(6, False)
    time.sleep(2.5)  
  
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