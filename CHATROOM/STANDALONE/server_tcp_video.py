import socket, cv2, pickle, struct, time, traceback
from cv2 import VideoCapture
from cv2 import waitKey

port = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
host_name = socket.gethostbyaddr(host_ip)
full_host = f'{host_ip}:{port}'

print(f'[+] HOST: {host_ip}')
print(f'[+] HOST IP: {host}')
print(f'[+] port: {host_name}')
print(f'[+] HOST name: {host_name}')

server_socket.bind((host_ip, port))
server_socket.listen(5)
starttime = time.time()
cstart = time.ctime(starttime)
print(f'[+] Listening on [{full_host}]\n[{cstart}]')
print('X'*50,'\n')
try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f'[+] Received Connection from Sock [{client_socket}] Address:  [{addr}]\n[{cstart}]')
        if client_socket:
            vid = cv2.VideoCapture(0)
           # capture = cv2.VideoCapture(vid)
            tf = vid.isOpened()
            if tf == False:
                capture.open(vid)
            vid.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
            vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
            while(vid.isOpened()):
                img, frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack('Q', len(a))+a
                print(message)
                cv2.imshow('[+] Stream', vid)
                cv2.imshow('[+] Stream', message)

                key = cv2.waitKey(0) & 0xFF
                if cv2.waitKey(0) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    client_socket.close()

except struct.error as sterror:
    print('[-] Struct Error \n', sterror)
except Exception as E:
    err_name = type(err).__name__
    print(f'[-] Type Error: [{err_name}]\n[{E}]\n[{traceback.print_exc()}]')





    #
    # global capture
    # capture = cv2.VideoCapture(vid)
    # tf = capture.isOpened()
    # if tf == False: capture.open(vid)
    # while True:
    #     isTrue, frame = capture.read()
    #     print(f'[+] frame True? [{isTrue}] :: [{tf}]')
    #     cv2.imshow('video', frame)
    #     if cv2.waitKey(0) & 0xFF == ord('q'): return frame
    #     capture.release()
    #     cv2.destroyAllWindows()
    #     return frame, capture
