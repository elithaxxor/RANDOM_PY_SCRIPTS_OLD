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


import re
import linkGrabber

# links = linkGrabber.Links("http://www.google.com")
# links.find()
# # limit the number of "a" tags to 5
# links.find(limit=5)
# # filter the "a" tag href attribute
# links.find(href=re.compile("plus.google.com"))




def display_header(list_or_dict):
    # print('*' * 75)
    x = 'x'
    print(f"{'*' * 75:^70}")
    print(f"{'*' * 75:^70}")
    pretty = f'xxx DOWNLOAD {list_or_dict} xxx'
    print(f'{pretty : ^70}')
    print(f"{x * 20: ^70}")
    one = (f'[USAGE] - [1] This is a python program that takes a list of download links, and saves each file to the programs download directory.')
    two = (f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
    three = (f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
    four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
    five = (f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
    print(), print()
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")



def display_dict(rom_dict):
    d = 'DICTIONARY'
    print(display_header(d))
    index_01 = 0
    print(f'[SYSTEM] {type(rom_dict)}**--> ')
        
    for display in rom_dict:
        print(f'[SYSTEM]*[Dict] {display}')

def write_csv(soup):
    try:
        #game_name_list = soup.find(class_='download-directory-listing') # class ing-table - mau have to change between romsets
        f = csv.writer(open('games00.csv', 'w')) ## create csv
        f.writerow(['Game', 'File_Name'])
        return soup

    except OSError as error:
        return f"{'x' * 50} \n SAME FILE ERROR LINE 186 \n {str(error)}" and sys.exit(1)

def debugger():
    star = 4
    start = 0
    while True:
        print(f"{'*' * 50 : ^70}")
        start += 1
        if start == star:
            break


         
        

# req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})  # for downloads
# request = requests.get(URL).text  # for beatifulsoup
# print(req)
# print(requests)
# # webpage = urlopen(req) #.read().decode('utf-8)
# # print(webpage)

def downloader(URL):
    try:
        start_time = time.time()
        print(f'[{start_time}]')
        print()
        print('URL parsing', URL)
        DOWNLOAD_NAME = URL
        DOWNLOAD_NAME.split('/')[-1]  # remove the last char '/''
        cwd = os.getcwd()
        name_len = len(DOWNLOAD_NAME)
        DOWNLOAD_NAME = DOWNLOAD_NAME[name_len - 25 :]
        print(f'[SYSTEM] {DOWNLOAD_NAME}')
        #DOWNLOAD_NAME = DOWNLOAD_NAME.replace("/", "")
       #DOWNLOAD_NAME = DOWNLOAD_NAME.replace("-", "")
        DOWNLOAD_LOC = str(cwd) + f'/{DOWNLOAD_NAME}'
        path = DOWNLOAD_LOC + DOWNLOAD_NAME
        print('Download Name', DOWNLOAD_NAME)
        print('path creaated at:', path)
        #def rec_get(URL):
        
        
        
        
        #payload = {'query': 'sega dreamcast'}
        payload = {}
        #r = req.get(URL, params=payload
        
        # print(.URL)
        r = req.get(URL)
        print(r.headers)
        print('x' * 55)
        print(r)
        print(r.status_code)
        status_check = r.status_code



    # except Exception as e: 
    #     print(str(e))


    except OSError as error:
        print(f"{'x' * 50} \n SAME FILE ERROR LINE 186 \n {str(error)}" and sys.exit(1))
        sys.exit(1)

########################################################################################
############################ WRITE HTML DATA AND WRITE BS ELEMENTS #####################
############################# INITILIZE SOUP ###########################################
########################################################################################
    else:                 
        if (r.status_code == 200):        
            try:
                http = req.get(URL)
                soup = BeautifulSoup(http.content, 'lxml')      ######### <--------- USE / CHANGE LATER FOR BETTER RESULTS
                #soup = BeautifulSoup(http.content, "html.parser")
                print('SOUP --- PARSED')
                html_parsed = soup.prettify()
                print(soup.prettify)
                global game_name_list                                            #######  <--------- CHANGE GLOBAL PARAMATERS IF CHANGING CLASS BELOW
                game_name_list = soup.find(class_='download-directory-listing')  ##### <--------  USE / CHANGE LATER FOR BETTER RESULTS
                #html_data = input("[SYS] Enter file name to save soup (.html)")
                with open('html_data.html', "a") as f:
                    f.write(html_parsed)
                    print(f"[SYS] HTML_PARSE created at {os.getcwd()}")


            except Exception as e:
                print(str(e))

########################################################################################
############################ PARSE INFO TO CSV   ####################
########################################################################################     
                    
    finally:
        f = csv.writer(open('GAME_INDEX.csv', 'w')) ## create csv
        f.writerow(['game_index', 'dlinks']) 
        print('GAME INDEX CREATED')  
        game_list = []
        download_list = []
        
        index00 = 0
        if index00 <= len(game_name_list):
            
           
        for game_mag in game_name_list:
            game = game_mag[0]
            #game = game_name_list[0]
            game_name_list_items = game_name_list.find_all('a') ### OR download-listing-table
            game_list = game_list.append(game_mag)
            print(game_name_list, 0000000)
            
            download_list.append(game_name_list_items)
            print(download_list)
            print(type(download_list))
            
            print(game_name_list_items, 111111)
            print(debugger())
            print(debugger())

            print(game_name_list, 2222222)
            print(type(game_name_list))
           
            
            print(game_name_list, 2222222)

            print(debugger())
            print(debugger())
            
            games = game_mag[0]
            print(type(games))
            print(games, 333333)
            
        #game_name_list_items00 = game_name_list.find_all('a') # Catch the A tag to get download links
        
            link = f"[{index00}] + {game_name_list}"
            f = csv.writer(open('SUPER.csv', 'a'))
            
            f.writerow(str(link))
            f.writerow(game_name_list)
            f.writerow(game_name_list_items)
            f.writerow(games)
            f.writerow(game_mag[0])
            
            # game_name_list_items(link)
            print(f'{game_name_list.string},\n 888')
            print(game_mag)
            print(),print(),print()
            print(download_list)
            
            index00 += 1
            print(f'[{index00}]-- {type(game_mag)} ADDED TO LIST/CSV \n --[{index00}] - {game_mag})')
            print('555555555')
            print(game_name_list_items)
            return game_list, game_name_list, games
        
        else:
            print('SYSTEM FOUND NO GAMES IN SOUP BOWL')
        
            

            # except OSError as error:
            #     print(f"{'x' * 50} \n SAME FILE ERROR LINE 186 \n {str(error)}" and sys.exit(1))  


# except OSError as error:
#     print(f"{'x' * 50} \n SAME FILE ERROR LINE 186 \n {str(error)}" and sys.exit(1))


rom_dict = {'GENESIS':'https://archive.org/download/SegaGenesisMegaDriveRomCollectionByGhostware','SATURN':'https://archive.org/download/SegaSaturnRomCollectionByGhostware', 'DREAMCAST':'https://archive.org/download/DreamcastCollectionByGhostwareMulti-region', 'NES':'https://archive.org/download/NintendoMultiRomCollectionByGhostware','SNES':'https://archive.org/download/SuperNintendoUSACollectionByGhostware'}                          
URL = 'https://archive.org/download/NaomiRomsReuploadByGhostware/'
URL0 = downloader(URL)
print('download complete', URL0)
print(display_dict(rom_dict))

# DOWNLOAD_URL = 'https://archive.org/download/NaomiRomsReuploadByGhostware/Capcom_vs_SNK_2_Mark_of_the_Millennium_2001.zip'
# DOWNLOAD_UR'https://ia803008.us.archive.org/16/items/NaomiRomsReuploadByGhostware/NaomiRomsReuploadByGhostware_files.xml'


display_dict(rom_dict)

#rec = rec_get(URL)
#print('soup parse complete:' ,URL)


print(debugger())

x, y, z = downloader(URL0)
print(debugger())
print(888888)
print(type(x))
print(x)


print(x, 111111)
print(), print()

print(y, 2222222)
print(type(y))

df = pd.read_csv("/Users/macbook/Documents/CS/PROJECT/AutoDownloader/GAMES_00.csv")
df.head(30)

            




#print(df.head(30))
#soup = get_soup(URL)
#        return soup
#
#    except Exception as e:
#        print(str(e))
#        y = "[SYSTEM] Error When Parsing html data [SYSTEM]"
#        print(f"{y}")
#




        # with open('bodytext.txt', 'a') as a:
        #     a.write(body_text)
        #     print(f"[SYS] bodytext created at {os.getcwd()}")

      

        
   
            
            ### SAMPLE
            
#                        soup = BeautifulSoup(req00.text, "html.parser")
#                    html_parsed = soup.prettify()
#
#                    #print(soup.prettify)
#                    #html_data = input("[SYS] Enter file name to save soup (.html)")
#
#                    with open('torrent_downloader.html', "a") as f:
#                        f.write(html_parsed)
#                        print(f"[SYS] HTML_PARSE created at {os.getcwd()}")
#                        t_name_list = soup.find(class_='col-9 page-content') # class ing-table - mau have to change between
#                        t_name_list_items = t_name_list.find_all('a') # Catch the A tag to get download linksromsets
#                        f = csv.writer(open('torrents_debug.csv', 'w')) ## create csv
#                        f.writerow(['Torrent', 'File_Name'])
#                        print(f'[SYS].. torrent .CSV created in app dir'.center(width))
#                        # torrent_downloader.html.close()
#
#
#                        #return req00, soup, t_name_list_items
#
#
#                    f = csv.writer(open('torrents.csv', 'w')) ## create csv
#                    f.writerow(['Torrent', 'Links'])
#
#                    link_list = []
#                    index00 = 0
#                    for torrent_mag in t_name_list_items:
#                        if index00 <= len(t_name_list_items):
#                            torrent = torrent_mag.contents[0]
#                            link = f"[{index00}] + {torrent_mag.get('href')}"
#                            print(f'[{index00}]-- {type(link)} ADDED TO LIST/CSV \n --[{index00}] - {link})')
#
#                            link_list.append(link)
#                            f.writerow([torrent, link])
#                            index00 += 1
#                        else:
#                            break
#                    print(f'TORRENT INDEX .CSV CREATED in {os.getcwd()}'


#write_csv(soup)
#print('csv write complete ')




# PARENT CLASS 'download-directory-listing'

# SIBLING CLASS 'directory-listing-table'
##### SOUP SOUP soup.find(class_='directory-listing-table') ## 


#game_name_list_items = game_name_list.find_all('a') # Catch the A tag to get download links
#print(game_name_list_items)



