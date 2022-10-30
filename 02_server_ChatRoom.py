import socket
import time
import pickle # for object serialization



#                                  PICKLES OBJECT SERIALIZATION DOCS                                                        #
# pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
# Write the pickled representation of the object obj to the open file object file. This is equivalent to Pickler(file, protocol).dump(obj).
#
# Arguments file, protocol, fix_imports and buffer_callback have the same meaning as in the Pickler constructor.
#
#
# pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
# Read the pickled representation of an object from the open file object file and return the reconstituted object hierarchy specified therein. This is equivalent to Unpickler(file).load().
#
# The protocol version of the pickle is detected automatically, so no protocol argument is needed. Bytes past the pickled representation of the object are ignored.


########## ------> PICKLE TRANCODES INTO BYTE FORMAT--> DO NOT FORGET TO SET CLIENT SIDE TO RECEIVE BYTE FORMAT

## TO HELP PREVENT OVER-BUFFER IN COMMUNICATION STRING: ##
# Start all messages with a header, telling the sys the size
# Create fixd leanth HEADER_SIZE and include the size of message

HEADER_SIZE = 10 ## set the header to 10 char
#try:
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





#
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)
