import wget
import os
import urllib
from urllib.request import Request, urlopen
import tensorflow as tf
import bs4
from bs4 import BeautifulSoup
import os
import datetime
import urllib.request
import urllib.parse
import requests
import getpass as gp
import numpy as np
import pandas as pd

# import __ __downloadlist as dl
# from __downloadlist import *

#

URL = input("[SYS] Enter URL: ")
req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})  # for downloads
request = requests.get(URL).text  # for beatifulsoup
print(req)
print(requests)
# webpage = urlopen(req) #.read().decode('utf-
# print(webpage)

### GET LIST FROM SHAWNA
#### FEEED PROGRAM LIST AFTER PARSING HTML TAGS
## SET LOOP, WITH OS TIMER SET TO 30 SEC to pick up all downloads


try:  # parsing w/header
    # URL = input('Enter URL: ')
    HEADERS = {}
    HEADERS["User-Agent"] = [
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    ]
    req = urllib.request.Request(URL, headers=HEADERS)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open("withHeaders.txt", "w")
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    x = "*"
    print(f"{x * 50} \n [SYS] Error Carry on.. \n {str(e)}")


try:  # downloader
    DOWNLOAD_LOC = "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS"
    DOWNLOAD_NAME = input(str("[SYS] Please Enter Download Name:"))
    DOWNLOAD_LOC += DOWNLOAD_NAME
    print(DOWNLOAD_LOC)
    webpage_2 = tf.keras.utils.get_file(
        "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST.torrent", req
    )
    print(f"[SYS File Saved: {webpage_2}")
except Exception as e:
    print(str(e))


############### BEATIFUL-SOUP ########################
try:
    soup = BeautifulSoup(URL, "html.parser")
    print(f"soup.prettify, \n")
    HTML_PARSED = soup.prettify()
    print()
    print("*" * 50)
    print(HTML_PARSED)
    PRETTIFY_FILE = input("[SYS] Enter file name to save soup (.html)")
    with open(PRETTIFY_FILE, "a") as f:
        f.write(HTML_PARSED)
        print(f"[SYS] HTML_PARSE created at {os.getcwd()}")
except Exception as e:
    print(str(e))


# ## SEARCH BAR QUERY (URL ENCODING)
# url = "http://pythonprogramming.net"
# values = {"s": "basic", "submit": "search"}
# data = urllib.parse.urlencode(values).encode("utf-8")
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# print(respData)  # get
#

#
