'''
...147p.
...image : https://drive.google.com/open?id=1IDz6MESchcOnECNremJxKGmR0ve0zxtL
'''

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
Low = 0
High = 1
Trig = 21
Echo = 20

distance1= [0, 0, 0, 0]
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.output(Trig, Low)

def distance_check():
    GPIO.output(Trig, High)
    time.sleep(0.00001) #...wait 10us.
    GPIO.output(Trig, Low)
    stop = 0
    start = 0
    #...wait until Echo is high, it is the moment of start.
    while GPIO.input(Echo) == 0:
        start = time.time()
    
    #...wait until Echo is low, it is the moment of stop.
    while GPIO.input(Echo) == 1:
        stop = time.time()
        
    duration = stop - start
    distance = (duration * 340 * 100) / 2
    return distance

def average_distance():
    distance = 0
    for i in range(0, 4):
        distance1[i] = distance_check()
        time.sleep(0.1)
    
    for i in range(0, 4):
        distance += distance1[i]
    distance = distance / 4
    return distance

try:
    i = 0
    while True:
        result_distance = average_distance()
        print("repeat = %d distance = %.1f cm"%(i, result_distance))
        time.sleep(0.1)
        i += 1
except KeyboardInterrupt:
    GPIO.cleanup()
    
    