'''
...95p.Blutooth Communication :
   98p.$sudo raspi-config ¡æ enable Serial.
   ¡é
   98p.disable login at Serial communication :
        /boot/cmdline.txt
        #...before : original :
        #dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=PARTUUID=d6dcdf52-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
        #...after : for bluetooth w/o login, deleted part : console=serial0,115200
        dwc_otg.lpm_enable=0 console=tty1 root=PARTUUID=d6dcdf52-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
   ¡é
   99p.$sudo apt-get install python-serial 
       download and test "blutooth terminal" at android play store.
   
'''
#---

'''
...image : https://drive.google.com/open?id=1YOB2l89ykcLzKtUbJsZ5RKzCD6DWfta6
   image : https://drive.google.com/open?id=1clA8bBWsjeo0mpUckbDH7oB3ArGgQApo 
...¡°ImportError: No module named serial¡±
   https://stackoverflow.com/questions/49916535/importerror-no-module-named-serial-after-installing-pyserial
   pip install serial
'''

import serial #...for Serial communication.
import time   #...for use of sleep().
import threading   #...for use thread.

#...set the definition of Seraial(/dev/ttyS0), speed 9600bps, timeout 0.5sec
#   to open the port of Serial.
s = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.5)

#...Thread class : always get ready to receive.
class bluetooth_receive_data(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)     #...init thread.
        self.stop_event = threading.Event() #...define thread a new event.
        print("bluetooth_receive_data has stared...")
        print("input anydata, exit is Ctrl+D...")
    
    def run(self): #...main of Thread class.
        threading.Thread.__init__(self)     #...init thread.
        
        #...always get ready to receive except 'stop event'.
        while not self.stop_event.is_set(): 
            temp_str = s.read(15)           #...read received data(Max 15 characters).
            if len(temp_str) > 0:           #...if there is data.
                print("received data = %s"%(temp_str))
                print('received data length = %d\n'%(len(temp_str)))
    
    def stop(self):           #...exit thread().
        self.stop_event.set() #...if thread exit, set the exit by event.set. 
        
r = bluetooth_receive_data() #...create Thread object.
r.start()   #...start thread.

while True: #...Bluetooth Main.
    try:
        str_data = input() #...get ready input from keyboard.
        if len(str_data) > 0: #...if there is sent data.
                print("sent data = %s"%(str_data))
                print('sent data length = %d\n'%(len(str_data)))
                s.write((str_data + "\r").encode()) #...send data.
    except KeyboardInterrupt: #...interrupt occurs at keyboard.
        s.close()        #...close port of Serial.
        time.sleep(0.01) #...wait 10ms.
        r.stop()         #...exit thread.
        
exit() #...exit main program.
                