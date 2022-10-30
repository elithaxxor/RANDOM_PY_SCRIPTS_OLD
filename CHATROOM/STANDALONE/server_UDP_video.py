import socket, cv2, pickle, struct, time, imutils, base64, traceback
import numpy as np


# brew install imagesnap

port = 4444
BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # establish
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE) #look into the socet for buffer
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
host_name = socket.gethostbyaddr(host_ip)
full_host = f'{host_ip}:{port}'

server_socket.bind((host_ip, port))
starttime = time.time()
cstart = time.ctime(starttime)
vid = cv2.VideoCapture('random.mp4') # add path to video
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
            msg, client_addr = server_socket.recvfrom(BUFF_SIZE)
            _, frame = vid.read()
            frame = imutils.resize(frame, width=WIDTH)
            encode, buffer = cv2.imencode('jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80]) ## imcode to write binary, imwrite to specify jpg quality
            frame = cv2.putText(frame, 'FPS :' + str(fps), (10, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255),2)
            cv2.imshow('[+] [Starting Video Stream] [+] ', frame)
            key = cv2.waitKey(10) & 0xFF
            if key == ord('q'):
                server_socket.close()
                break
            if count == frames_to_count:
                try:
                    fps = round(frames_to_count/(time.time()-start))
                    start = time.time()
                    count = 0
                    print(fps)
                except Exception as e:
                    print(f'[+] Error in Handling FPS count \n [{e}]')
                    pass
            count += 1

    except socket.error as sockerr:
        traceback.print_exc()
        print('[+] Raised Socket Error')
    except Exception as e:
        traceback.print_exc()
        print(f'[+] Raised Other Error \n[{str(e)}]')





