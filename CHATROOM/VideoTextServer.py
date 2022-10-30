## UDP SERVER.PY
import os, sys, traceback, cv2, imutils, socket, time, datetime, base64
import threading, wave, pickle, struct, threading, queue, logging
import numpy as np
#import dirty_hasher as DH
# import pyaudio
from datetime import date
from Crypto.Cipher import AES
import base64
import time
import concurrent.futures




'''
* threaded all functions, that way each daemon (function) is constnatly listening for connection.
* socket.accept must be global and listening. or constanlty listening and encapsulated. 
* ATTEMMPT TO ESTABLISH SYN SYN-ACK CONNECTION VIA TCP, THEN SHIFT TO UDP FOR DATA TRANSFER 
* pip install PyAudio
* see (socket.opt)# https://notes.shichao.io/unp/ch7/
## reading image from memory buffer ### 
* cb2.imencode os used to read an image from memory buffer. 
* cv2.imcode, cv2.imenencode 
*** Since max connections (socket.listen() is set to 5, the que will be set to 10.
* 2 per user at max capacity with each one running texting and video deamon. 
* q = queue.Queue(maxsize=10)

Constructor for a FIFO queue (FIRST IN FIRST OUT). (task priority for openCV frames) 

'''

'''
1. start udp for server, TCP for chat  
2. log info
3. load video camera/send frame
4. start UDP daemon (send/recv) 
5. Text - TCP Socket 
Upload - UPD
'''

'''
To do list: 
Inintiate Camera Feed and frame on both ends. 
to complete encryptins and ASYNCIO
'''
'''
* conn is sock object, use addr to get client name 
* use bind to create socket object, canot do as client 
* then use listen to listen for host, outside of loop.
* create loop 
'''
'''
* Quick functions that may be usefull leater on. 
* inet_aton(ip) -- converts the ip into c-type data structure, accepted anywhere.
* take a stirng and makes it an IP. 
'''
def ip2int(ip):
    '''converts IP to interger'''
    return int(socket.inet_aton(ip).encode('hex'),16)
def in2ip(ip):
    '''converts interger to IP format'''
    return socket.inet_ntoa(hex(ip)[2:].decode('hex'))
def check_q(q):
    print('Queue Size: ', queue.Queue.qsize(q))
    print('Empty Queue? : ',queue.Queue.empty(q))
    print('Full Que? ', queue.Queue.full(q))

q = queue.Queue(maxsize=10)
print('Empty Queue? ', check_q(q))


'''[1]
* Establish Server Params. [UDP Video Stream].
* Do not forget to open ports on router and firewall. 
* UNIX/DARWIN systems - 
- sudo ufw allow 20/tcp
- sudo ufw allow 21/tcp
- sudo ufw allow 990/tcp
- sudo ufw allow 40000:50000/tcp
- sudo ufw status
** mangle ttl if you want to be sexy **
(defaults vary per OS, Unix based OS is usally 65, I beleive. 
MANGLE TTL 
iptables -t mangle -I POSTROUTING 1 -j TTL --ttl-set 66
'''


port = 4921
BUFF_SIZE = 65536  # play with buffer
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
'''     
    * to change buffer 
    * socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, newSizeInBytes)
    * socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, newSizeInBytes)
'''
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
more_hostInfo = socket.gethostbyname_ex(host_ip)
host_interfaces = socket.getaddrinfo(host=host_name, port=port, family=socket.AF_INET)
host_addr=((host_ip, port))
#host_IPint = ip2int(host_ip)
# host_IPconvert = in2ip(host_ip)
ipStat = socket.getaddrinfo(host_ip, port)
#host_nameinfo = socket.getnameinfo((host_ip, port))
#h_ip = ip2int(ip)
host_Localdomain = socket.getfqdn()
host_domain = socket.getfqdn(host_ip)

print(f'Hostname- ', host_name)
print(f'Host ip- ', host_ip)
print(f'more_hostInfo- ', more_hostInfo)
print(f'full address- ', host_addr)
print('host_interfaces', host_interfaces)
#print('IP as hex', h_ip)
print('host domain', host_domain)
print('host lcoal domain', host_Localdomain)

