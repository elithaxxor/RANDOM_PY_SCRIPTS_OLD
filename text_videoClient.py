## UDP SERVER.PY
import os, sys, traceback, cv2, imutils, socket, time,datetime, base64
import threading, wave, pickle, struct, threading, queue, socket
import numpy as np
#import gpass
import datetime as dt
from datetime import datetime
from time import sleep
from Crypto.Cipher import AES


'''
Client Side- UDP Streamer / text room 
Set params for UDP -00 
use struct to onvert python bytes to C-datastructrs (arrays, vectors etc.) ]

'''

''' START UDP STREAM FOR VIDEO CHAT '''
BREAK = False
# play with buffer
BUFF_SIZE = 65535
port = 4921
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
client_name = socket.gethostname()
client_ip = socket.gethostbyname(client_name)
client_addr = ((client_ip, port)) ## set text port - 2 in args below


print(f'[+]- Enter The Server Address for Connection -[+]')
host_ip = input('')
message=b'' ## general message for input
print(f'[+]- Enter Screenname -[+]')
screen_name = input('')
screen_name.encode(encoding='utf-8')

host_name = socket.gethostname()
#host_name = socket.gethostname(server_ip)
socket.gethostbyname(host_name)

client_infoStr = f'[+] --[UDP-STREAM].. Starting client-server handshake. \n\t\t[{client_name}@{client_ip}:{port}]-- '
client_infoStr = str(screen_name) + str(client_infoStr)
payload_size = struct.calcsize("Q")  # 8bytes of memory
q = queue.Queue(maxsize=10)
vid=cv2.VideoCapture(0)


''' START CLIENT, OPEN VIDEO FRAME, GET USERNAME. CALC PAYLOADSIZE '''
def StartClient():
    def encrypt_256(msg_text):
        cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
        print(f'[+] Encryption Methology [{encypt_256}]')
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        return encoded
    def decrypt_256(msg_text):
        decoded = cipher.decrypt(baes64.b64decode(msg_text))
        return decoded
    WIDTH=500
    print(client_infoStr)
    print(f'[+] Client Is Searching for camera server now.. \n\t\t [{time.time()}]\n [{client_infoStr}]')

    while True:
        while(vid.isOpened()):
            try:
                print('[+].. Moving on', client_infoStr)
                ret, frame = vid.read()
                frame = imutils.resize(frame, width=WIDTH)
                q.put(frame)
                time.sleep(.001)
                print(f'[!] Frame Exit..  '), time.sleep(1.5), print('[+]--Working To Establish Connection--[+]')
                if ret is False:
                    print(f'[!]--Error in Camera Feed/Buffer, sys return [{ret}]')
                    time.sleep(.5)
                    sys.exit(1)
            except Exception as e:
                print(f'[-] -- [Error in make_vid function] -- [-] \n[{str(e)}][{traceback.print_exc()}] \n [{sys.exc_info()[2]}]')
                sys.exit(1)

        BREAK=True
        vid.release()


'''
* establish TCP connection for messaging 
* socket exceptions  fall under OSError 
* rather than redecalre port numbers, and confuse users *
* we will simply subtract 1 from the port for the client/server daemon connecta/accept 
* start at port X and subtract 1 from the start port for each daemon subsequltlu accessed.  
'''

def recv_msg():
    ''' Try Except Else '''
    def encrypt_256(msg_text):
        cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
        print(f'[+] Encryption Methology [{encypt_256}]')
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        return encoded
    def decrypt_256(msg_text):
        decoded = cipher.decrypt(baes64.b64decode(msg_text))
        return decoded
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #server_ip = socket.gethostbyname(server_name)
            client_socket.connect((host_ip, port))
            if client_socket.connect == 0:
                print('[+] Client found the server, attempting to connect.. '), time.sleep(.5)
            else:
                print('[!] Error with server connection, still listening. ')
        except Exception as ex:
            errname = type(err).name + str(ex) + traceback.format_exc()
            print(errname), sys.exit(1)
