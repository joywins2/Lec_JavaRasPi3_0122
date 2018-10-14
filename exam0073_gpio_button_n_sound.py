'''
...ref : https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all
   
'''

import RPi.GPIO as GPIO
import time
import sys
#...This says that we want to import the mixer module from the pygame package.
#...from PACKAGE import Module.
from pygame import mixer

# Pins definitions
btn_pin = 4
led_pin = 12

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# Initialize pygame mixer
mixer.init()

# Remember the current and previous button states
current_state = True
prev_state = True


'''
...Load the sounds
   Our downloaded file, applause-1.wav is used to create a Sound object, 
   which we store in the sound variable. 
   We can call the .play() method in our Sound object to start playing the .wav file.
'''
sound = mixer.Sound('applause-1.wav')

def ex_001_pushButtonGetSound():
    while True:
        current_state = GPIO.input(btn_pin)
        if (current_state == False) and (prev_state == True):
            sound.play()
        prev_state = current_state
    
def ex_002_pushButtonGetSound_n_LedOn():    
    while True:
        # If button is pressed, turn on LED and play sound
        current_state = GPIO.input(btn_pin)
        if (current_state == False) and (prev_state == True):
            if mixer.get_busy():
                sound.stop()
            else:
                GPIO.output(led_pin, GPIO.HIGH)
                sound.play()

        # Only turn off LED if sound has stopped playing
        if mixer.get_busy() == False:
            GPIO.output(led_pin, GPIO.LOW)

        # Save state of switch to use in next iteration of the loop
        prev_state = current_state
  
try:        
    #ex_001_pushButtonGetSound()
    ex_002_pushButtonGetSound_n_LedOn()

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    GPIO.cleanup()  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")  
    print("Unexpected error:", sys.exc_info()[0])
  
finally:  
    GPIO.cleanup() # this ensures a clean exit   
    print("GPIO cleanup...")