'''[2]
    *Establish connection 
    *Get Info on active connections, 
    *Log user activty in .txt (or .json?) set (max users to 5.) 

    *ask for screenname and concatinate it to msg system 
    *Create Fstring
    *create list of active users to broadcast to later.
'''
server_socket.bind((host_ip, port)) #creates object with host and port
#server_socket.listen(5)
server_info = f'[+] --[{host_ip}:{port}]-- {datetime}::[{time.ctime}] '
print(f'[+] Server Listening [{time.time()}]]\n [{server_info}]')


'''
active_clients = []
client_info = []
client_name = socket.gethostbyaddr(str(host_ip)) # get clieint name
more_clientInfo = socket.gethostbyname_ex(client_ip)
client_interfaces = socket.getaddrinfo(host=str(client_name), port=port, family=socket.AF_INET)
# client_address = ((client_ip, ))
client_IPint = ip2int(client_ip)
client_IPconvert = int2ip(client_ip)
client_domain = getfqdn(client_ip)

print('client domain', client_domain)
print('X' * 50)
print('client_IPint', client_IPint)
print('client_IPconvert', client_IPconvert)
print(f'Hostname- ', host_name)
print(f'Host ip- ', host)
print(f'more_clientInfo- ', more_clientInfo)
print(f'client_nameinfo- ', client_nameinfo)
print('client_interfaces', client_interfaces)
print('client_IPconvert', client_IPconvert)
print('client_IPconvert', client_IPconvert)

server_log=f'SERVERLOG {str(time.ctime())} + {str(date.today())}'
with open(server_log, 'a') as f:
    f.writelines(str(active_clients) + f'{(date.time())}' +f'{(time.ctime())}')
    f.write('client \n:' + str(client_name) + client_ip)
    f.write('client info: \n' + str(more_clientInfo))
    f.write('more client info: \n' + str(more_clientInfo))
    f.write('client name info: \n' + str(more_clientInfo))
'''

''' [3]
    *encode premade srver messsages in base64 
    *make server_info a constant base64str for easier passing/readibility.

    *Sort thru AES hash (its encapsualted in this function) 
    *take returned AES hash and encode it again, b64 
    ** do not encyrpt 
    
    $$$$ HASH FIRST, THEN ENCODE $$$ (reverse it, and your f**d)
'''
def start_listener():
    def encrypt_256(msg_text):
        cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
        print(f'[+] Encryption Methology [{encypt_256}]')
        # encoded = base64.b64encode(cipher.encrypt(msg_text))
        encoded = base64.b64encode(cipher.encrypt(msg_text)).hexidigest()
        print('[+] Encoded -', encoded)
        return encoded
    def decrypt_256(msg_text):
        decoded = cipher.decrypt(baes64.b64decode(msg_text))
        return decoded

    client_list = []
    log_data = []
    print('X' * 50)
    server_info = f'[+] --[{host_ip}:{port}]-- {date.today}::[{time.ctime}] '
    HEADER = encrypt_256(server_info)
    a = pickle.dumps(HEADER)
    msg = struct.pack('Q', len(a))+a
    HEADER.encode(encoding='utf-8')

    print('X' * 50)
    print(f'[+] Server Listening [{time.time()}]]\n [{server_info}]')
    print('Client-Interface: \n', client_interfaces)
    print('Server-Interface: \n', host_interfaces)
    print('256 AES Header', HEADER)
    print('X' * 50)

    send_socket=socket.socket()
    send_socket.bind((host_ip, int(port-1)))
    send_socket.listen(5)

    assert msg <= BUFF_STREAM
    try:
        client_socket.sendall(msg)
        if client_socket.sendall == 0:
            print(f'[+] Sent Message to :: [{client_addr}]')
        print('[!] Error sending header')
    except Exception:
        errname = type(err).name
        print(errname, Exception)
        raise Exception + errname -- start_listener()


