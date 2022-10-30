import socket, cv2, pickle, struct, time, imutils, base64, traceback
import numpy as np


# brew install imagesnap
import socket, struct, ipaddress


def str2ip(ip):
    return ipaddress.ip_address(ip)

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    print(packedIP)
    #print(struct.unpack('',packedIP)[0])
    return struct.unpack("!L", packedIP)[0]

def ip2int(ip):
    '''converts IP to interger'''
    return int(socket.inet_aton(ip).encode('hex'),16)

port = 4444
BUFF_SIZE = 9216
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # establish
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE) #look into the socet for buffer
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
host_name = socket.gethostbyaddr(host_ip)
full_host = f'{host_ip}:{port}'

server_socket.bind((host_ip, port))
starttime = time.time()
cstart = time.ctime(starttime)
vid = cv2.VideoCapture(0) # add path to video
fps, start, frames_to_count, count = (0,0,20,0)

print(f'[+] HOST: [{host_ip}]')
print(f'[+] HOST IP: [{host}]')
print(f'[+] port: [{port}]')
print(f'[+] HOST name: [{host_name}]')

print(f'[+] FPS: [{fps}]')
print(f'[+] st: [{start}]')
print(f'[+] frames_to_count: [{frames_to_count}]')
print(f'[+] cnt: [{count}]')
print('\n', 'X'*50)
print(f'[+] Listening on [{full_host}]\n[{cstart}]')
print('X'*50,'\n')

while True:
    try:
        msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
        print('\n', 'X' * 50)
        print(f'[+] Received Connection  from [{client_addr}]\n[{cstart}]')
        print(f'[+] MSG: [{msg}]\n[{client_addr}] @ [{time.ctime()}]')
        print('X' * 50, '\n')
        WIDTH=400
        while(vid.isOpened()):
            print(f'[+] Video Buffer Recvd from [{client_addr}] @ [{time.ctime()}]')
            #msg, client_addr = server_socket.recvfrom(BUFF_SIZE) ## may be redundant

            _, frame = vid.read()
            frame = imutils.resize(frame, width=WIDTH)
            cv2.imshow('frame',frame)
            encode, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80]) ## imcode to write binary, 80% jpeg quality
            message = base64.b64encode(buffer)
            print(client_addr)
            print(type(client_addr))
            client_ip=client_addr[0]
            print(client_ip)
            print(type(client_ip))

            client_ip=int(ipaddress.IPv4Address(client_ip))
            print(client_ip)
            print(type(client_ip))

            # client_ip=str(ipaddress.IPv4Address(3232235521))


            cv2.imshow('[Transmitting Video]', frame)  # show frame serverside

            data=b''
            payload_size=struct.calcsize('Q')

            message = struct.pack('>I', len(message)) + message


            server_socket.sendto(message, client_addr)
            if key == ord('q'):
                server_socket.close()
                break

            # if server_socket.sendto:
            #     print('[+] Buffer packets sent.. ')
            # frame = cv2.putText(frame, 'FPS :' + str(fps), (10, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255),2)
            # cv2.imshow('[+] [Starting Video Stream] [+] ', frame)
            # key = cv2.waitKey(1) & 0xFF



            # if count == frames_to_count:
            #     try:
            #         fps = round(frames_to_count/(time.time()-start))
            #         start = time.time()
            #         count = 0
            #         print(fps)
            #     except Exception as e:
            #         print(f'[+] Error in Handling FPS count \n [{e}]')
            #         pass
            # count += 1

    except socket.error as sockerr:
        traceback.print_exc()
        print('[+] Raised Socket Error')
    except Exception as e:
        traceback.print_exc()
        print(f'[+] Raised Other Error \n[{str(e)}]')





