import threading
import socket

#host = '127.0.0.1' # local host
#port = 8081
#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((host, port))


port = 22221
server = socket.socket()
host_name = socket.gethostname()
address = socket.gethostbyname(host_name)
server.listen()

# bind the socket.
server.bind((host_name, 22221)) ## <======== REMEMBER ### MUST BE TUPLE
                                    ## <===== REMEMBER THIS ## MUST BE TUPLE ##
clients = []
client_names = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = clientv(1024).decode('utf-8')
            msg = message
            if msg.decode('utf-8').startwith('KICK'):
                if client_names[clients.index(client)] == 'admin' or client_names[clients.index(client)] == 'ADMIN':
                    dumbass_00 = msg.decode = msg.decode('utf-8'[5:0]) ####### CHECK STRING PLACEMENTS.... NEED TO REDO STRINGSS
                    kick_user(dumbass_00) # calls func to kick user
                else:
                    client.send("[SYS]** Command Was Refused.".encode(utf-8))

            elif msg.decode('utf-8').startwith('BAN'):
                if client_names[clients.index(client)] == 'admin' or client_names[clients.index(client)] == 'ADMIN':
                    dumbass_01 = msg.decode('utf-8'[4:0]) ##### CHECK STRING PLACEMENTS. NEED TO RE DO STRINGS
                    with open(ban_list.txt, 'a') as f:
                        f.write(f'{dumbass_01}\n')
                    print(f'{dumbass_01} was banned from the server')
                    ban_user(dumbass_01) # calls kick user func

            broadcast(message)

            print("[SYSTEM]... hello")
            broadcast(message)
        except:
            if client_names in clients:
                index = client_list.index(client)
                clients.remove(client)
                client.close()
                client_name = client_names[index] # pulls first index
                broadcast(f'[SERVER-BROADCAST]{client_name} left the chat.'.encode('utf-8'))
                client_names.remove(client_name)
                break

def receive():
    while True:
        client, c_address = server.accept()
        print(f"[SERVER-MSG] Connected with {c_address}") # or c_address[]
        print(f"[SERVER-MSG] Connected with {c_address[1]}")

        #client.send('ALIAS'.encode('utf-8')) ## sends client 'alias', so they know to add name
        client_name = client.recv(1024).decode('utf-8')

        with open('ban_list.txt', 'r') as f:
            bans = f.readlines()

        if (client_name+'\n' in bans):
            client.send('[SYS] You are banned.'.encode('utf-8'))
            #client.close()
            continue



        ## [LATER] - Rudementry Password implimention. Impliment HASH Algorothim LATER.
        ## set up admin / user privledges
        if client_name == 'ADMIN':
            client.send('[SYS] Enter Password: '.encode('utf-8'))
            password = client.recv(1024).decode('utf-8')
            if password!= 'LOVEYOU':
                client.send('[SYS]*  Wrong Password'.encode('utf-8'))
                client.close()
                continue ## use continue to keep server running. it will not run code below

        print(f'[SERVER-MSG] Client Username: {client_name}')
        broadcast(f'[SERVER-BROADCAST]{client_name} joined the chat!'.encode('utf-8')) # broadcast message to all
        client.send('[SERVER-MSG] Connected to the server!'.encode('utf-8')) # send messag eto cleint

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start() ## KEEPS THE PROGRAM RUNNING, CALLS FUNCTION HANDLE

print(f'[SYSTEM] Server running... IP: {host} Port: {port}')

def kick_user(name):
    if name in client_names:
        kick_index = client_names.index(name) ## creates a list of kicked clients
        kicked_client = client_names[kick_index]
        clients.remove(kicked_client)
        kicked_client.send('You were kicked by admin').encode('utf-8')
        kicked_client.close()
        client_names.remove(name) # remove from client list
        broadcast(f'{name} was kicked by admin'.encode('utf-8'))
        client.send

print(f'[SYS]** Server is listening')
receive()
