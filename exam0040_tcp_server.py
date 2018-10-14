'''
...116p.set RaspberryPi as a TCP Server which can connect clients upto 5.
   the port of TCP Server is 111, and it will exit when received 'q' or 'Q' from client
   or received data 5times.
'''

import socket #...use socket library.

#...create TCP socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#...set every port of all TCP IP to 111.
server_socket.bind(("", 111))
#...get ready to wait for 5 connections from client.
server_socket.listen(5)
print("client use port 111")

try:
    i = 0
    while 1:
        #...accept request of conection from client.
        client_socket, address = server_socket.accept()
        print("client address : ", address)
        
        while 1:
            data = "RaspberryPi3 TCP server data"
            if(data == 'Q' or data == 'q'):
                #...send server data.
                client_socket.send(data)
                #...exit socket.
                client_socket.close() 
            else:
                i += 1
                #...send server data.
                client_socket.send(str(i) + ":" + data)
                print(" r0 recieved wait ")
                #...receive 512byte.
                data = client_socket.recv(512)
            
            #...if repeat 5times or 'Q'|'q'.
            if(data == 'q' or data == 'Q' or i == 5):
                #...exit socket.
                client_socket.close()                    
                print("exit socket...")
                break
            else:
                print("client data : " + data)
        
        break
    #...exit socket.
    server_socket.close()
except KeyboardInterrupt: #...Ctrl + C.
    print(" 1 sock closed")
    #...exit socket.
    server_socket.close()

#...exit socket.
server_socket.close()
    