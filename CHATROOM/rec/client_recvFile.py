import os
import socket
import time
import sys


### ADD ARP - A as a function
### ADD FUNCTIO TO READ .TXT, .JSON, ON SCREEN
## add option to close or upload another file.


## Client
cport = 22222

# pass back to socket.gethostname()
#server_host = input('[SYSTEM]** Enter the server IP for connection: ')
server_host = "192.168.171.235"
client_name = socket.gethostname()
client_IP = socket.gethostbyname(client_name)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def mkdir():
    global cwd
    cwd = os.getcwd()
    path = str(cwd) + 'rec/'
    os.mkdir(path)
    print("[!] ", cwd + 'rec/')


def client_conn():
    try:
        socket.connect((server_host, 22222))
        print(f'[SYSTEM][CONNECTING..]{server_host} : {cport}')
        if socket.connect != True:
            sys.exit(1)
    except Exception as e:
        print(f'[SYSTEM]*[ERROR] Unable to connect to: {server_host} \n {e}')

    print(f'Hello {client_name}, you are connected on: {client_IP}')

    ## receive file paramaters
    file_name = socket.recv(1024).decode('utf-8')  # ('utf-8')
    file_size = socket.recv(1024).decode('utf-8')  # ('utf-8')
    print(
        f'[SYSTEM]** {file_name} is : {file_size} bytes \n [SYSTEM].. Initiating File Transfer. ')

    get_file(file_name, file_size)
# print(f'{file_name} is {file_size}')\\\


def get_file(file_name, file_size):
    ## open and write the file into BINARY
    cwd = os.getcwd()
    d_path = cwd + "/rec"
    with open(d_path + file_name, 'wb') as file:
        receive_count = 0
        print(type(file_size))
        print(file_size)

        #
        start_time = time.time()
        #print(start_time) # or start_time()
        ##
        while receive_count < file_size:
            data = socket.recv(8192)
            if not (data):  # may be unecessary.
                break
            file.write(data)
            receive_count += len(data)

        end_time = time.time()
    time_to_complete = end_time - start_time
    print(f'[SYSTEM] File Transfer Complete in {time_to_complete}')
    socket.close()


def main():
    #mkdir()
    client_conn()

if __name__ == "__main__":
    main()
