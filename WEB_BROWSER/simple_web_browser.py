from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import Arcus #@UnusedImport
import Savitar #@UnusedImport
from cura.CuraApplication import CuraApplication


class MyWebBrowser(QMainWindow):
    '''
        * the module used in this program was depricated after pyqt5.
        * pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyqt5==5.10.1
        ## if the above does not work, use the two below.
        * MACOS brew install pyqt
        * pip install --upgrade --user pyqt5==5.12
        * pip install --upgrade --user pyqtwebengine==5.12
    '''

    def __init__(self):
        #super(MyWebBrowser, *args, *kwargs)
        self.window = QWidget()
        self.window.setWindowTitle('Simple Webbrowser')

        # h/w layout
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        ## url bar
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        #search button
        self.go_btn = QPushButton("Go")
        self.go_btn = setMinimumHeight(30)
        ## back button
        self.back_btn = QPushButton("<")
        self.back_btn = setMinimumHeight(30)
        # forward button
        self.forward_btn = QPushButton(">")
        self.forward_btn = setMinimumHeight(30)

        # add widgets to horizontal layout
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        # create browser
        self.browser = QWebEngineView()

        ## widget functionality
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.go_forward_btn.clicked.connect(self.browser.forward)
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl('http://gooogle.com'))

        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self, url):
        # set the url bar text
        if not url.startswith("http"):
            url = "http:// " + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


        ## bounding browser to events

app = QApplication([])
window = MyWebBrowser()
app.exec_()

# app = CuraApplication()
# app.run()







