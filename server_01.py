import socket
import threading ## allows two things to happen at once

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
#SERVER = '192.168.50.86'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) ## must be a tuple
DISCONNECT_MESSAGE = '!DISCONNECT'

print(f'The IP address is {SERVER} at port {PORT}')
#binding socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr): ## handles individual connection client - server.
    print(f'New Connection Recieved From: {addr}')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode() ## tells us how long the message is
        if msg_length:
            msg_length = int(msg_length) ## converts to integer
            msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            break
        print(f'[{addr}] {msg}')
    conn.close()

def start(): ## handles new connections
    server.listen()
    print(f'[LISTENING] Server is litning on {SERVER}')
    while True: ## keep the server listening for new connections
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr)) #ceates continious application to keep running
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() -1}')
    pass

print('[SERVER] server is starting..')
start()
