'''
...ref : https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all
   
'''

import RPi.GPIO as GPIO
import time
import sys

# Pin definitions
led_pin = 12
btn_pin = 4

# Our counter
ex004_counter = 0
# Remember the current and previous button states
ex004_current_state = True
ex004_prev_state = True

# Suppress warnings
#GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(btn_pin, GPIO.IN)


def exPWM_001():
    # Initialize pwm object with 50 Hz and 0% duty cycle
    pwm = GPIO.PWM(led_pin, 50)
    pwm.start(0)
    
    # Set PWM duty cycle to 50%, wait, then to 90%
    pwm.ChangeDutyCycle(50)
    time.sleep(2)
    pwm.ChangeDutyCycle(90)
    time.sleep(2)            
        
    # Stop, cleanup, and exit
    pwm.stop()
    GPIO.cleanup()
    

def exPWM_002():
    # Initialize pwm object with 50 Hz and 0% duty cycle
    pwm = GPIO.PWM(led_pin, 50)
    pwm.start(0)
    
    # Have the LED slowly fade up, turn off, and repeat
    while True:
        for brightness in range(0, 101):
            pwm.ChangeDutyCycle(brightness)
            time.sleep(0.02)    
  
    

def ex_003():
    '''
    #...image : https://drive.google.com/open?id=12PKijQ9VGFI2v0EtGmqi5j6mpRgq51DU
    The other odd thing you might see is that if GPIO.input(btn_pin) is True (which means the pin is logic high, or 3.3V), we turn the LED off. Wait, what?
    In our circuit, our button has a pull-up resistor connecting one of the pins to a constant 3.3V. 
    This means that in its default state (not pressed), the pin connected to the button is 3.3V. 
    
    When we press the button, the pin is connected to ground (through the buttons internal contacts), and the pin becomes logic low (0V).
    '''
    while True:
        time.sleep(0.25)    
        if GPIO.input(btn_pin):
            print("btn released, led_pin OFF")
            GPIO.output(led_pin, GPIO.LOW)
        else:
            print("btn pressed, led ON")
            GPIO.output(led_pin, GPIO.HIGH)    
  

def ex_004():
    # Our counter
    global ex004_counter
    # Remember the current and previous button states
    global ex004_current_state
    global ex004_prev_state    
    
    while True:
        ex004_current_state = GPIO.input(btn_pin)
        if (ex004_current_state == False) and (ex004_prev_state == True):
            ex004_counter = ex004_counter + 1
            print("ex004_counter %d"%ex004_counter)
        ex004_prev_state = ex004_current_state
    
  
try:        
    #exPWM_001()
    #exPWM_002()   
    #ex_003()
    ex_004()


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