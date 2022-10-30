import socket
import sys
import time
from tqdm import tqdm


port = 22221
new_socket = socket.socket()
host_name = socket.gethostname()
address = socket.gethostbyname(host_name)
# bind the socket.
new_socket.bind((host_name, 33331))  ## <======== REMEMBER ### MUST BE TUPLE
## <===== REMEMBER THIS ## MUST BE TUPLE ##
while True:
    print(f"[CURRENT]** {address} @{host_name}")
    name_input = input("[USER-ID]** Enter Username: ")
    new_socket.listen(1)  # listen to connections
    print(f"[LISTENING]...")
    #### !!!!!!!! INSERT TQDM !!!!!!!! ######
    # https://www.youtube.com/watch?v=FptVpIPhdpM

    # accept new connections
    conn, add = new_socket.accept()  # conn is connected to socket, add is client iP
    # print(type(add, conn)) # (TAKES INCOMING CONNECTION)
    print(f"[INCOMING] Connecting from [{add[0]}]")  ## calls the TUPLE estables earlier

    ## Store incoming data
    client = conn.recv(1024).decode("utf-8")  # .decode() # sets max at 1024 bytes
    print(f"[SUCCESS] {client} has connected")
    conn.send(name_input.encode())  # send client name inputed
    # deliver messages
    while True:
        message = input("ME : ")
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(f"{client} : {message}")
else:
    print("ASDFASDLFASD")


# sever_host = input('[CONNECT-IP]** Enter the sever IP for connection: ') ## pass back to socket.gethostname()
# cport = input('[CONNECT-PORT]** Enter the sever port for connection: ')
# name_input = input('[USER-ID]** Enter Username: ')
#

# print(dir(sys))
# print(dir())
