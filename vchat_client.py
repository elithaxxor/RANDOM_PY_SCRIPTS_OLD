import socket, cv2, pickle, struct, time
# brew install imagesnap
# pip3 install sounddevice
# pip3 install cv2
# pip install vext



cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera in use')
    sys.exit(1)

'''Retrieve Frame Height.'''
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

'''Reset Frame Height'''
print('Setting Frame 720x1280'), time.sleep(1)
cap.set(3, 1280)
cap.set(4, 720)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print('[+] Enter The IP for connection: ')
IP = input('')
PORT = 9999
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))
data = b""
payload_size = struct.calcsize("Q") #Q = long long int (8byte)
while True:
    while len(data) < payload_size:
        packet = clientSocket.recv(4 * 1024) # 4k -- sets up the buffer
        if not packet:
            break
        data += packet
        packed_msg_size = data[:payload_size] #
        data = data[payload_size:] # contains video frame .. replace the size with the frame
        msg_size = struct.unpack('Q', packed_msg_size)[0]
        print(f'[+]  Msg Size:  [{msg_size}]')
        while len(data) < msg_size:
            data += clientSocket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data) ## display output
        cv2.namedWindow("[+] Video Chat")
        ret, frame = cap.imread(frame)
        if not ret:
            print('Unable to read frame')
        cv2.imshow('+] Video Chat', frame)

        key = cv2.waitKey(0) & 0xFF
        if cv2.waitKey(0) & 0xFF == ord('q'):
            client_socket.close()
            if client_socket.close():
                print('Socket Closed')
            cv2.destroyAllWindows()
            cap.release()
            if cap.release():
                print('Recourses relased')
            cv2.destroyAllWindows()
            break






