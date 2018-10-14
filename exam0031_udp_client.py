'''
...117p.this is a client source for PC.
   set svr_addr to the address of RaspberryPi and Port No(111).
   access and send data to server 5times and exit.
'''

import socket 
#...create UDP socket class. 
svrSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#...server IP and Port No(111).
svr_addr = ("192.168.0.5", 111)

#...client IP and Port No(112)
send_addr = ("192.168.0.4", 112)

i = 0
while True:
    print("svr_add = ", svr_addr)
    #...send server side data.    
    '''
    svrSock.sendto(str(i) + " PC client message ", svr_addr) #...before.
    ...TypeError: a bytes-like object is required, not 'str'
       https://stackoverflow.com/questions/33003498/typeerror-a-bytes-like-object-is-required-not-str
    #...after :
    '''
    msg = str(i) + " PC client message "
    msg = msg.encode("utf-8")
    svrSock.sendto(msg, svr_addr)
    
    #...read data upto 1024 byte.
    data, addr = svrSock.recvfrom(1024)
    
    #...recieved data
    print(data.strip(), addr)
    
    if i == 5:
        break