def start_stream():
    start = time.ctime()
    try:
        vid = cv2.VideoCapture(1)
    except Exception:
        print(Exception, traceback.format_exc())
        raise Exception + 'Cannot Open Video Camera'

    print(f'[+] Stream Started [{start}]]\n\t\t [{server_info}]')
    WIDTH = 500

    if vid.isOpened() == False:
        print(vid.isOpened())
        print('[!] Camera is already in use, or device/OS permissions need to be changed. [!]')

    while vid.isOpened:
        try:
            print(f'[+]--Initiating Camera Frame--[+]\n{[start]}')
            ret, frame = vid.read()
            if ret == False:
                print(f'[!]--Error in Camera Feed, sys return [{ret}]')
            frame = imutils.resize(frame, width=WIDTH)
            q.put(frame) ## store into the frame
            check_q()

            time.sleep(.001)
            print('[-] Chat Closed ')
            time.sleep(.0001)
            vid.release()
            BREAK = True
            break

        except OSError as e:
            print('Error loading frame frame','\n', e)
            sys.exit()
        except oserror:
            print('Error sending frame ')
            sys.exit()

        except exception as e:
            print(f'[-] -- [Error in make_vid function] -- [-] \n{str(e)}[{traceback.exc()}] \n [{sys.exc.info()[2]}]')
            sys.exit(1)
def b64_encoder():
    encoded = cv2.namedWindow('[+] [B64-ENCODER STARTED] ')
    print('Encoded_value', Encoded)
    return encoded
def Queue_Info():
    Queue.qsize()
    Queue.empty()
    Queue.full()
    print('Empty Queue? ', Queue.empty(q))
    print('Empty full? ', Queue.full(q))
    print('queue Size? ', Queue.qsize(q))


def send_vid():
    global e, err

    def encrypt_256(msg_text):
        cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
        print(f'[+] Encryption Methology [{encypt_256}]')
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        return encoded
    def decrypt_256(msg_text):
        decoded = cipher.decrypt(baes64.b64decode(msg_text))
        return decoded

    fps, start, frames2count, count = (0, 0, 20, 0)
    cv2.namedWindow('[+] [OUTBOUND-FRAME] ')
    cv2.moveWindow('[+]) [OUTBOUND-FRAME ]', 400, 30)

    '''
        * try - else block, recv from buffer
        * check if iP is valid  -- then pass msg AFTER verifcation to ELSE block. 
        * read message, start frame delivery 
    '''
    try:
        msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
        print(f'[+] Attempting to Connect: [{client_addr}] :: [{time.ctime()}]')
        client_ip = ip2int(ip)
        if client_ip < 1:
            print(f'[-] Error in reading client\s address. [{msg}] :: [{client_addr}]:: [RESETTING SERVER]')
            sys.exit(1)
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            sleep(1)
            raise ('No data available')
        else: ## any error aside from buffer over flow
            print(str(e))
    except Exception as e:
        errname=type(err).name
        print(errname, Exception)
        raise

    else:
        msg = decrypt_256(msg)
        print(f'[+] [RECEIVED-MSG] {time.ctime()}[+] [ENCODED] [{msg}] [+] [DECODED] [+] [{base64.b64decode(msg)}]')
        WIDTH = 500
        while True:
            Queue_Info()
            frame = q.get()
            encoded, buffer = cv2.imencode('.jpeg', fraem, [cv2.IMWRITE_JPEG_QUALITY, 80])
            message = base64.b64encode(buffer) ### maybe pickle???
            print('[+] Encoded Buffer')
            message = b'[+] Sending Frames..   '
            server_socket.sendall(message, client_addr)
            if server_socket.sendto is True:
                print(f'[+] Sent Message to :: [{client_addr}]')

            try:
                frame = cv2.putText(frame, 'FPS: ', +str(round(fps, 1)), (10, 40), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 255), 2)
            except:
                print('[!] Frame Exception', frame)
                pass

        # calculate fps
            if int(count) == frames_to_count:
                try:
                    start = time.ctime()
                    fps = round(frames_to_count / int((time.time()) - int(st)), 1)
                    count = 0
                except Exception:pass
                else:
                    end = (start-time.ctime())
                    count += 1
                    cv2.imshow(f'[+]Transmitting Video [{end}] \n[+]*FPS [{fps}]\n[+]**{frame}')
                    print(f'[+]--SERVER-STATs--[+]\n\t\t[+]*Fps [{fps}]\n\t\t[+]*Fps [{frame}]')

                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        print(f'[+]End Transmisson  [{end}] \n[+]*FPS [{fps}]\n[+]**{frame}')
                        client_socket.close()
                        sys.exit(1)

