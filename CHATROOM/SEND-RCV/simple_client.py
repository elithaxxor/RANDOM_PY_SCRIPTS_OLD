
import socket
import threading

server_host = input('[CONNECT-IP]** Enter the server IP for connection: ') ## pass back to socket.gethostname()
cport = input('[CONNECT-PORT]** Enter the sever port for connection: ')
client_name = input('[USER-ID]** Enter Username: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_host, int(cport)))
def receive():
    while True:
            message = client.recv(1024).decode('utf-8')
            #if message == 'ALIAS':
            client.send(client_name.encode())
