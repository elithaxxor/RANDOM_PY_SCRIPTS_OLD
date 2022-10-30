import socket
import select
import errno
import sys
import json.decoder


# sdafsdf

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 22222


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
# set receive method to not block-- for debugging.
client_socket.setblocking(False)

USER_TAG = input("Username: ")
USERNAME = USER_TAG.encode('utf-8')
USERNAME_HEADER = f'{len(USERNAME):<{HEADER_LENGTH}}'.encode('utf-8')

print(USERNAME_HEADER)

client_socket.send(USERNAME_HEADER + USERNAME)

try:
    while True:
        message = input(f'[CLIENT] {USERNAME} >>')
        if message: # if there is amessage in he string
            message = message.encode('utf-8')
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)

        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print(f'[SYS]** Session Closed By Server.')
                sys.exit()

    username_length = int(username_header.decode('utf-8').strip())
    username = client_socket.recv(username_length).decode('utf-8')#

    message_header = client_socket.recv(HEADER_LENGTH)
    message_length = int(message_header.decode('utf-8').strip())
    message = client_socket.recv(message_length).decode('utf-8')


    print(f'{username} > {message}')

except IOError as e:
    print('Reading error: '.format(str(e)))
    sys.exit()
    pass
      
except exception as e:
    print('Reading error: '.format(str(e)))
    sys.exit()



#