''':cvar
* .sendall works better with TCP, especilly when given buffers/streams

*** LIST IS NOT MUTABLE, SOCKETS USE STRING/BYTE ALOT. 
>>> line = 'Kong Panda'
>>> index = line.find('Panda')
>>> output_line = line[:index] + 'Fu ' + line[index:]
>>> output_line
'Kong Fu Panda'

while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!")
    data = clientsocket.recv(1024).decode()
    print (data)
    r='REceieve'
    clientsocket.send(r.encode())
    
    USE  recvfrom() for connetion less -- allows user to retrieve sending source. 
    
'''
'''
error catching sample: 
    try:
        print(f'[+] [INBOUND MSG] [{time.ctime()}]\n [+].. Connection recvd from [{client_addr}]')
        msg, client_addr = server_socket.socket.recvfrom(BUFF_SIZE)
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            sleep(1)
            print('No data available')
        else: ## any error aside from buffer over flow
            print(str(e))
    else:
        msg = decrypt_256(msg)
        print(f'[+] [RECEIVED-MSG] {time.ctime()}[+] [ENCODED] [{msg}] [+] [DECODED] [+] [{base64.b64decode(msg)}]')
    WIDTH = 500
    
    
     
        :: Start new listener OBJ: (send_socket) ::
        * to read data, first decode THEN decrypt. 
        * encrypting, encode, serealize, compare bytes, then sending the packet
                    
                    
                    ---- TEMPLATE ---
                    data = input ()
                    a = pickle.dumps(data)
                    message = struct.pack("Q",len(a))+a
                    client_socket.sendall(message)
                    cnt+=1
'''
def send_msg():
    global USER
    def encrypt_256(msg_text):
        cipher = AES.new(secret_key, AES.MODE_ECB)  # never use ECB in strong systems obviously
        print(f'[+] Encryption Methology [{encypt_256}]')
       # encoded = base64.b64encode(cipher.encrypt(msg_text))
        encoded = base64.b64encode(cipher.encrypt(msg_text)).hexidigest()
        print('[+] Encoded -', encoded)
        return encoded
    def decrypt_256(msg_text):
        decoded = cipher.decrypt(baes64.b64decode(msg_text))
        return decoded

    client_list = []
    log_data = []
    send_socket=socket.socket()
    send_socket.bind((host_ip, int(port-1)))
    send_socket.listen(5)
    #client_socket, addr = send_socket.accept()
    while True:
        conn, client_ip = server_socket.accept()
        if conn == 0:
            print(f'[+] [INBOUND CONNECTION] [{time.ctime()}]\n [+]..From [{client_ip}]')
            continue

    '''
        * User-name logic. 
        * recv data from UDP stream
        * start bufferstream with USER at byte 0  
        * keep buffering data < payload size
    '''
    send_count = 0
    data = b''
    payload_size = struct.calcsize("Q")
    ''' 
        ** use payload_size as payload size controller. payload_size set to 8byte.  
    '''
    if send_socket:
        try:
            while data < payload_size:
                user, packet = server_socket.recvfrom(BUFF_SIZE)#.decode('utf-8')
                print(user).decode('utf-8'), print(packet).decode('utf-8'), print(data).decode('utf-8')
                if not packet: sys.exit(0)

                data+=packet ## concatinate recieved packet to empty byte array.
                assert data <= packet, f"[!] Possible Overflow Error [!] Data: [{len(data)}] ::\n\n max payload [{packet}]"

                packed_msg_size = data[:payload_size] ##  limiter for 8 bytes
                data = data[payload_size:] ## reads teh first 8 bits back into data. keeps fro  over flowing
                msg_size = struct.unpack("Q", packed_msg_size)[0] ## read entire message size

                assert data < msg_size
                assert data < payload_size, f"[!] Possible Overflow Error [!] Data: [{len(data)}] ::\n\n max payload [{payload_size}]"
                if data > payload_size:
                    print(f'[+] Data outside buffer range'), sys.exit(0)
                while len(data)<msg_size: ## if this works, it fills data up to 8 bytes
                    data+= send_socket.recvfrom(BUFF_SIZE).decode('utf-8')

            print(f'[+]{data} added')
            print(data).decode('utf-8') ## decode may be redundant
            client_list.append(data)
            data = decrypt_256(data).decode('utf-8')
            log_data.append(data + '\n')
            log_data.append(data + '\n')

        except OSError as ose:
            errname = type(err).name
            print('Error loading frame frame-- ',errname,'\n', ose,'\n',traceback.format_exc())
            raise
        except Exception as e:
            errname = type(err).name
            print(f'[-] -- [Error in make_vid function] {errname}-- [-] \n{str(e)}[{traceback.exc()}] \n [{sys.exc.info()[2]}]')

        '''
            * Set Up Header 
        '''
        while True:
            try:
                payload_size = struct.calcsize("Q")
                send_Start = f"{'X' * 50}, '\n', '[+]--[+] [{USER}]Sending Message [+]\n\t[+]--[+]"

                print(HEADER_SIZE), print(payload_size)
                HEADER=encrypt_256(send_Start)
                print(type(HEADER))
                HEADER_SEND = struct.pack("Q", len(HEADER)) + HEADER
                print(type(payload_size))
                print(type(HEADER_SEND))

                assert HEADER_SIZE <= BUFF_SIZE
                if client_socket:
                    try:
                        client_socket.sendall(HEADER_SEND)
                        raise Exception('UNABLE TO SEND HEADER')
                    except Exception:
                        print('UNABLE TO SEND HEADER')

                ''' 
                    ** START INPUT SEQUENCE 
                '''
                print('X' * 50, '\n', f'[+] ---[INPUT]: ')
                to_client = input()
                print('[+].. .'), time.sleep(.3)
                a = pickle.dumps(to_client)
                message = struct.pack("Q", len(a)) + a
                client_socket.sendall(message)
                send_count += 1
                print(f'[+] [{message_count}] Message Sent [{ctime.time()}]')
                time.sleep(0.01)

            except Exception:
                typERRs = str('Error in Parsing Headers')
                errname = type(err).name + typeERRs
                print(errname)
                raise Exception + errname + send_msg()

    raise Exception('UNABLE TO SEND HEADER')



