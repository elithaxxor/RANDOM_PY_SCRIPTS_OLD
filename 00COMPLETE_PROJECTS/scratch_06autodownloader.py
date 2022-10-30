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

### GET LIST FROM SHAWNA
#### FEEED PROGRAM LIST AFTER PARSING HTML TAGS
## SET LOOP, WITH OS TIMER SET TO 30 SEC to pick up all downloads
# URL = input("[SYS] Enter URL: ")
website_list = dl.website_list
index_end = len(website_list)
index_dict = {}
# print(type(index_end))
print()
print()
print()

print(os.get_terminal_size())  # returns the terminals size
width = os.get_terminal_size().columns  # set the width to center goods
print("[** WELCOME TO THE AUTOMATIC .TORRENT DOWNLOADER (ADD USAGE INST LATER) ]".center(width))


# print(dict)
## MAKE LIST INTO DICT, EASIER TO HANDLE.
# index = 0index = 0
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
##### THE DOWNLOADER AS FUNCTION ########


## to print LIST (not DICT), with prettyness
print(f'{display_list()}\n')
print('X' * 50)
print(display_dict())
print('X' * 50)

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


def reverse(s):
    rev = ''
    for i in range(len(text), 0, -1):
        rev += text[i-1]
    return rev



counter_00 = 0
for key in website_list:
    print('[SYSTEM]**2 Sleeping for 3 Seconds')
    time.sleep(3)
    print()
    if counter_00 == index_end:  ## break
        sys.exit(0)
    else:
        print(f"[SYSTEM] ++ Parsing ++ ".center(width))
        print(f"{'*' * 30}".center(width))
        print(f'[{counter_00}] : {key} ++')


        counter_00 += 1
        def run_downloader():  #
            try:  # parsing w/header
                print()
                print(f'[SYSTEM]** Connecting To Server. Sleeping for 5 seconds... ')
                time.sleep(5)
                URL = key
                print(type(URL))
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
                print(f'[SYSTEM]server response data saved to {saveFile} in program directory')

                return req
                # respData = resp.read(req)
                ## save file for further analasys --

            except OSError as error:
                return f"{'x' * 50} \n SAME FILE ERROR LINE 186 \n {str(error)}" and sys.exit(1)
        try:
            #for i in range(len(website_list)):
            cwd = os.getcwd()
            DOWNLOAD_NAME = website_list[counter_00]  # set iteration
            DOWNLOAD_NAME = reverse(DOWNLOAD_NAME)

            print(f'333333333333333333 :: {DOWNLOAD_NAME}')
            #DOWNLOAD_NAME = DOWNLOAD_NAME[10:-1]
            DOWNLOAD_NAME = DOWNLOAD_NAME.replace("/", "")
            DOWNLOAD_NAME = DOWNLOAD_NAME.replace("-", "")
            DOWNLOAD_LOC = str(cwd) + f'/{DOWNLOAD_NAME}'
            path = DOWNLOAD_LOC + DOWNLOAD_NAME
            print(f'[SYSTEM] File will be saved to: {path}')
            # os.makedirs(path, 777)
            print('[SYSTEM]**3 sleeping for 3 seconds: ')
            time.sleep(3)
            print()
            print("[SYSTEM] ++ RUNNING DOWNLOAD REQUEST++".center(width))

            # print(f"{string_01 :^70}")

            if path:
                to_connect = run_downloader()
                print(to_connect)
                print(
                    f'[SYSTEM]** {key}  DEBUG--- LINE 109 --- URL HAS PASSED SERVER-CHECK \n saving to {DOWNLOAD_LOC}\n ** AS PATH {path}'.center(
                        width))
                print()
                download = tf.keras.utils.get_file(f"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME}", to_connect)
                SUCCESS = f"[SYS] - [SUCCESS] - Parsed {key} Successfully \n File Saved: ***** {download} ***** \n /Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME} [SUCCESS] "
                print(f"{SUCCESS}".center(width))
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
