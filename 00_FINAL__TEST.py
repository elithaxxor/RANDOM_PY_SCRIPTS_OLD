import wget
import time
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
import requests as req
import getpass as gp
import numpy as np
import pandas as pd
import sys
import csv 
import matplotlib.pyplot as plt
import pandas as pd
import __downloadlist as dl
from __downloadlist import *
import sys
import re
import linkGrabber
from linkGrabber import Links
import platform
import subprocess
import IPCHECKER as IPx
from IPCHECKER import *
from subprocess import call
import traceback




class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"

    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"

    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"

    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"


class Spinner:
    busy = False
    delay = 0.1
    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False

def clear():
    # check and make call for specific operating system
    os_name = platform.system()
    _ = call('clear' if os_name == 'Linux' or 'Windows' or 'Darwin' else 'cls')

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
    subprocess.check_call([sys.executable, "-m", "pip", "install", tqdm])
    subprocess.check_call([sys.executable, "-m", "pip", "install", datetime])








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

color = Colors()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset

print(IPx.IP)
# print(f'\033[0;35;47m \t\t[{IPx.get_ip()}]  ...? \033[0m 0;35;47m')
width = os.get_terminal_size().columns  # set the width to center goods
terminal = os.environ.get('TERM')
width_len = width
cwd = os.getcwd()
IP = f"\033[1;35;0m {IPx.IP}"
current_version = platform.release()
system_info = platform.platform()
os_name0 = platform.system()


d = 'DICTIONARY'
print(display_header(d))
index_01 = 0
print(f'SYSTEM INFO'.center(width))
print(f'\033[1;35;m [{current_version}]  ...? '.center(width))
print(f'\033[1;35;m [{os_name0}] + [{terminal}] ...? '.center(width))
print(f'\033[1;35;m [{system_info}]  ...? '.center(width))
print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))  ### ADDD YOUR IP
print(f'\033[1;35;0m [{IP}]  ...? '.center(width))  ### ADDD YOUR IP

time.sleep(5)
clear()
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
    for key  in website_list:
        print("*" * 20)
        print(f'[{index_02}] : {key} ++')
        index_02 += 1


##  ORIGINAL CODE
# def download(to_connect):
#     try:
#         download = tf.keras.utils.get_file(f"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME}", to_connect)
#         SUCCESS = f"\n[SYS] - [SUCCESS] - DOWNLOADED {key} Successfully \n File Saved: ***** {download} ***** \n /Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME} [SUCCESS] "
#         print(f"{SUCCESS}".center(width))
#         print(f"{'x'*30}".center(width))
#         print()
#         end_time = time.time()
#         return download
#
#     except Exception as e:
#         print('error in download', str(e))



#### come back to
def download(to_connect):
    try:
        global DOWNLOAD_NAME
        if DOWNLOAD_NAME == '':
            empty_str = 'empty_value.torrent'
            DOWNLOAD_NAME = DOWNLOAD_NAME.join(empty_str)
            download = tf.keras.utils.get_file(f"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME}", to_connect)
            SUCCESS = f"\n[SYS] - [SUCCESS] - DOWNLOADED {key} Successfully \n File Saved: ***** {download} ***** \n /Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME} [SUCCESS] "
            print(f"{SUCCESS}".center(width))
            print(f"{'x'*30}".center(width))
            print()
            end_time = time.time()
            clear()
            return download
        elif DOWNLOAD_NAME != '':
            download = tf.keras.utils.get_file(
                f"/Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME}", to_connect)
            SUCCESS = f"\n[SYS] - [SUCCESS] - DOWNLOADED {key} Successfully \n File Saved: ***** {download} ***** \n /Users/macbook/Documents/CS/PROJECT/AutoDownloader/TEST_DOWNLOADS/{DOWNLOAD_NAME} [SUCCESS] "
            print(f"{SUCCESS}".center(width))
            print(f"{'x' * 30}".center(width))
            print()
            end_time = time.time()
            clear()
            return download


    except Exception as e:
        traceback.print_exc()
        print('error in download', str(e))

##########################################################
#################### DOWNLOADER ##########################


print(),print()
## to print LIST (not DICT), with prettyness
print(f'{display_list()}\n')
print('*' * (width_len * 2))


def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]


