# chatroom in python
# Socket = socket is networking terminology, which serves as an intermediate connecting the
# application layer to transfer layer this package is presented at clint side and server side
# Sockets allow communication between two different processes on the same or different machines.

import socket
import sys
import time

# creating socket and retrieving the hostname
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

# bind the host and port
new_socket.bind((host_name, port))
print("Binding Successful")
print("This Is your IP address: ", s_ip)


# listening for connection
name = input("Enter Your Name: ")
new_socket.listen(1)

# accepting for connections
conn, add = new_socket.accept()
print("Received connection from", add[0])
print("connection established\nconnected from : ",add[0])

# storing incoming info
client = (conn.recv(1024).decode())
print(client + " connected")
conn.send(name.encode())

# delivering msg
while True:
    message = input("me: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)
