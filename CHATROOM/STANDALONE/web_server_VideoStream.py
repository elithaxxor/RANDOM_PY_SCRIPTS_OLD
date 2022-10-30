import socket, cv2, pickle, struct, time, traceback, sys
import pyshine as ps  # pip3 install pyshine==0.0.9
from socket import *
from cv2 import VideoCapture, waitKey



HTML = """
<html>
<head>
<title>PyShine Live Streaming</title>
</head>

<body>
<center><h1> PyShine Live Streaming using OpenCV </h1></center>
<center><img src="stream.mjpg" width='640' height='480' autoplay playsinline></center>
</body>
</html>
"""

def webServer():
    def main_streamer():
        StreamProps = ps.StreamProps
        StreamProps.set_Page(StreamProps, HTML)
        address = ('192.168.50.186', 9999)  # Enter your IP address
        try:
            StreamProps.set_Mode(StreamProps, 'cv2')
            capture = cv2.VideoCapture(0)
            capture.set(cv2.CAP_PROP_BUFFERSIZE, 4)
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
            capture.set(cv2.CAP_PROP_FPS, 30)
            StreamProps.set_Capture(StreamProps, capture)
            StreamProps.set_Quality(StreamProps, 90)
            server = ps.Streamer(address, StreamProps)
            print('Server started at', 'http://' + address[0] + ':' + str(address[1]))
            server.serve_forever()
        except KeyboardInterrupt:
            capture.release()
            serverSocket.close()
            return False
        except Exception as e:
            print(f'Error in main_streamer {traceback.print_exc} \n \n {sys.exc_info()[2]} {e}')


    '''create socket obj /// create bind/ // start listen //Accept connection// then recv connection // 
    conditions-return // setuup header (data) // call main_stream  '''

    # data = "1.1200 OK\r\n"
    # data += "Content-Type: text/html; charset=utf-8
    # data += '\r\n'
    global serverSocket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        PORT = 9000
        serverSocket.bind(('localhost', PORT))
        serverSocket.listen(5)
        while(1):
                (client_socket, address) = serverSocket.accept()
                client_sent = client_socket.recv(5000).decode()
                pieces = client_sent.split('\n')

                if len(client_sent) > 0:
                    print(f'[+] Request from client :: \n {client_sent}')
                else:print(f'[+] Request blank request client :: \n {client_sent}')
                if (len(pieces) > 0):
                    print(pieces)
                else:print(f'[+] Request blank request client :: \n {client_sent}')

                data = f"1.1200 OK\r\n" + f"Content-Type: text/html; charset=utf-8\r\n" + f'\r\n'
                client_socket.sendall(data.encode())
                client_socket.send(b"\r\n")  # binary for line down
                client_socket.send(b"-------- TEST SERVER ---------")  # binary for line down
                client_socket.send(b"\r\n")  # binary for line down
                flag = main_streamer()

                if flag is False:
                    client_socket.shutdown(SHUT_WR)
                    serverSocket.close()


    except KeyboardInterrupt as e:
        print('[+] End-User initiated shutdown.')
    except Exception as e:
        print(str(e))

        # Part 01 using opencv access webcam and transmit the video in HTML

def runServer():
    webServer()
