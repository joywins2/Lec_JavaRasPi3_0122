'''
...179P.Important!!!
   image : https://drive.google.com/open?id=1QdZMhf_06B3F4VcgPNrOcN9l0K4ghltZ
   S/W ON, GPIO 26 is 0 and if S/W OFF, GPIO 26 is 1.
   even though GPIO 5 is OUTPUT, 
       setting its value 0 makes LED ON since flow is successful.
       setting its value 1 makes LED OFF since flow is not successful.    
'''

import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(26, GPIO.IN)   #...set Switch1, GPIO 26 pin to INPUT
GPIO.setup(27, GPIO.IN)   #...set Switch2, GPIO 27 pin to INPUT
GPIO.setup(5, GPIO.OUT)   #...set LED, GPIO 5 pin to OUTPUT

def my_callback(channel):
    if GPIO.input(27) == 0:
        print("GPIO 27 Switch ON, GPIO 5 LED ON...")
        GPIO.output(5, False)
    else:
        print("GPIO 27 Switch OFF GPIO 5 LED OFF...")
        GPIO.output(5, True)
        
#...register event my_callback for GPIO 27.
GPIO.add_event_detect(27, GPIO.FALLING, callback=my_callback)

while True:
    try:
        time.sleep(1) #...main waits for every 10ms.
        print("main runs...")
    except KeyboardInterrupt:
        #...remove event for GPIO 27.
        GPIO.remove_event_detect(27)
        GPIO.cleanup()    
'''
finally:
    GPIO.cleanup()
'''