print('UNABLE TO SEND HEADER')

'''
while var client_data 
global payload_size to red  uce clutter and cpu overwork 

'''

def recv_msg():
    recv_socket = socket.socket()
    recv_socket.bind((host_ip, int(port-2)))
    recv_socket.listen(5)
    client_sock, addr = client_socket.accept()
    payload_size = struct.calcsize("Q")
    '''
         * Set Up Header 
     '''
    recv_Start = f"{'X' * 50}, '\n', '[+]--[+] Accepted Message [+]\n\t[+]--[+]"
    recv_Start = pickle.dumps(recv_Start)
    HEADER_SIZE = struct.calcsize(recv_Start)

    print(HEADER_SIZE), print(payload_size)

    HEADER = encrypt_256(send_Start)
    HEADER = pickle.dumps(HEADER)
    print(type(HEADER))
    HEADER_SEND = struct.pack("Q", len(HEADER)) + HEADER
    print(type(payload_size))
    print(type(HEADER))

    payload_size = struct.calcsize("Q")
    HEADER_SIZE = struct.calcsize(send_Start)
    print(HEADER_SIZE), print(payload_size)
    HEADER = encrypt_256(send_Start)
    HEADER = pickle.dumps(HEADER)
    print(type(HEADER))
    HEADER_SEND = struct.pack("Q", len(HEADER)) + HEADER
    print(type(payload_size))
    print(type(HEADER))

    assert payload_size <= HEADER_SIZE,  f"[!] Possible Overflow Error [!] Data: [{len(HEADER)}] ::\n\n max payload [{payload_size}]"
    if payload_size <= HEADER_SIZE:
        client_socket.sendall(b'[+]-Encoded and AES cypther- [+],\n', HEADER)
    print(f'[+]-- PAYLOAD [{payload}],\n\t\t[+] [PAYLOAD-SIZE] [{len_payload}]') ## shhould be max 256
    '''
       * set up listener to receive errors. 
       * REUSE b'data to clear header and buffer text. 
        * append buffer into  b'data' till it hits payload size (8 byte)  
    '''
    count = 0
    data=b''
    while True:
        while len(data) < payload_size:  ##
            try:
                buffer = client_socket.recv(4096)  # set buffer
                if not buffer: break
                data += buffer ## append recv_sock to empty data
            except Exception:
                raise Exception

        packed_msg_size = data[:payload_size]
        data=data[payload_size:]
        msg_size = struct.unpack('Q', packed_msg_size)[0]
        print(type(payload_size))
        print(len(msg_size))

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
            frame = pickle.loads(client_data)
            print(f'frame len {(len(frame))}')

            while len(client_data) < msg_size:
                sockStream = client_socket.recv(4 * 1024)
                frame_data = client_data[:msg_size]
                print('\nX' * 50)
                print(f'[MSG] from client')
                print(sockStream)
                print(frame_data)

                if (str == "exit1" or str == "EXIT1"):
                    kill_app = f'[+] [{USER}] sent kill command, sys.exit(1)'
                    print(kill_app)
                    kill_app.encode(encoding='utf-8')
                    break
                break

                "N:", s.recv(1024).decode()
                client_socket.close()
            print('[fin]')


