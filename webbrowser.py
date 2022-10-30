import socket
from html.parser import HTMLParser

## The Client
class WebBrowserC():
    def __init__(self):
        super(self.__class__, self).__init__()
        print(f'[+] Address" ')
        self.IP = input('')
        self.IPparts = self.IP.split('.')
        self.PORT = 80
        self.htmlPARSER = self.HTMLParser()

    @staticmethod
    def handle_starttag(tag, attrs):
        print("Encountered a start tag:", tag)
    @staticmethod
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    @staticmethod
    def handle_data(self, data):
        print("Encountered some data  :", data)

    def webbrowser(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((self.IP, self.PORT))
        cmd = "GET f'{IP}'\r\n\r\n".encode() ## change \r\n to headers later".encode()
        clientSocket.send(cmd) # might change to send all
        clientSocket.send(b'\r\n')
        clientSocket.send(b"------------")

        handle_starttag()

        while True:
            clientData = clientSocket.recv(512)
            parse = self.htmlPARSER

            if len(clientData) < 1:
                break
            print(clientData.decode(), end='')
        clientSocket.close()

    class HTMLParser(HTMLParser):
        pass


def run_browser():
    browser = WebBrowserC()
    browser.webbrowser()

    parser00 = browser.htmlPARSER
    parser00.feed('<html><head><title>Test</title></head>'
                '<body><h1>Parse me!</h1></body></html>')

    parser = HTMLParser()
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>Parse me!</h1></body></html>')



run_browser()


