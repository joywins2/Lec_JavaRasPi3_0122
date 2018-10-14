'''
...169p.173p.
   image : https://drive.google.com/open?id=1ynzyEaXqpYgodZBAvb1P6y0xc_N90tSC
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


class DHT11:
    pin = 4
    temperature = -1
    humidity = -1 
    
    def __init__(self, pin, temperature=-1, humidity=-1):
        self.pin = pin
        self.temperature = temperature
        self.humidity = humidity 
    
    def read(self):
        #...RaspberryPi set pin to OUT/HIGH for sending a signal of start.
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.05)        #...set interval for 50ms after sending signal.
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.018)    #...wait for 18ms.
        
        #...For receiving data from sensor, set pin to IN/PULL_UP.
        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_UP)        
        
        #...get 40 data bit by reading data.
        #...get data by calling collect_input() to read by 1bit and save data into array.
        data= self.collect_input()
        
        #...get the length of data pull up by calling parse_data_pull_up_lengths().
        pull_up_lengths = self.parse_data_pull_up_lengths(data)
        #...check the read data and if it is smaller than 40, return 0.
        if len(pull_up_lengths) != 40:
            result = 0
            self.temperature = 0
            self.humidity = 0
            return result
        
        #...get the length of section which is pull up into bits.
        bits = self.calculate_bits(pull_up_lengths)
        #...convert to byte.
        the_bytes = self.bits_to_bytes(bits)
        
        #...check the value valid.
        checksum = self.calculate_checksum(the_bytes)
        #...if calculated value and recieved value are not equal.
        if the_bytes[4] != checksum:
            result = 0
            self.temperature = 0
            self.humidity = 0
            return result
        result = 1
        self.temperature = the_bytes[2]
        self.humidity = the_bytes[0]
        return result
    
    #...read by 1bit for 100times.
    #...save the info of bit when GPIO is PULL UP/DOWN into array.
    #...data is 0 or 1 when PULL UP.
    def collect_input(self):
        #...var of count shows no change in status.
        unchanged_count = 0
        max_unchanged_count = 100
        last = -1
        data = [] #...list var.
        while True:
            #...read one bit and save it into list var.
            current = GPIO.input(self.pin)
            data.append(current)
            
            #...if it is different from the previous read bit.
            if last != current:
                unchanged_count = 0
                last = current
            else:
                #...if no change in read bit, increase 1.
                unchanged_count += 1
            if unchanged_count > max_unchanged_count:
                 break 
        return data
    
    #...get the length of pull up from read data.
    def parse_data_pull_up_lengths(self, data):
        STATE_INIT_PULL_DOWN = 1 #...the initial pull down state.
        STATE_INIT_PULL_UP = 2   #...the initial pull up state.
        STATE_DATA_FIRST_PULL_DOWN = 3   #...the 1st pull down state.
        STATE_DATA_PULL_UP = 4
        STATE_DATA_PULL_DOWN = 5
        state = STATE_INIT_PULL_DOWN
        #...list var sotres the length of pull up.
        lengths = []
        current_length= 0
        #...check pull up/down as long as the length of data.
        for i in range(len(data)):
            current = data[i]
            current_length += 1
            if state == STATE_INIT_PULL_DOWN:
                if current == GPIO.LOW:  #...initial PULL DOWN.
                    state = STATE_INIT_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_INIT_PULL_UP: 
                if current == GPIO.HIGH:  #...initial PULL UP.
                    state = STATE_DATA_FIRST_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_FIRST_PULL_DOWN: 
                if current == GPIO.LOW:  #...initial PULL DOWN.
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_UP: 
                if current == GPIO.HIGH:  #...data pull up, check the length of pull up.
                    current_length = 0
                    state = STATE_DATA_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_DOWN: 
                if current == GPIO.LOW:  #...pull down, save the previous length of pull up.
                    lengths.append(current_length)
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
        #...return all received data.
        return lengths
        
    #...get the length of section which is pull up.
    def calculate_bits(self, pull_up_lengths):
        shortest = 1000
        longest = 0
        for i in range(0, len(pull_up_lengths)):
            length = pull_up_lengths[i]
            if length < shortest:
                shortest = length
            if length > longest:
                longest = length
        #...get the average of pull up period.
        halfway = shortest + (longest - shortest)/2
        bits = []
        for i in range(0, len(pull_up_lengths)):
            bit = False     #...data 0.
            if pull_up_lengths[i] > halfway:
                bit = True  #...data 1.
            bits.append(bit)#...save bit data.
        return bits
    
    #...convert bit into byte.
    def bits_to_bytes(self, bits):
        the_bytes = []
        byte = 0   #...initial value.
        for i in range(0, len(bits)):
            byte = byte << 1   #...raise the location of existing value.
            if(bits[i]):
                byte = byte|1  #...if bit is 1.
            else:
                byte = byte|0  #...if bit is 0.
                
            if((i+1)%8 == 0):  #...calculate again byte.
                the_bytes.append(byte)   #...save byte converted value.
                byte = 0   #...init new byte.
        return the_bytes   #...return byte value.
    
    #...check received data valid.
    def calculate_checksum(self, the_bytes):
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255


#...create DHT11 class and set the pin.
data = DHT11(pin = 4)

#while True:
result = data.read()
if result:
    print("Temperature;%dC"%data.temperature)
    print("Humidity;%d% %"%data.humidity)
 #   time.sleep(1)
 
GPIO.cleanup()    
        
        
                
        
        
    