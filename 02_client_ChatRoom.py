import socket
import pickle

# pickle dump - to encode, (send)
# pickle.load - to decode, (RECV)



HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## create user input for .gethostname
s.connect((socket.gethostname(), 1234))
print(f'DEBUG -- > SEE ADDRESS TO GET CREATE USER INPUT (FOR WAN CONNECTION){socket.gethostname()}')
#
# logic- creeate empty str for full message,
# then receive buffer in while loop. Filter out any byte <-
# then break & print full message (in while loop)
# append decoded MSG to MESSAGE
# check if MESSAGE is real, then print message

while True: ## Buffer
    MESSAGE = b'' ## transcode as byte data for pickle 
    NEW_MSG = True ## iniate loop. see 4 lines dow 'if state'
    while True:
        msg = s.recv(16)
        #print(MSG.decode("utf-8"))
        if NEW_MSG: ##
            print("[SYS] new msg len:", msg[:HEADER_SIZE]) ##
            msglen = int(msg[:HEADER_SIZE]) ## parse the message header
            NEW_MSG = False ## break out of if loop

            print(f'[SYS] Full Message Length: {msglen}')
            MESSAGE = NEW_MSG.decode('utf-8')
            print(f'[SYS] Message Length is: {len(MESSAGE)}')

        # KEEP LOOPING THRU 16BYTE BUFFER --> CHANGE LATER TO ALLOW LARGER MESSAGES
        if len(MESSAGE)-HEADER_SIZE == msglen:
            print(f'[SYS] Full Message Receved')
            print(MESSAGE[HEADER_SIZE:])
            NEW_MSG = True # CONTINUE LOOP
            MESSAGE = b'' # reset var string for line 19 --> b''for pickle dataframe



# ############## FROM PREVIOUS PROGRAM ---> IMPLIMENT THIS TO BREAK BUFFER IF BYTES ARE LESS THAN 0. SEE RECURSIVE LOOP IN SERVER.
#         if len(MESSAGE) < 0: ## breaks buffer if bytes received are less than 0. See loop in server code.
#             break
#     MESSAGE += MSG.decode('utf-8')
#     if len(MESSAGE) > 0:
#         print('f[MESSAGE]{MESSAGE}')
#



#
