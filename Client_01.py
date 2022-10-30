import socket
import threading ## allows two things to happen at once


FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
#SERVER = '192.168.50.86'
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '192.168.50.129'
ADDR = (SERVER, PORT) ## must be a tuple
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    send_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))

send("Hello World!")
input()
send(DISCONNECT_MESSAGE)
input()


print(dir(socket)
print(dir(threading))
