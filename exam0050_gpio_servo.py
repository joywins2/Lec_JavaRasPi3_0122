'''
...image : https://drive.google.com/open?id=1zfOZ19gj_Q5N-dkhHBZZvw8rGXlBIFfU
...126p. GPIO and Servo Motor :
   GPIO 15 pin(BCM) to Orange, 5V to Red, GND to black. 
   move servo motor 180, 90, -180 degree.   
'''

'''
...Question : why is GPIO 15 not available?
pi@raspberrypi:~/Lec_JavaRasPi3_0122 $ sudo python exam0050_gpio_servo.py
exam0050_gpio_servo.py:11: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(pin, GPIO.OUT)  #...set GPIO 15 pin to output.

'''

import RPi.GPIO as GPIO
import time
pin = 21         #...set GPIO 15 pin to the signal of servo motor.
GPIO.setmode(GPIO.BCM)     #...set the protocol GPIO PIN to BCM. 
GPIO.setup(pin, GPIO.OUT)  #...set GPIO 15 pin to output.
svr = GPIO.PWM(pin, 50)    #...set the pulse(?)/frequency of pin to 50Hz 20ms. 
svr.start(50)    #...set duty cycle to 50%.

try:
    for i in range(0, 5):
        #...rotate 180 degree to the left.
        svr.ChangeDutyCycle(10)
        time.sleep(1)
        #...rotate 180 degree to the right.
        svr.ChangeDutyCycle(1)
        time.sleep(1)
        #...rotate 180 degree to the middle.
        svr.ChangeDutyCycle(5)
        time.sleep(1)
except KeyboardInterrupt: #...Ctrl + C.
    svr.stop()
    
#...init all setting of GPIO.    
GPIO.cleanup()