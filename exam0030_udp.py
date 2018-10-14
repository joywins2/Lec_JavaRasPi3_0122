'''
...116p.RaspberryPi takes a role of UDP server and receive UDP data through port No.
   and displays the received data including IP and Port No(111).
   whenever there is any receipt, RaspberryPi the iteration count + message + IP address.
   and stop at 5th.
'''

import socket 
#...create UDP socket for client. 
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#...client UDP data with all IP and Port No(111).
clientSock.bind(("", 111))

i = 0
while True:
    #...read data upto 1024 byte.
    data, svr_addr = clientSock.recvfrom(1024)
    #...recieved data and relative address.
    print(data.strip(), svr_addr)
    #...send server side data.
    clientSock.sendto(str(i) + " Raspberry server message ", svr_addr)
    if i == 5:
        break