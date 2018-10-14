import RPi.GPIO as GPIO
import time

buzz20 = 20
buzz21 = 21

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzz20, GPIO.OUT)
    GPIO.setup(buzz21, GPIO.OUT)
    
    global buzz20
    global buzz21
     
    buzz20 = GPIO.PWM(buzz20, 500) #...set frequency to 500hz. 
    buzz20.start(50)   #...set duty cycle to 25%.
     
    buzz21 = GPIO.PWM(buzz21, 500) 
    buzz21.start(50)
    
try:
    setup()    
    for i in range(0, 8):
        buzz20.ChangeFrequency(400)
        buzz20.start(10)
        time.sleep(0.25)
        buzz20.stop()
        time.sleep(0.1)
        
    
    for i in range(0, 8):
        buzz21.ChangeFrequency(400)
        buzz21.start(10)
        time.sleep(0.25)
        buzz21.stop()
        time.sleep(0.1)        

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("except KeyboardInterrupt\n")  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    println("Other error or exception occurred!\n")  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit          
    print("finally GPIO.cleanup()...\n")