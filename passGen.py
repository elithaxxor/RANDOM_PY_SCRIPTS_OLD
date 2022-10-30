import time
import socket
import sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
print(f'[CURRENT]** {ip}')


sever_host = input('[CONNECT-IP]** Enter the sever IP for connection: ') ## pass back to socket.gethostname()
cport = input('[CONNECT-PORT]** Enter the sever port for connection: ')
name_input = input('[USER-ID]** Enter Username: ')

type(int(cport))#
#type(int(server_host))

print(f'The username is: {name_input} \n [CONNECTING..]{server_host} on [PORT] {cport}')

socket_server.send(name_input.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ':', message)
    message = input('Client : ')
    socket_server.send(message.encode())

#socket_server.connect(sever_host, cport)




