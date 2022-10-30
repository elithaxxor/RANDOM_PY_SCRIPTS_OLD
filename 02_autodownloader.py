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
import __downloadlist as dl
from __downloadlist import *
import sys

def prettify():
    star = 4
    start = 0
    while True:
        print(f"{'*' * 50 : ^70}")
        start += 1
        if start is star:
            break

    print()


### GET LIST FROM SHAWNA
#### FEEED PROGRAM LIST AFTER PARSING HTML TAGS
## SET LOOP, WITH OS TIMER SET TO 30 SEC to pick up all downloads
# URL = input("[SYS] Enter URL: ")
website_list = dl.website_list
index_end = len(website_list)
index_dict = {}
# print(type(index_end))
print()
print(f"[SYSTEM]** You have entered {index_end} downloads.")
print()
print()

# print(dict)
## MAKE LIST INTO DICT, EASIER TO HANDLE.
# index = 0index = 0

index_01 = 0
for website, index in enumerate(website_list):
    if index_01 is index_end:
        print('7' * 50)
        break
    index_dict[index] = website
    #    print("*" * 50)
    index_01 += 1

print(type(index_dict))
print(index_dict)
#
# ## BLOCK TO MAKE CODE PRETTY ##
# star = 4
# start = 0
# while True:
#     print(f"{'*' * 50 : ^70}")
#     start += 1
#     if start is star:
#         break
#
#
#
print()
pretty = 'xxx DOWNLOAD LIST'
print(f'{pretty : ^70}')
print(f"{'x' * 20: ^70}")
print(f'[SYSTEM] {type(website_list)}**--> saved to dict for further processing')

## to print LIST (not DICT), with prettyness
index_02 = 0
for key in website_list:
    print("*" * 20)
    print(f'[{index_02}] : {key} ++')
    index_02 += 1

print()
print(prettify())

for test in index_dict:
    print(f'[SYSTEM]********* {test}')

print('7' * 50)

try:  # parsing w/heade
    URL = website_list[0]
    print(type(URL))
    print(URL)
    HEADERS = {}
    HEADERS["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    req = urllib.request.Request(URL, headers=HEADERS)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open("withHeaders.txt", "w")
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    x = "*"
    print(f"{x * 50} \n [SYS] Error [BREAK].. \n {str(e)}")
    sys.exit()

try:  # downloader
    DOWNLOAD_LOC = "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/"
    DOWNLOAD_NAME = input(str("[SYS] Please Enter Download Name:"))
    DOWNLOAD_LOC += DOWNLOAD_NAME
    print(DOWNLOAD_LOC)

    webpage_2 = tf.keras.utils.get_file(
        "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/TEST.zip", req
    )
    print(f"[SYS File Saved: {webpage_2}")
except Exception as e:
    print(f'[SYS] SYS ERROR- {str(e)} \n [SYS] Moving on to webscraper.')






############### BEATIFUL-SOUP ########################
#
# req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})  # for downloads
# request = requests.get(URL).text  # for beatifulsoup
# print(req)
# print(requests)
# # webpage = urlopen(req) #.read().decode('utf-8)
# # print(webpage)
#
#
# try:
#     soup = BeautifulSoup(URL, "html.parser")
#     print(f"soup.prettify, \n")
#     HTML_PARSED = soup.prettify()
#     print()
#     print("*" * 50)
#     print(HTML_PARSED)
#     PRETTIFY_FILE = input("[SYS] Enter file name to save soup (.html)")
#     with open(PRETTIFY_FILE, "a") as f:
#         f.write(HTML_PARSED)
#         print(f"[SYS] HTML_PARSE created at {os.getcwd()}")
# except Exception as e:
#     print(str(e))
#


# print(f"{index} : {website}  \n")
# dict = dict(zip(website_list, range(len(website_list))))
# print(type(website_list))
# print(website_list)
# index_dict = index_dict['Value'].append(website)
# index_dict['Value'] = website
# index_dict = index_dict['Website'].append(website)
# index += 1


################## LIST TO STRING  ##############
# URL = list(index_dict.items())[0][0]
# print(type(first_value))
# print('First Value: ', first_value)
#
# print('8' * 50)
#
# def listToString(list_conversion_pass):
#     # initialize an empty string
#     str1 = ""
#     # return string
#     return(str1.join(list_conversion_pass))
#
# URL = listToString(first_value)
# print(URL)
# #listToString(first_value)
# #print(URL)
#
