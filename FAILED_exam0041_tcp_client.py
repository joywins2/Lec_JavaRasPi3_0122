'''
...117p.set the IP and port(111) of RaspberryPi as a TCP client.
   connect to client.
   send data to client at receipt of response from client.
'''

import socket #...use socket library.

#...create TCP socket.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#...set the address and port of server.
client_socket.connect(("192.168.0.5", 111))

i = 0
while 1:
    #...receive upto 512.
    data = client_socket.recv(512)
    data = data.decode("utf-8")
    
    if(data == 'Q' or data == 'q'):
        #...exit socket.
        client_socket.close() 
        break
        
    else:    
        print("svr data : " + data + "\r")
        data = " pc TCP client data..."
        i += 1
        if(data == 'Q' or data == 'q' or i ==5 ):
            #...send client data.
            client_socket.send("Q/q/5 : " + data)
            #...exit socket.
            client_socket.close() 
            break
            
        else:
            #...send client data.
            client_socket.send(str(i) + " : " + data)