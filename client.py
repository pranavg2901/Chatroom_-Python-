
import socket
import sys
import time

# creating socket and accepting user input

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

# connection to the server
print("This is your IP Address:",ip)
server_host = input("Enter Friend IP address: ")
name = input("Enter Friend name: ")

socket_server.connect((server_host,sport))

# Receiving msg from server
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, "Has Joined...")
while True:
    message = (socket_server.recv(1024).decode())
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
