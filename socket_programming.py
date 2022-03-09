#The code below allow connection bewtween one server and only one client
#And also Only one transmittion is done here.
#To allow multiple and continous communication some approches like threading, or using asyncronious com .. should be implemented.
#echo-server.py

import socket

HOST = '127.0.0.1'
PORT = 65432 #port to listen (Non privileged ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_INET : IPv4, SOCK_STREAM : TCP type socket
    s.bind((HOST, PORT))   #bind the socket with an interface and define a port If host is not defined all available interfaces will be used
    s.listen()       #enable the accepting connections    
    conn, addr = s.accept()
    with conn:
        print(f"Connected buy {addr}")
        while True: #untill sender stops , read all data and echos back to sender
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            
# echo-server.py

# ...

# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
 

#Viewing Socket State            
#Above files can be run on same computer in different terminals
# python echo-server.py
# python echo-client.py

#To see the OS port status run
# netstat -an 
"""Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      0  *.65432                *.*                    LISTEN"""