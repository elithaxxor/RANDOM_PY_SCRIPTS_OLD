import socket
import sys
import time


socket_server = socket.socket()
server_host = socket.gethostname()
cip = socket.gethostbyname(server_host)
cport = 22221

print(f"[CURRENT]** {cip} @ {socket_server}")

server_host_input = input(
    "[CONNECT-IP]** Enter the server IP for connection: "
)  ## pass back to socket.gethostname()

##
name_input = input("[ID]** Enter an ID: ")

## connect to the socket and bind ports
socket_server.connect((server_host_input, 22221))

## receive the message from sever_host
socket_server.send(name_input.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(f"[CONNECTON] {server_name}, has joined..")

while True:
    message = (socket_server.recv(1024)).decode()  ## invoke .recv
    print(f"{server_name}, : {message}")
    message = input("[self] : ")  # stores 1024 bit to message
    socket_server.send(message.encode())

    #
