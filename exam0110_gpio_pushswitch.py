'''
...179P.Important!!!
   image : https://drive.google.com/open?id=1pPU8kqBr7Yx3PCRtpP98u0l65sZ8QGlR
   if S/W ON, GPIO 26 is 0 and if S/W OFF, GPIO 26 is 1.
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

try:
    while True:
        #...if GPIO 26 Switch is on.
        if GPIO.input(26) == 1:
            print("GPIO 26 Switch OFF, GPIO 5 LED OFF...")
            GPIO.output(5, True)
        else:
            print("GPIO 26 Switch ON, GPIO 5 LED ON..")
            GPIO.output(5, False)
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
'''
finally:
    GPIO.cleanup()
'''
