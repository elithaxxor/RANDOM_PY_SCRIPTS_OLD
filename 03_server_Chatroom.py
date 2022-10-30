import socket
import select
import sys
import select
import json.decoder



HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 22222

# use select.select to parse server/client information

#try:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) ## FOR DEBUGGING (TO FREE UP ADDRESS)
server_socket.bind((IP, PORT))
server_socket.listen()
client_list = [server_socket] # list of sockets, use later to append new users for select.select.
clients = {} # dictionary of clients<<--- remeber to clear clients and client_list together
######self.assert_(, 'message')



print(f'Listening for connections on {IP}:{PORT}...')
# Handles message receiving
def receive_message(client_socket):
    try:
        # read the header
        message_header = client_socket.recv(HEADER_LENGTH)
          ### if client sends socket.close(), the server will receive a message with 0 header,
          ### impliment check and return false to iniitiate close on server.
        if not len(message_header): ### to check if list is empty.
            return False

        ### calculate message lenght an dreturn back to function
        message_length = int(message_header.decode('utf-8').strip()) # decode the header, strip
        return {'header': message_header, 'data': client_socket.recv(message_length)} ## return message header and strips spaces from the side.

    except:
        return False

###  LOGIC ###
# We want a continous loop to send/recv messags
# use (socket) select.select to leverage  rlist, wlist, and xlist (read, write, error list)
# run loop through read_sockets--> to pass/fail for match between SERVER socket and CLIENT socket.

    #########


while True:
    read_sockets, _, exception_sockets = select.select(client_list, [], client_list)

    # 1. Incoming server handle
    # 2. Receive messager
    # 3. Server Broadcast Message
    for notified_socket in read_sockets: ## PASS/CHECK to determine match between read_ssockets from select.select()__
        if notified_socket == server_socket:  ### LISTEN IN FOR SERVER MESSAGE, accept server message
            client_socket, client_address = server_socket.accept() ## --> CREATES NEW SOCKET OBJECT, use for later.
            #client_socket = uniquue client object || clinet_address = IP/PORT
            CLIENT = receive_message(client_socket) ## // intended to accept client user_name <-- nCREATE FUNCTION LATER TO HANDLE CLIENT CLIENT NAME.
            if CLIENT is False: ## continue loop if no user name is sent.
                continue
            client_list.append(client_socket) ## use these two lines of coe togher, later.
            clients[notified_socket] = CLIENT ## save user name to to header address.
            #client_01 = CLIENT.decode('utf-8')
            print(f'Accepted new connection from {client_socket}:{client_address}, username: {CLIENT}')
    ## Establish incoming message, if its NOT from server
    # establish if message exists, or if client disconnects
    #
        else: # else, assuming socket is broadcasting message.
            MESSAGE = receive_message(notified_socket)
            if MESSAGE is False: ## check if string is empty: - if string is empty, close conection=
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                clients_list.remove(notified_socket) ## <-- use these two to gether when updaing client list
                del clients[notified_socket]
                continue


            CLIENT = clients[notified_socket] ## retrieve client name from client list to add to print message;
            print(f'Received message from {CLIENT["data"].decode("utf-8")}: {MESSAGE["data"].decode("utf-8")}')

            ### To broadcast message to clients:
            for client_socket in clients:
                if client_socket != notified_socket: ## PASS/FAIL to prevent sender from sending to self.
                    client_socket.send(CLIENT['header'] + CLIENT['data'] + MESSAGE['header'] + MESSAGE['data']).encode('utf-8')

    for notified_socket in exception_sockets:
        clients_list.remove(notfied_socket)
        del clients[notified_socket]









    #     pass
    #
    # except:
    #
    #     # Something went wrong like empty message or client exited abruptly.
    #     return False
    #
    #
    # #
