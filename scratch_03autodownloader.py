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
#try:
    DOWNLOAD_LOC = "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/"
    # DOWNLOAD_NAME = input(str("[SYS] Please Enter Download Name:"))
    DOWNLOAD_NAME = website_list[0]
    #DOWNLOAD_LOC += DOWNLOAD_NAME
    PATH = os.path.join(DOWNLOAD_LOC, DOWNLOAD_NAME)
    os.mkdir(PATH)
#except OSError as error:
#        x = '*'
#        print(f"{x * 50} \n ******** \n {str(error)}")







#
#
# ### ^^ make os line 86
# print()
# print(prettify())
#
# for test in index_dict:
#     print(f'[SYSTEM]********* {test}')
#
# print('7' * 50)
# # print(website_list)
#
# def website_iter(url):
#     pass
#
# try:  # parsing w/header
#    # URL = list(index_dict.items())[0][0]
#     #print(URL)
#     #print(f'{type(URL)} ')
#     # URL = str(first_value) #[0:]
#     iter = 0
#     while iter < len(website_list): #index_end = len(website_list)
#         #for site in len(website_list):
#         # print(website_list[iter])
#         URL = website_list[iter]
#         iter += 1
#
#         if URL:
#             print(type(URL))
#             print(URL)
#             HEADERS = {}
#             HEADERS[
#                 "User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
#
#             req = urllib.request.Request(URL, headers=HEADERS)
#             resp = urllib.request.urlopen(req)
#             respData = resp.read()
#
#             #     ### CHANGE CODE LATER ###
#             # saveFile = open("withHeaders.txt", "w")
#             # saveFile.write(str(respData))
#             # saveFile.close()
#
#             if resp:
#                 try:  # downloader
#                     DOWNLOAD_LOC = "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/"
#                     # DOWNLOAD_NAME = input(str("[SYS] Please Enter Download Name:"))
#                     DOWNLOAD_NAME = website_list[iter]
#                     DOWNLOAD_LOC += DOWNLOAD_NAME
#                     # print(DOWNLOAD_LOC)
#                 except Exception as e:
#                     x = "*"
#                     print(f"{x * 50} \n [SYS] Error [BREAK].. \n {str(e)}")
#
#                 #
#                 #     ### GET OS TO MKDIR of DOWNLOAD_NAME file
#                 #     webpage_2 = tf.keras.utils.get_file(
#                 #         f"{DOWNLOAD_LOC}", req
#                 #     )
#                 #     print(f"[SYS File Saved: {webpage_2}")
#                 # except Exception as e:
#                 #     print(f'[SYS] SYS ERROR- {str(e)} \n [SYS] {str(e)}  .')
#
# except Exception as e:
#     x = "*"
#     print(f"{x * 50} \n [SYS] Error [BREAK].. \n {str(e)}")
#     sys.exit()
# #
#
#
#
# # try:  # downloader
# #     DOWNLOAD_LOC = "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/"
# #     #DOWNLOAD_NAME = input(str("[SYS] Please Enter Download Name:"))
# #     DOWNLOAD_NAME =
# #     DOWNLOAD_LOC += DOWNLOAD_NAME
# #     print(DOWNLOAD_LOC)
# #
# #     webpage_2 = tf.keras.utils.get_file(
# #         "/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/TEST.zip", req
# #     )
# #     print(f"[SYS File Saved: {webpage_2}")
# # except Exception as e:
# #     print(f'[SYS] SYS ERROR- {str(e)} \n [SYS] Moving on to webscraper.')
#
#
# #
# # ########  ADD BUFFER #####
# #
# #
# #     file_size = os.path.getsize(TEST.torrent)
# #     buffer = file_size
# #     print(prettify())
# #     print(f'[SYS] FILE SIZE IS {file_size} ')
# #     ## open and read as binary for parsing
# #     with open(webpage_2, "rb", buffering=300000) as file:
# #         send_count = 0
# #         send_start = time.time()
# #         # start loop
# #         while send_count != file_size:  # start loop
#             data = file.read(8192)
#             if not (data):
#                 break  # <- end of F/T
#             client.sendall(data)
#             send_count += len(data)
#
#         send_end = time.time()
#
#     total_time = send_end - send_start
#     print(f"[SYSTEM] {webpage_2} Transfer Complete in: {total_time}")
#     socket.close()  # stop
#     #print(f"[SYS File Saved: {webpage_2}")
# except Exception as e:
#     print(f'[SYS] SYS ERROR- {str(e)} \n [SYS] Moving on to webscraper.')
#
#
#
# buffer = file_size
# ## open and read as binary for parsing
# with open(file_name, "rb", buffering=300000) as file:
#     send_count = 0
#     send_start = time.time()
#
#     # start loop
#     while send_count != file_size:  # start loop
#         data = file.read(8192)
#         if not (data):
#             break  # <- end of F/T
#         client.sendall(data)
#         send_count += len(data)
#
#     send_end = time.time()
#
# total_time = send_end - send_start
# print(f"[SYSTEM] {file_name} Transfer Complete in: {total_time}")
# socket.close()  # stop
#



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