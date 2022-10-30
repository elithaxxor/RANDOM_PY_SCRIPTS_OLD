import os
import socket
import time
import sys
import select  ## OS LEEL loop
import io


## Server - RASPBERRY PI

PORT = 22222
client_name = socket.gethostname()
IP = socket.gethostbyname(client_name)

print(f"[SYS]connected to {client_name} with IP {IP} at port: {PORT}")
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


print(f"[SYS] Initiating connection..{socket}")
print(type(socket))

socket.bind((IP, PORT))
socket.listen(5)  # sets max que  to 5
print(f"[SYSTEM] {socket.getsockname()}")

## accepting connection
client, addr = socket.accept()
file_name = input("[SYSTEM] Enter File Name: ")
file_size = os.path.getsize(file_name)

print(f"[SYSTEM] connected to {client}, {addr}")
print(f"[SYSTEM] {file_name} is {file_size} bytes large")

## Send paramaters to client.
client.send(file_name.encode())
client.send(str(file_size).encode())


buffer = file_size
## open and read as binary for parsing
with open(file_name, "rb", buffering=30000) as file:
    send_count = 0
    send_start = time.time()

    # start loop
    while send_count != file_size:  # start loop
        data = file.read(8192)
        if not (data):
            break  # <- end of F/T
        client.sendall(data)
        send_count += len(data)

    send_end = time.time()

total_time = send_end - send_start
print(f"[SYSTEM] {file_name} Transfer Complete in: {total_time}")
socket.close()  # stop

#
#
#
# ##################################
# def linesplit(socket):
#     buffer = socket.recv(4096)
#     buffering = True
#     while buffering:
#     ## open and read as binary for parsing
#         with open(file_name, 'rb', buffering = 3000000000) as file: ## buffer by 3GB
#             send_count = 0
#             send_start = time.time()
#                 # start loop
#             while send_count != file_size: # start loop
#                 data = file.read(4096)
#                 if not (data):
#                 break #<- end of F/T
#                 client.sendall(data)
#                 send_count += len(data) ## byte format established line 63
#
#         send_end = time.time()
# total_time = send_end - send_start
# print(f'[SYSTEM] {file_name} Transfer Complete in: {total_time}')
# socket.close() # stop
#
#
#

#
#
#
# # sample buffer #
# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established.")
#     # clientsocket.send(bytes('[SERVER**]- You have been connected to the SERVER', 'utf-8'))
#     clientsocket.send(bytes(msg,"utf-8"))
#     #d = {1:"hi", 2: "there"}
#     msg = pickle.dumps(d)
#     msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
#     print(msg)
#     clientsocket.send(msg)
#
#     msg = "[SERVER] Welcome to the server!"
#     msg = f'{len(MSG):<{HEADERSIZE}} + MSG' ## left align lenght of MSG to the left and append MSG from ^
#     print(f'DEBUGGING--> CHECK MESSAGE FORMATTING: {MSG}') #### DEBUG `delete later}     clientsocket.send(bytes("utf-8"))
#     clientsocket.send(bytes(msg,"utf-8"))
#     #clientsocket.close()
#     while True:
#         time.sleep(3)
#         msg = f"The time is {time.time()}"
#         msg = f"{len(msg):<{HEADERSIZE}}" + msg
#         print(msg)


#
# def linesplit(socket):
#     buffer = socket.recv(4096)
#     buffering = True
#     while buffering:
#         if "\n" in buffer:
#             (line, buffer) = buffer.split("\n", 1)
#             yield line + "\n"
#         else:
#             more = socket.recv(4096)
#             if not more:
#                 buffering = False
#             else:
#                 buffer += more
#     if buffer:
#         yield buffer