'''
 reset buffer (port), set server socket to UDP, non-handshake stream 
 set listener for buffer and use byte64 to encode  
'''


def recv_vStream():
    try:
        BUFF_SIZE = 65536
        cv2.namedWindow(f'[+] --[INCOMING VIDEO STREAM]-- {server_info} --[+]')
        cv2.moveWindow(f'[+] --[INCOMING VIDEO STREAM]-- {server_info} --[+]', 400,300)
        fps, start, frames_to_count, count = (0, 0, 20, 0)

        server_socket = socket.socket(socket.AF_INET, socket.DOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
        server_socket.bind((host_ip, int(port-3)))
        print(f'[VIDEO PARAMS] || FPS [{fps}] || frames_to_count [{frames_to_count}]|| FPS [{count}] ')


        while True:
            packet, addr = server_socket.recvfrom(BUFF_SIZE)
            data = decrypt_256(packet)  ### TESTING ---> COMMENT OUT LATER FOR FINAL TEST.
            data = base64.b64decode(eData)
            frame_data = np.fromstring(data, dtype=np.uint8) ## convert to np array for image proessing

            frame=cv2.imdecode(npdata,1) # read from buffer
            frame=cv2.putText(frame,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
            frame=cv2.imshow("[+] Buffering Frames [+]")

            print(data)

            key = cv2.waitKey('q')
            if key == ord('q'):
                client_socket.close()
                break

            if count == frames_to_count:
                try:
                    fps = round(frames_to_count / (time.time() - start), 1)
                    st = time.time()
                    count = 0
                except:
                    pass
            count += 1
            time.sleep(0.001)

        client_socket.close()
        cv2.destroyAllWindows()
    except Exception as e:
        errname = type(err).name + str(e)
        print(f'[-] Error Receiving Message. {errname} \n{str(e)} \n{sys.last_traceback} || {traceback.print_exc} || {sys.exc.info()[2]}')
        raise Exception('recv_Stream')

def f(id):
    print('started thread')
    return int(id)+1



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.submit(start_listener)
        executor.submit(start_stream)
        executor.submit(send_vid)
        executor.submit(send_msg)
        executor.submit(rcv_msg)
        executor.submit(recv_vStream)

def multi_thread():
    t1 = threading.Thread(target=start_listener)
    t2 = threading.Thread(target=send_vid)
    t3 = threading.Thread(target=make_vid)
    t4 = threading.Thread(target=send_msg)
    t5 = threading.Thread(target=recv_msg)
    t6 = threading.Thread(target=recv_vStream)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()


if __name__ == '__main__':
    multi_thread()

''': SAMPLE THREADING SERVER 
Even though not quite understand your question, due to lack of background of your aws related problem. It's doable to use context to do this, just as you mentioned.

import threading
import time


class Sleeper(threading.Thread):
    def __init__(self, sleep=5.0):
        threading.Thread.__init__(self, name='Sleeper')
        self.stop_event = threading.Event()
        self.sleep = sleep

    def run(self):
        print('Thread {thread} started'.format(thread=threading.current_thread()))
        while self.sleep > 0 and not self.stop_event.is_set():
            time.sleep(1.0)
            self.sleep -= 1
        print('Thread {thread} ended'.format(thread=threading.current_thread()))

    def stop(self):
        self.stop_event.set()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop()
        print('Force set Thread Sleeper stop_event')


with Sleeper(sleep=2.0) as sleeper:
    time.sleep(5)

print('Main Thread ends')

'''

''' ASYNCIO SOCKET CODE 

import asyncore

class EchoHandler(asyncore.dispatcher_with_send):

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        
        
    
    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)


    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)
asyncore.loop()
'''
