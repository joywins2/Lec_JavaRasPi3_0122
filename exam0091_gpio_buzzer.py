'''
...159p.
   image : https://drive.google.com/open?id=10xISuzeEfse5K2X9B0SZEhgUU-ya2Gyi
'''

import RPi.GPIO as GPIO
import time

buzz20 = 20
buzz21 = 21
octav = [131, 147, 165, 175, 196, 220, 247, 262, 294, 330, 350, 
         392, 440, 494, 524, 588, 659, 699, 784, 880, 988, 1047]


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzz20, GPIO.OUT)
    
    global Buzz20
     
    Buzz20 = GPIO.PWM(buzz20, 440) #...set frequency to 440hz. 
    Buzz20.start(10)   #...set duty cycle to 10%.
    
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzz21, GPIO.OUT)
    
    global Buzz21
     
    Buzz21 = GPIO.PWM(buzz21, 440) #...set frequency to 440hz. 
    Buzz21.start(10)   #...set duty cycle to 10%.
     
def play_octav20():
    GPIO.output(buzz20, 1)
    time.sleep(0.5)
    print("play_octav...")
    
    for i in range(0, len(octav)):
        Buzz20.ChangeFrequency(octav[i])
        time.sleep(0.5)
    return

def play_octav21():
    GPIO.output(buzz21, 1)
    time.sleep(0.5)
    print("play_octav...")
    
    for i in range(0, len(octav)):
        Buzz21.ChangeFrequency(octav[i])
        time.sleep(0.5)
    return

    
try:
    setup()    
    play_octav20()
    print("playing Buzz20...")
    
    for i in range(100, 4000, 10): #...increase frequency 100hz~4000hz by 10Hz.
        Buzz20.ChangeFrequency(i)
        time.sleep(0.01)
    
    Buzz20.stop()      
    time.sleep(1)    

            
    play_octav21()
    print("playing Buzz21...")
    
    for i in range(100, 4000, 10): #...increase frequency 100hz~4000hz by 10Hz.
        Buzz21.ChangeFrequency(i)
        time.sleep(0.01)    
    
    Buzz21.stop()      
    time.sleep(1)
        
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C      
    print("except KeyboardInterrupt\n")
    GPIO.cleanup() # this ensures a clean exit
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!\n")
    GPIO.cleanup() # this ensures a clean exit
  
finally:         
    print("finally GPIO.cleanup()...\n")
    GPIO.cleanup() # this ensures a clean exit
    
GPIO.cleanup() # this ensures a clean exit