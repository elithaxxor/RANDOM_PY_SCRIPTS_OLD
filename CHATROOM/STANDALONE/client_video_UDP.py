import socket, cv2, pickle, struct, time, imutils, base64, sys
import traceback

import numpy as np

try:
    while True:
        port = 4444
        BUFF_SIZE = 65536
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # establish
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE) #look into the socet for buffer
        client = socket.gethostname()
        client_ip = socket.gethostbyname(client)
        client_name = socket.gethostbyaddr(client_ip)
        full_client = f'{client_ip}:{port}'
        print(f'[+] HOST: [{client_ip}]')
        print(f'[+] HOST IP: [{client}]')
        print(f'[+] port: [{port}]')
        print(f'[+] HOST name: [{client_name}]')
        print(f'[+] Enter the IP for connection: [{client_ip}]')
        server = input('')
        print(f'[+] Connecting [{client_ip}]" [{port}]')
        print(f'[+] Attempting to Send Message to Server')
        message = b'[hello world]'
        client_socket.sendto(message, (server, port))
        if client_socket.sendto:
            print(f'[+] Connection to [{server}] Succesful.')
            break
        else:
            print(f'[+] Connection to [{server}] Not-Successfull\n SYS.EXIT')
            sys.exit(1)

    try:
        ## to receive datagramer
        fps, start, frames_to_count, count = (0, 0, 20, 0)
        while True:
            print('\n', 'X' * 50)
            print(f'[+] --Moving On To Stream Sequence-- [+]')
            packet, _ = client_socket.recvfrom(BUFF_SIZE)
            data = base64.b64decode(packet, " /")  # decode whats received
            data = str(data)
            npdata = np.fromstring(data, dtype=np.uint8)  # recover data || np.unt8 8bit unsigned  image array
            frame = cv2.imdecode(npdata, 1)
            frame = cv2.putText(frame, 'FPS :' + str(fps), (10, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7,
                                (0, 0, 255), 2)  ## add to frame
            cv2.imshow('[+] Receving Buffer', frame)
            key = cv2.waitKey(0) & 0xFF  # 1 ms delay
            if key == ord('q'):
                client_socket.close()
                break
    except socket.error as sockerr:
        traceback.print_exc()
        print('[+] Raised Socket Error')
        sys.exit(1)
    except Exception as e:
        traceback.print_exc()
        print(f'[+] Raised Other Error \n[{str(e)}]')
        pass

except socket.error as sockerr:
    traceback.print_exc()
    print('[+] Raised Socket Error')
    sys.exit(1)

except Exception as e:
    traceback.print_exc()
    print(f'[+] Raised Other Error \n[{str(e)}]')
    pass