#'''Try Block Else'''
        else:
            udp_check = f'[+] --[UDP-STREAM].. \n[{client_name}@{client_ip}:{port}]-- '
            udp_check.encode(encoding='utf-8')
            data = b""
            payload_size = struct.calcsize("Q")
            while len(data) < payload_size:
                packet, host_addr = client_socket.recv(4096) ## reciving the pickle
                if not packet: break
                print('[+] Packet Recvd, ', packet)
            packed_msg_size = data[:payload_size] # controller for unpacking bytearray
            data=data[payload_size:] # set data to 8 byte
            msg_size=struct.unpack('Q', packed_msg_size)[0]
            while len(data)<msg_size: # or < BUFFER
                data+=client_socket.recv(4096) # recv buffer
            framed_data=data[:msg_size] # set teh frame to max size
            data=data[msg_size:] # read data back into the message
            frame=pickle.loads(framed_data)
            print(f'[{time.ctime()}]-- [MSG] {frame} \n')
            time.sleep(.001)

def send_msg():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recv_port = port-1
    client_socket.connect((host_ip, recv_port))
    if client_socket.connect == 0:
        print('[+] Client found the server, initiating text service.. '), time.sleep(.5)
        while True:
            print('[+] Client found the server, attempting to connect.. ')
            data=input('')
            a=pickle.dumps(data)
            message=struct.pack('q',len(a))+a ## REMEMBER ',' not '+'
            client_socket.sendall(message),time.sleep(.01)

''' 
    * use recvfrom UDP 
'''
def recv_vid():
    global start
    fps, start, frames2count, count = (0,0,20,0)
    message = b'Coolio' # may replace this with username
    client_socket.send(message, (host_ip, port)) # use UDP stream
    cv2.namedWindow('Client Video')
    cv2.moveWindow('Client Video', 10,400)
    cv2.putText('test window :: FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    while True:
        packet, server_addr = client_socket.recvfrom(BUFF_SIZE)
        data = base64.b64decode(packet) # take in packet
        npdata = np.fromstring(data,dtype=np.uint8) # read into byte array
        frame = cv2.imdecode(npdata,1)
        frame = cv2.putText(frame,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        cv2.imshow('Client Video', frame)

        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            client_socket.close()
            sys.exit(0)
        if count==frames_to_count:
            try:
                fps = round(frames_to_count / (time.time() - start), 1)
                start = time.time()
                count=0
            except:
                pass
        count+=1
        time.sleep(.0001)

def send_vid():
    socket_address = (host_ip, port-3)
    #socket_address = (server_ip, port-3)
    print('Server Listening.. ', socket_address)

    fps, start, frames_to_count, count = (0,0,20,0)
    cv2.namedWindow('SEND VID') # create video frame obj
    cv2.moveWindow('SEND VID', 10,30)


    while True:
        WIDTH=500
        while True:
            frame=q.get()
            encoded,buffer=cv2.imencode('.jpeg', frame,[cv2.IMWRITE_JPEG_QUALITY,80])
            message = base64.b64encode(buffer)
            client_sock.sendto(message,socket_address)
            frame = cv2.putText(frame,'FPS: '+str(round(fps,1)),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

            if count == frames_to_count:
                try:
                    fps = round(frames_to_count / (time.time() - start), 1)
                    start = time.time()
                    count = 0
                except:
                    pass

            cv2.imshow('SEND VID', frame)
            key = cv2.waitKey(1) & 0xff

            if key == ord('q'):
                client_socket.close()
                sys.exit(0)
            time.sleep(.0001)
            count += 1




def multi_thread():
    t2 = threading.Thread(target=StartClient)
    t3 = threading.Thread(target=recv_msg)
    t4 = threading.Thread(target=send_msg)
    t5 = threading.Thread(target=recv_vid)
    t6 = threading.Thread(target=send_vid)
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()


if __name__ == '__main__':
    multi_thread()













