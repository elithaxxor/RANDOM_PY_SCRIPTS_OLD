	import wget, os, urllib, time, datetime, requests, sys
from urllib.request import Request, urlopen
import tensorflow as tf
import bs4
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import getpass as gp
import numpy as np
import pandas as pd
import __downloadlist as dl
from __downloadlist import *
import sys


import re
import linkGrabber





print(os.get_terminal_size())  # returns the terminals size
website_list = dl.website_list
index_end = len(website_list)
index_dict = {}
# print(type(index_end))
width = os.get_terminal_size().columns  # set the width to center goods
width_len = width

# print(width)
# print(type(width))

print(), print(), print()
print("[** -[AUTOMATIC DOWNLOADER]- **]".center(width))
print(f"{'*' * 25}".center(width))

#print(type(width_len))
#print(width_len)

# print(dict)
## MAKE LIST INTO DICT, EASIER TO HANDLE.
def debugger():
    star = 4
    start = 0
    while True:
        print(f"{'*' * 50 : ^70}")
        start += 1
        if start == star:
            break


def display_header(list_or_dict):
    # print('*' * 75)
    x = 'x'
    print(f"{'*' * 75:^70}")
    print(f"{'*' * 75:^70}")
    pretty = f'xxx DOWNLOAD {list_or_dict} xxx'
    print(f'{pretty : ^70}')
    print(f"{x * 20: ^70}")
    zero = (f'[USAGE] - [0] {dl.href_str}')
    one = (f'[USAGE] - [1] This is a python program that takes a list of download links, and saves each file to the programs download directory.')
    two = (f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
    three = (f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
    four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
    five = (f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    print(f"{zero:^70}")
    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")


index_dict = {}


def display_dict():
    d = 'DICTIONARY'
    print(display_header(d))
    index_01 = 0
    print(f'[SYSTEM] {type(website_list)}**--> List Of All Downloads')
    print(f"[SYSTEM]** You have entered {index_end} downloads.")

    for website, index in enumerate(website_list):
        if index_01 == index_end:
            break
        index_dict[index] = website
        index_01 += 1
    for test in index_dict:
        print(f'[SYSTEM]*[Dict] {test}')


def display_list():
    # print()
    # pretty = 'xxx DOWNLOAD LIST'
    # print(f'{pretty : ^70}')
    # print(f"{'x' * 20: ^70}")
    l = 'LIST'
    print(display_header(l))
    print(f'[SYSTEM] {type(website_list)}**--> List Of All Downloads')
    print(f"[SYSTEM]** You have entered {index_end} downloads.")
    index_02 = 0
    for key in website_list:
        print("*" * 20)
        print(f'[{index_02}] : {key} ++')
        index_02 += 1


##########################################################
#################### DOWNLOADER ##########################


print(),print()
## to print LIST (not DICT), with prettyness
print(f'{display_list()}\n')
print('*' * (width_len * 2))
#print(display_dict())
#print('X' * width_len)

# index_02 = 0
# while index_02 != index_end:
#     print()
#     print("[SYSTEM]**1 sleeping for 5 seconds")
#     time.sleep(5)
#     if index_02 == index_end:
#         print(f'[SYSTEM]********** [END] ***********)')
#         break


def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]




counter_00 = 0
for key in website_list:
    print('[SYSTEM]**2 Sleeping for 3 Seconds')
    time.sleep(3)
    print()
    if counter_00 == index_end:  ## break
        sys.exit(0)
    else:
        print(f"[SYSTEM] ++ Parsing ++ ".center(width))
        print(f"{'x'*30}".center(width))
        print()
        print(f"{'*' * 30}".center(width))
        print(f'[{counter_00}] : {key} ++')









        def reverse(s):
            rev = ''
            for i in range(len(DOWNLOAD_NAME), 0, -1):
                rev += DOWNLOAD_NAME[i-1]
            return rev


        counter_00 += 1
        def run_downloader():  #
            try:  # parsing w/header
                
                start_time = time.time()
                print()

                print(f'[SYSTEM]** Connecting To Server. Sleeping for 5 seconds...\n ')
                time.sleep(3)
                URL = key
                #print(type(URL))
                print(URL)
                HEADERS = {}
                HEADERS[
                    "User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

                req = urllib.request.Request(URL, headers=HEADERS)
                resp = urllib.request.urlopen(req)
                respData = resp.read()

                saveFile = open("resp_data.txt", "w")
                saveFile.write(str(respData))
                saveFile.close()
                end_time = time.time()
                time_to_complete = end_time - start_time

                print(f'[SYSTEM] Server response in: [{time_to_complete}]')
                print(f'\n[SYSTEM]server response data saved to {saveFile} in program directory')

              
                return req
                # respData = resp.read(req)
                ## save file for further analasys --



            except OSError as error:
                return f"{'x' * 50} \n SAME FILE ERROR LINE 186 \n {str(error)}" and sys.exit(1)



        def torrent_grabber(url):
            try: 
                soup = BeautifulSoup(r.text, "html.parser")
                html_parsed = soup.prettify()
                print(soup.prettify)
                #html_data = input("[SYS] Enter file name to save soup (.html)")
                with open('html_data.html', "a") as f:
                    f.write(html_parsed)
                print(f"[SYS] HTML_PARSE created at {os.getcwd()}")

                body_text = soup.find(class_='BodyText')
                tbody = soup.find(class_='navia dirlisting')

                print(f"{body_text} + \n\n\n\n\n {tbody}")


            except Exception as e:
                print(str(e))
                y = "[SYSTEM] Error When Parsing html data [SYSTEM]"
                print(f"{y}")



        ##################################################################################
        ##########################  START SEQUENCE TO RUN ###############################
        ##################################################################################
        try:
            #for i in range(len(website_list)):
            cwd = os.getcwd()
            DOWNLOAD_NAME = website_list[counter_00]  # set iteration
            torrent = 'torrent'
            website = 'https://1337x.to'
            #if (key.find(torrent)!=-1 or 
            if key.find(website)!=-1:
                print(f'[SYS] No Torrents Found, Continuing To Parse Request. ')
            else:            #  if (torrent in DOWNLOAD_NAME or website in DOWNLOAD_NAME): ## may need to set to website_list counter 
                print(f'[SYS] Torrent Site Found, running HTML Parser'.center(width))
                soup_connect = run_downloader()
                soup = torrent_grabber(soup_connect)






                      ##################################################################################
        ##########################  PASSS / FAIL FOR TORRENT ###############################
        ##################################################################################
                    

            #DOWNLOAD_NAME = reverse(DOWNLOAD_NAME)
            NAME_LEN = len(DOWNLOAD_NAME)
            DOWNLOAD_NAME = DOWNLOAD_NAME[NAME_LEN - 25 :]


            print(f'[SYSTEM] File_Name :: {DOWNLOAD_NAME}')
            DOWNLOAD_NAME = DOWNLOAD_NAME.replace("/", "")
            DOWNLOAD_NAME = DOWNLOAD_NAME.replace("-", "")
            DOWNLOAD_LOC = str(cwd) + f'/{DOWNLOAD_NAME}'
            path = DOWNLOAD_LOC + DOWNLOAD_NAME
            print(f'[SYSTEM] File will be saved to: {path}')
            # os.makedirs(path, 777)
            print('[SYSTEM]**3 sleeping for 3 seconds: ')
            time.sleep(1)
            print()
            print("[SYSTEM] ++ RUNNING DOWNLOAD REQUEST++".center(width))
            print(f"{'x'*30}".center(width))
            print()

            # print(f"{string_01 :^70}")

            if path:
                start_time = time.time()

                to_connect = run_downloader()
                print(to_connect)
                print(
                    f'\n[SYSTEM]** {key}  DEBUG--- LINE 109 --- URL HAS PASSED SERVER-CHECK \n saving to {DOWNLOAD_LOC}\n ** AS PATH {path}'.center(
                        width))
                print()
                download = tf.keras.utils.get_file(f"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME}", to_connect)
                SUCCESS = f"\n[SYS] - [SUCCESS] - Parsed {key} Successfully \n File Saved: ***** {download} ***** \n /Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME} [SUCCESS] "
                print(f"{SUCCESS}".center(width))
                print(f"{'x'*30}".center(width))
                print()
                end_time = time.time()
                time_to_complete = end_time - start_time
                print(f'[SYSTEM] Download complete in: [{time_to_complete}]')

                #counter_00 += 1
                continue

        except Exception as e:
            print(f"[SYS] - [ERROR] - DOWNLOAD ERROR - [ERROR] \n {str(e)}")
            sys.exit(1)
        except Exception as a:
            print(f"[SYS] Error [BREAK] LINE 130\n {str(a)}")
            
    counter_00 += 1
    print(f'--LINE COUNTER--'.center(width))
    print(f'[SYSTEM]-- COUNTER DEBUG **[{counter_00}]**'.center(width))











# links = linkGrabber.Links("http://www.google.com")
# links.find()
# # limit the number of "a" tags to 5
# links.find(limit=5)
# # filter the "a" tag href attribute
# links.find(href=re.compile("plus.google.com"))





# index_02 += 1

#
#
#
# i += 1
#     if run_downloader(key, path):
#         print(f'[sys] {DOWNLOAD_NAME} Successfully created in {DOWNLOAD_LOC}')
#         pass
#         # run_downloader(key)
#     else:
#         print('[SYSTEM] Error- line 169.. ')
#         pass
