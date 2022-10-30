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
import getpass as gp
import numpy as np
import pandas as pd


#url = 'http://itorrents.org/torrent/BDB7B86A1099FE63B2575DAB4DAF6E7F5B4BA1FB.torrent'
#torrent = wget.download(url)

#torrent_01 = tf.keras.utils.get_file('the_mummy.csv', 'http://itorrents.org/torrent/BDB7B86A1099FE63B2575DAB4DAF6E7F5B4BA1FB.torrent')
#################### urllib ################

URL = input('[SYS] Enter URL: ')

x = 1
try:
    HEADERS = {}
    HEADERS["User-Agent"] = [
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    ]
    req = urllib.request.Request(URL, headers=HEADERS)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respdATA))
    saveFile.close()
except Exception as e:
    x = "*"
    print(f"{x * 50} \n [SYS] Error Carry on.. \n {str(e)}")
    print("[SYS] Break ")
# #
# print(HTML)
# print(HTML.read())
# print(f'[SYS]')
# # ######### BEATIFUL SOUP #######
# # # to make source code prettier:
# soup = BeautifulSoup(HTML,'html.parser')
#
# print(f'soup.prettify, \n')
#
# HTML_PARSE = soup.prettify()
#
# # write out to file
# with open('HTML_PARSE.html', 'a') as f:
#     f.write(HTML_PARSE)
# print(f'[SYS] HTML_PARSE created at {os.getcwd()}')
#
# #
#################### TENSORFLOW ##################

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
print(req)
webpage = urlopen(req) #.read().decode('utf-
print(webpage)
webpage_2 = tf.keras.utils.get_file('/Users/macbook/Documents/CS/PROJECT/AutoDownloader/torry_01.torrent', req)
print(webpage_2)


#print(webpage)
