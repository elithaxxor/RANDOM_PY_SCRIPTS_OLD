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
