import socket
import time
import pickle # for object serialization



HEADER_SIZE = 10 ## set the header to 10 char
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
#except:
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    # clientsocket.send(bytes('[SERVER**]- You have been connected to the SERVER', 'utf-8'))
    clientsocket.send(bytes(msg,"utf-8"))
    #d = {1:"hi", 2: "there"}
    msg = pickle.dumps(d)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
    print(msg)
    clientsocket.send(msg)

    msg = "[SERVER] Welcome to the server!"
    msg = f'{len(MSG):<{HEADERSIZE}} + MSG' ## left align lenght of MSG to the left and append MSG from ^
    print(f'DEBUGGING--> CHECK MESSAGE FORMATTING: {MSG}') #### DEBUG `delete later}     clientsocket.send(bytes("utf-8"))
    clientsocket.send(bytes(msg,"utf-8"))
    #clientsocket.close()
    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}" + msg
        print(msg)


