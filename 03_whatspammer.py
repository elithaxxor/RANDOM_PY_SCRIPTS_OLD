import time
import pyautogui
import random
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import time
import time
import pywhatkit
import sys
#from dateutil.relativedelta import relativedelta
import os
import re

width = os.get_terminal_size().columns  # set the width to center goods
width_len = width
cwd = os.getcwd()


class current_time(datetime):
    now = datetime.now()
    custom_date_time = timedelta(hours=3, minutes=5, seconds=30)
    end_loop = (now + custom_date_time)

    def __init__(self):
        self.time = time
        self.re = re
        super(current_time, self).__init__()

    def time_now(self):
        global hour
        hour = self.hour
        print(hour) 


        # min00 = min_pattern(now)
        # global timer
        # timer = random.randrange(5.0, 8.0)
        # print('now', now)
        # print('current hour', now.hour)
        # print(f'Current min,  {min00}')
        # print('custom_date_time', custom_date_time)





    def min_pattern(self, now):
        time_pattern = re.compile(r"[:\d:]")
        time_list = time_pattern.findall(str(now))
        min_str = ''
        min_list = time_list[11:13]
        min_list = min_list[0:2]
        min_str = min_str.join(min_list[0:2])
        return min_str

    def sendMsg(now, hour, sleeper):
        with open('spambot.txt', 'r') as file:
            line = file.readline()
            ticker = 0
            while str(now) != end_loop:  # end_loop:
                for each_line in file:
                    min_str01 = min_pattern(now)
                    msg_min00 = int(min_str01) + int(sleeper) + 1
                    if now == end_loop:
                        return f'SENT [{ticker}] MESSAGES to [INSERT USER PHONE# INPUT] '
                    else:
                        print('X' * 50)
                        # msg_min00 = int(min_str) + int(sleeper) + 1
                        print(f'Min: {msg_min00} :: Sleeper: {sleeper} \n')
                        print(f'The message: {each_line} will be printed at {hour}:{msg_min00}')
                        print()
                        pywhatkit.sendwhatmsg('+18622371332', f'{each_line}', hour, msg_min00)
                        pyautogui.typewrite(each_line)
                        pyautogui.press('enter')
                        each_line = file.readline()
                        ticker += 1
                        print(f'Sent Message # {ticker} at {hour}:{msg_min00}')
                        msg_min00 += sleeper + 2
                        print('message timer with sleeper', msg_min00)
                        break  #### PASS OR CONTINUE??


def display_header():
    print('whatsapp spammer--'.center(width))
    x = 'x'
    # pretty = f'xxx DOWNLOAD {list_or_dict} xxx'
    # print(f'{pretty : ^70}')
    print(f"{x * 20: ^70}")
    # zero = (f'[USAGE] - [0] {dl.href_str}')
    one = (f'[USAGE] - [1] This is a python program that spams WhatsApp messages via the web interface.')
    two = (
        f'[USAGE] - [2] You will see your mouse move with out you contorling it,  Do not be alarm, the program is workin.')
    three = (f'[USAGE] - [3] You can edit the send list by going to the CWD and editing spam.txt')
    four = (f'[USAGE] - [4] Each line indicates a new message, do not leave blank spaces or blank lines.')
    five = (f'**********************************************************************************************')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')

    # print(f"{zero:^70}")
    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print()


try:
    display_header()
    print()
    print(f'-- WHATSAPP SPAMMER --'.center(width))
    print('Current OS Navigator: ', os.name)
    print(f'Current Working Directory: {cwd}')
    print()
    print('starting loop')

    print(), print(), print()
    while str(now) != end_loop:
        print(f' The loop is set to end in (hour, min, second):  {custom_date_time} \n')
        print(f'END LOOP TIME: {end_loop} \n')
        # print('Min List:', min_list)
        # print('Current minute (as str)', min_str)
        global sleeper
        sleeper = random.randint(2, 5)
        time.sleep(sleeper)

        sendMsg(now, hour, sleeper)

except Exception as e:
    print(str(e))
    print('system exiting due to sendMSG error.'.center(width))
    sys.exit(1)

finally:
    print('Either you have reached the message limit, or there was an error in the program. See Error Code Above')