def torrent_pull(torrentlist):
    #website = 'http://itorrents.org/torrent/'
    print(f'[SYS] -- [{counter_00}] STARTING SIMPLE SEARCH [{counter_00}]'.center(width))
    for i in range(len(torrentlist)):
        print(torrentlist[i])
        if torrentlist[i] == torrentlist[2]:
            return torrentlist[i]
            
            
def magnet_pull(torrentlist):
    #website = 'http://itorrents.org/torrent/'
    print(f'[SYS] -- [{counter_00}] STARTING SIMPLE SEARCH [{counter_00}]'.center(width))
    for i in range(len(torrentlist)):
        print(torrentlist[i])
        if torrentlist[i] == torrentlist[0]:
            clear()
            return torrentlist[i]

        #if list[i] == website:
        if website in torrentlist[i]:
            print(f'[SYS] [{counter_00}] ** FOUND TORRENT LINK FROM SOUP PARSE ** [{counter_00}][SYS]'.center(width))
            clear()
            return i  ### INSTEAD RETUR MAGNET LINK

        else: 
            return torrentlist
        #i += 1
            
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dc


def url_req(URL00):
    try:
        print(URL00)
        HEADERS = {}
        HEADERS[
            "User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        req00 = urllib.request.Request(URL00, headers=HEADERS)
        resp00 = urllib.request.urlopen(req00)
        respData = resp00.read()

        saveFile = open("resp_data.txt", "w")
        saveFile.write(str(respData))
        saveFile.close()

        return req00
    except Exception as e:
        traceback.print_exc()
        print(f'Error in URL req {str(e)}')

counter_00 = 0
for key in website_list:
    print('[SYSTEM]**2 Sleeping for 3 Seconds')
    time.sleep(1)
    print()
    if counter_00 == index_end:  ## break
        sys.exit(0)
    else:
        print(f"[SYSTEM][{counter_00}] ++ Parsing ++ [{counter_00}]".center(width))
        print(f"{'x'*30}".center(width))
        print()
        print(f"{'*' * 30}".center(width))
        print(f'[{counter_00}] : {key} ++')
        counter_00 += 1



        def reverse(s):
            rev = ''
            for i in range(len(DOWNLOAD_NAME), 0, -1):
                rev += DOWNLOAD_NAME[i-1]
            return rev


        def bs_req(key):
            try:
                #payload = {'query': 'sega dreamcast'}
                print(f'[SYSTEM] -- [{counter_00}] Parsing Bs-Request With New Payload [{counter_00}] [SYSTEM]'.center(width))
                payload = {}
                # r = req.get(URL, params=payload)
                r = req.get(key)
                #print(req.url())
                print(r)
                print(f"{r}".center(width))
                print(f"{r.status_code}".center(width))
                print(f"{r.headers}".center(width))
            
                #print(f"{body_text} + \n\n\n\n\n {tbody}")
                clear()
                return r

            except Exception as e:
                traceback.print_exc()
                print(str(e))
                y = "[SYSTEM] [{counter_00}] Error When Parsing html data [{counter_00}] [SYSTEM]"
                print(f"{y}{e}")


    
        def run_downloader(key):
            website = '1337x.to'
            if (key.find(website))!=-1:
                print(f'[SYS] Torrent Site Found, running HTML Parser'.center(width))
                try:
                    start_time = time.time()
                    req00 = bs_req(key) ## NESTED REQUEST USING REQUESTS (for somereason, BS doesnt work with urllib)
                    #soup = torrent_grabber(req)
                    soup = BeautifulSoup(req00.text, "html.parser")
                    html_parsed = soup.prettify()
                    #print(soup.prettify)
                    #html_data = input("[SYS] Enter file name to save soup (.html)")

                    with open('torrent_downloader.html', "a") as f:
                        f.write(html_parsed)
                        print(f"[SYS] HTML_PARSE created at {os.getcwd()}")
                        t_name_list = soup.find(class_='col-9 page-content') # class ing-table - mau have to change between
                        t_name_list_items = t_name_list.find_all('a') # Catch the A tag to get download linksromsets
                        f = csv.writer(open('torrents_debug.csv', 'w')) ## create csv
                        f.writerow(['Torrent', 'File_Name'])
                        print(f'[SYS].. torrent .CSV created in app dir'.center(width))
                        # torrent_downloader.html.close()

                        f = csv.writer(open('torrents.csv', 'w')) ## create csv
                        f.writerow(['Torrent', 'Links'])
                       # f.close()
                        link_list = []
                        index00 = 0

                        for torrent_mag in t_name_list_items:
                            if index00 == 5:
                                break
                            else:
                                torrent = torrent_mag.contents[0]
                                link = f"[{index00}] + {torrent_mag.get('href')}"
                                #print(f'[{index00}]-- {type(link)} ADDED TO LIST/CSV \n --[{index00}] - {link})')

                                link_list.append(link)
                                f.writerow([torrent, link])
                                #f.close()
                        index00 += 1

                        print(f'TORRENT INDEX .CSV CREATED in {os.getcwd()}')

                        ##### PASS TO FUNCTION lst_search ####lst_search

                        index01 = 0
                        for link_string in link_list:
                            #print(f'[{index01}] -- {link_string}')
                            index01 += 1
                            if index == 5:
                                break

                        print('4444')
                        i_torrent_link = torrent_pull(link_list)
                       # i_torrent_link = i_torrent_link.translate({ord(i): None for i in '[2] +0'})
                        #i_torrent_link = i_torrent_link.translate({ord(i): None for i in '[2] +'})
                        i_torrent_link = i_torrent_link[6:]

                        #magnet = torrent_pull(link_list)

                        print('ffffffff')
                        print(i_torrent_link)

                        if len(i_torrent_link) > 0:
                            try:
                                print(f'[SYSTEM]** [{counter_00}] Connecting To TORRENT SERVER  [{counter_00}] ...\n '.center(width))
                                time.sleep(1)
                                URL00 = i_torrent_link
                            
                                req01 = url_req(URL00)
                                #print(req01)
                                #print(type(URL))
                                print('888888', req01)
                                check00 = 'True'
                                print('Torrent Server Parsing COmplete')
                                print(f'[SYSTEM]** [{counter_00}] TORRENT PARSE COMPLETE, MOVING TO DOWNLOAD  [{counter_00}] ...\n '.center(width))
                                return req01, check00, i_torrent_link

                            except Exception as e:
                                print(str(e))
                                print('Error in requesting TORRENT URL LIB')
                                sys.exit(1)
                        else:
                            return req01, check00, i_torrent_link

                except Exception as e:
                    traceback.print_exc()
                    print(f'Error when processing Soupbowl - Torrent {str(e)}')



  ########################## CLOSE THE TRY FUNCTION ABOVE AND RESET THE BOTTOM CODE FOR NO TORRENT FOUDN #############################
                #################################################################################

            else:            #  if (torrent in DOWNLOAD_NAME or website in DOWNLOAD_NAME): ## may need to set to website_list counter
                print(f'[SYS] [{counter_00}] No Torrents Found, Continuing To Parse, then moving on to download[{counter_00}] '.center(width))
                try:  #  w/header
                    start_time = time.time()
                    print(f'f[SYS] - SERVER CONNECT AT {start_time}'.center(width))
                    print(f'f[SYS] - *************************** - '.center(width))
                    print()

                    print(f'[SYSTEM]** [{counter_00}] Connecting To Server. Sleeping for 5 seconds [{counter_00}'.center(width))
                    print()
                    print(f'ARCHIVE.ORG may take longer than normal DO NOT QUITE PROGRAM, IT WILL RETURN ERROR CODE IF PARSING ERROR.'.center(width))
                    print()
                    time.sleep(1)
                    URL = key
                    #print(type(URL))
                    print(URL)
                    HEADERS = {}
                    HEADERS[
                        "User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

                    req00= urllib.request.Request(URL, headers=HEADERS)
                    resp = urllib.request.urlopen(req00)
                    respData = resp.read()


                    saveFile = open("resp_data.txt", "w")
                    saveFile.write(str(respData))
                    saveFile.close()

                    ######################## http://itorrents.org/torrent/65651608104F93C3DD5D090F327D7507F772A4BC.torrent


                    end_time = time.time()
                    time_to_complete = end_time - start_time

                    print(f'[SYSTEM]-- Server response in: [{time_to_complete}]'.center(width))
                    time.sleep(.5)
                    print(f'\n[SYSTEM] --Server response data saved to-- {saveFile} in program directory'.center(width))
                    print(f' XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX '.center(width))
                    check = 'False'
                    time.sleep(.5)
                    clear()
                    return req00, check, URL

                    # respData = resp.read(req)
                    ## save file for further analasys --


                except OSError as error:
                    clear()


                    return f"{'x' * 50} \n {traceback.print_exc()}[ERROR] [{counter_00}] On No Torrent Downlaoder[{counter_00}]  \n {str(error)}" and sys.exit(1)

            #return req00, check, URL

        # except Exception as e:
        #     print(f'[SYS] [{counter_00}]  SOUP PARSING ERROR  [{counter_00}] {str(e)}. ')
        #
        #


        ##################################################################################
        ##########################  START SEQUENCE TO RUN ###############################
        ##################################################################################
        loop = 0
        while loop == 0:
            try:
                cwd = os.getcwd()
               #global DOWNLOAD_NAME
                DOWNLOAD_NAME =  website_list[counter_00]
                DOWNLOAD_OG = DOWNLOAD_NAME  # set iteration
                #torrent = 'torrent'

                #DOWNLOAD_NAME = reverse(DOWNLOAD_NAME)
                NAME_LEN = len(DOWNLOAD_NAME)
                DOWNLOAD_NAME = DOWNLOAD_NAME[NAME_LEN - 25 :]


                print(f'[SYSTEM] File_Name :: {DOWNLOAD_NAME}')
                DOWNLOAD_NAME = DOWNLOAD_NAME.replace("/", "")
                DOWNLOAD_NAME = DOWNLOAD_NAME.replace("-", "")
                DOWNLOAD_LOC = str(cwd) + f'/{DOWNLOAD_NAME}'
                path = DOWNLOAD_NAME + DOWNLOAD_NAME
                print(f'[SYSTEM] File will be saved to: {path}')
                # os.makedirs(path, 777)
                print('[SYSTEM]**3 sleeping for 3 seconds: ')
                time.sleep(1)
                print()
                print(f"[SYSTEM] ++ RUNNING DOWNLOAD REQUEST++".center(width))
                print(f"{'x'*30}".center(width))
                print()

                if path:
                    start_time = time.time()
                    to_connect, parsed, soup_links = run_downloader(key)
                    print('99999999999')

                    if parsed == 'True': ###
                        try:
                            print(f'YAY SOUP HAS MADE IT THIS FAR'.center(width))
                            print(), print()

                            print('soup links', soup_links)
                            print(parsed)
                            print('to connect', to_connect)
                            print(), print()

                            print(f'[SYSTEM][{counter_00}] {key} [{counter_00}] [SYSTEM]\n \n '.center(width))
                            print()
                            print(f'[SYSTEM][{counter_00}] -- {cyan} RUNNING TORRENT DOWNLOADER {reset}-- [{counter_00}] [SYSTEM] '.center(width))

                            print('soup_links', soup_links)
                            print('to_connect', to_connect)

                            download(to_connect)

                            print(f'[SYSTEM]--[{counter_00}] ** {cyan}  DOWNLOAD COMPLETE {reset} ** [{counter_00}]--'.center(width))
                            loop += 1
                            break


                        except Exception as f:
                            traceback.print_exc()
                            print(f'error in torrent download, {str(f)}')
                            # sys.exit(1)
                    elif parsed == 'False': ## If file is not from torrent, just pass to keras downloader
                        try:
                            print(f'[SYSTEM][{counter_00}] -- {cyan} RUNNING FILE GRABBER {reset} -- [{counter_00}] [SYSTEM] '.center(width))
                            download_file = download(to_connect)
                            print(f'[SYSTEM][{counter_00}] -- {cyan} {DOWNLOAD_NAME} COMPLETE {reset} -- [{counter_00}] [SYSTEM] '.center(width))
                            print('****', DOWNLOAD_LOC)
                            loop+=1
                            #pass

                        except Exception as e:
                            traceback.print_exc()
                            print(f' File Rip Error, {str(e)}')


            except Exception as e:
                traceback.print_exc()
                print(f"[SYS] - [ERROR] - DOWNLOAD ERROR - [ERROR] \n {str(e)}")
                sys.exit(1)


counter_00 += 1
print(f'--LINE COUNTER--'.center(width))
print(f'[SYSTEM]-- COUNTER DEBUG **[{counter_00}]**'.center(width))




