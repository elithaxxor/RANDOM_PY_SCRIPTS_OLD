
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################
############## ################ ############## ############################## ################

        ###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
        ###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
        ###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
        ###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
        ###### TESTING VARIOUS WAYS TO IMPLIMENT THREADPOOL EXECUTOR ###
import traceback, logging, sys, os, asyncio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import math
from datetime import datetime
import platform
import sys
import asyncio
import time
import threading
import traceback
import tqdm
import time
from time import sleep
from tqdm import tqdm
from multiprocessing import Pool


#import keyboard
import pynput
from pynput import keyboard

import IPCHECKER as IPx
from IPCHECKER import *
from subprocess import call
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


def display_header2():
    print(
        '\t\t \033 The program calculates prime #s using Threading, Hyperthreading (if available), Multi-Threading & Multi-Processsing.\033 \n'
        '\t\t Too High of a range will result in CPU hangup / over-utilization'
        '\t\t \033[1;34;40m Bright Blu Stay off Drugs Kidz, mmkay? \033[1;34;40m \033[0m 1;34;40m]'
        '\t\t: '), print(), print('\t\t\t', )
    print(f"{'X' * 50}".center(width))
    print('X' * 150)
    print('X' * 150)
    print(f"{'X' * 50}".center(width))
    print(), print()

    print(' :: Testing Order:: '.center(width))
    print(' :: ITERATOR - WITH THREADING - SINGLE CORE:: '.center(width))
    print(' :: ITERATOR - NO THREADING - SINGLE CORE :: '.center(width))
    print(' :: ITERATOR - ASYNCIO (EVENT LOOPING) :: '.center(width))
    print(' :: ITERATOR - MULTI THREADING  :: '.center(width))


class LIST_FUNC():
    def __init__(self, delay=None):
        is_prime0 = self.is_prime0
       # CLASS_RANGE = self.CLASS_RANGE

    @staticmethod
    def iter_list(PRIMES_TEST_LIST):
        PRIME_TEST_LEN = len(PRIMES_TEST_LIST)

        for iter00 in tqdm(PRIMES_TEST_LIST): ######ADD  TQ
            # print( iter00 #, sep = "\t")
            print(iter00, end ="" )
            if (iter00 + 1) == PRIME_TEST_LEN:
                print('X' * 50)
                end00 = time.time()
                end_time00 = end00 - start00
                print(f'Thread Count: {threading.active_count()}')
                print(f'End time for Iter List Test , with [{threading.active_count()}] Active Threads')
                print(end_time00)
                break

    def is_prime0(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in tqdm(range(3, sqrt_n + 1, 10000)):
            if n % i == 0:
                return False
        return True


    @staticmethod
    def check_freq(FREQ_ITER):

        def check_sleep(amount):
            with Spinner():
                freq_count = 0
                #print(f'\033[0;35m; [{amount}].. Gettting to Work [{amount}]\033[0;35;m'.center(width))
                start = datetime.now()
                time.sleep(amount)
                end = datetime.now()
                delta = end - start
                return delta.seconds + delta.microseconds / 1000000

        print(f'{bblue}Calculating UNIX-CLOCK and Thread Clock Variance{reset}')
        print(f'{bblue}This is a test will return the the response time from daemon to executed thread{reset}')
        print(
            f'\033[1;34;40m If the program wheel freezes, then youve overloaded your system... \n {yellow} {time.ctime(current_t)} {reset}   \t\t')

        print()
        print('X' * 100)
        print(f'** Sleep Timer.. [{check_sleep}')

        start00 = time.time()
        start_time00 = time.ctime(start00)
        print(f'Calculation Start Time: , {yellow} **[{start_time00}]** {reset} '.center(width))
        error = sum(abs(check_sleep(0.050) - 0.050) for i in tqdm(FREQ_ITER, bar_format = "{percentage:3.0f}%"))
        end00 = time.time()

        end_time00 = end00 - start00
        ctyme = round(end_time00, 4)
        cry_time00 = time.ctime(end_time00)
        print(f'\t\t Captured date-time: {cry_time}')
        print('X' * 50)
        print('X' * 50)
        print(
            f'\n{bblue}The Average Clock Variance, from UNIX-CLOCK and CPU threads Thread: (Average is 16ms){reset} \n Average Error is {red} [%{error}] {reset}')
        print(f'The Test Range : {yellow} [{PRIMES_TEST_RANGE}] {reset}')
        print(f'Task  completed in: {yellow} [{ctyme}] Seconds {reset}')
        print(f'Task  completed at: {yellow}[{cry_time00}]{reset}')
        print(f' CPU Latency In MS: (16ms is considered average) \n Average Error is {red} [%{error}] {reset}')


def display_header():
    # print('*' * 75)

    color_red = Colors()
    global red0
    red0 = color_red.fgRed
    global reset0
    reset0 = color_red.reset

    x = 'x'
    print(f"{'X' * 125:^70}")
    print(f"{'X' * 125:^70}")
    pretty = f'{red0}xxx PRIME-NUMBER-SHREDDER xxx{reset0}'
    print(f'{pretty : ^70}')
    print(f"{'X' * 125: ^70}")

    one = (f'[USAGE] - [1] This is a python program that takes a list of download links, and saves each file to the programs download directory.')
    two = (f'[USAGE] - [2] The program works well with most download repositories, and currently gets around security measure implimented by \n[USAGE] - [2]b 1337x.to, itorrent && archive.org')
    three = (f'[USAGE] - [3] Download a LINK GRABBING extension from chrome, to pull the URLs off of the browsers tabs.')
    four = (f'[USAGE] - [4] Save the list into download_list.txt (Found in the Directory as this program')
    five = (f'[USAGE] - [5] Wait for downloads. Archive.org may be slow. The program saves both a LIST and DICT for further usage. (see functions)')
    six = (f'[SYSTEM] copyright material from Adel Al-Aali [SYSTEM]')


    print(f"{one:^70}")
    print(f"{two:^70}")
    print(f"{three:^70}")
    print(f"{four:^70}")
    print(f"{five:^70}")
    print(f"{six:^70}")
    print(f"{x * 20: ^70}")
    print(), print()




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


width = os.get_terminal_size().columns  # set the width to center goods
width_len = width
TICKER = 0

try:
    print(IPx.IP)
    #print(f'\033[0;35;47m \t\t[{IPx.get_ip()}]  ...? \033[0m 0;35;47m')
    width = os.get_terminal_size().columns  # set the width to center goods
    terminal = os.environ.get('TERM')
    width_len = width
    cwd = os.getcwd()
    IP = f"\033[1;35;0m {IPx.IP}"

    current_version = platform.release()
    system_info = platform.platform()

    os_name0 = platform.system()
    # print(os_name0)
    #
    # print(current_version)


    clear()


    display_header()
    print()
    print('X' * 50)
    print('X' * 50)
    print()
    print(f'SYSTEM INFO'.center(width))
    print(f'\033[1;35;m [{current_version}]  ...? '.center(width))
    print(f'\033[1;35;m [{os_name0}] + [{terminal}] ...? '.center(width))
    print(f'\033[1;35;m [{system_info}]  ...? '.center(width))
    print(f'\033[1;35;0m [{current_version}]  ...? '.center(width))   ### ADDD YOUR IP
    print(f'\033[1;35;0m [{IP}]  ...? '.center(width))   ### ADDD YOUR IP
    print('X' * 50)
    print('X' * 50)
    print()

    print('X' * 50)
    print('X' * 50)

    time.sleep(7)
except OSError as ose:
    print(str(ose))
except Exception as E:
    traceback.print_exc()
    print(str(E))



###########
color = Colors()
functions = LIST_FUNC()
spinner = Spinner()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset
############
print(f'{yellow}Enter Prime Test Range: {reset} \n')
PRIMES_TEST_RANGE_INPUT = input()
print('X' * 25)
print(f'{yellow} Enter the amount of iterations to test CPU FREQ (under 200 is suffeciant:{reset}')
FREQ_ITER = input()
PRIMES_TEST_INT = int(float(PRIMES_TEST_RANGE_INPUT))
global PRIMES_TEST_RANGE
PRIMES_TEST_RANGE = range(PRIMES_TEST_INT)
PRIME_TEST_LEN = len(PRIMES_TEST_RANGE)
PRIMES_TEST_LIST = list(PRIMES_TEST_RANGE)

print(f"{'X' * 50}".center(width))
print(f"{'X' * 50}".center(width))
print(f' :: Starting Test on {bblue}Multi-Threaded ITERATION Range Iterator{reset} :: '.center(width))
print(
    f' Multi-Threading,{red}NOT USING ThreadPoolExecutor to handle time-slicing. {reset} \n  {bblue}Effeciancy will depend on the Test Algo.{reset}'.center(
        width))
#print(f'starting: {yellow}[{current_time04}]{reset}'.center(width))
print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}'.center(width))
print(f"{'X' * 50}".center(width))
print(f"{'X' * 50}".center(width))
time.sleep(5), print(), print()


############# Multi Threading
# format = "%(asctime)s: %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )
def read_data():
    time.sleep(1)
    for i in PRIMES_TEST_RANGE:
        logging.debug('Starting')
        print(f'Process Reviewing Range Input {i}')
        time.sleep(.000000001)
        logging.debug('Exiting')

def action():
    for i in PRIMES_TEST_RANGE:
        logging.debug('Starting')
        print(f'Reading Data {i}')
        time.sleep(.000000001)
        logging.debug('Exiting')

#if __name__ == '__main__':
t = threading.Thread(name='Thread_2', target = read_data)
w = threading.Thread(name = 'Thread_3', target = action)
w2 = threading.Thread(target = read_data)


t.start()
w.start()
w2.start()

t.join()
print (f"d.isAlive(), {d.is_alive()}")
w.join()
print (f"w.isAlive(), {w.is_alive()}")
w2.join()

## End Sequence ##
###########################################
print(), print()
print('X' * 50)
print('X' * 50)
print()
end03 = time.time()
cry_time01 = time.ctime(end03)
end_time00 = end03 - current_time03
print(f'The Test Range : {bblue}[{PRIMES_TEST_RANGE}{bblue}]')
print(f'Task  completed in: {yellow}[{end_time00}{reset}]')
#print(f'Task  completed at: {yellow}[{cry_time00}{reset}]')
print(f'Time To Complete Task {red}[{end_time00}]{reset}')
print('X' * 50)
print('X' * 50)
print(' :: Killing Threads:: ')
print (f"d.isAlive(), {d.is_alive()}")
print (f"d.isAlive(), {w.is_alive()}")
print (f"d.isAlive(), {w2.is_alive()}")

TICKER += 1
time.sleep(7)

#############################################################################################################################################
##################################  ##################################  ##################################  ##################################
#############################################################################################################################################

#############################################################################################################################################
##################################  ##################################  ##################################  ##################################
#############################################################################################################################################

## Threading w/ daemon on

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

def daemon(name):
    for i2 in PRIMES_TEST_RANGE:
        logging.info("Thread %s: starting", name)
        time.sleep(2)
        logging.info("Thread %s: finishing", name)

d0 = threading.Thread(name='daemon00', target=daemon)
d0.setDaemon(True)

def non_daemon():
    for i2 in PRIMES_TEST_RANGE:
        logging.info("Thread %s: starting")
        logging.info("Thread %s: finishing")

t0 = threading.Thread(name='non-daemon00', target = non_daemon)
d0.start()
t0.start()
d0.join()
print (f"d0.isAlive(), {d0.is_alive()}")
t0.join()
print (f"t0.isAlive(), {t0.is_alive()}")

print (f"d.isAlive(), {w2.is_alive()}")


##########################################
##########################################
##########################################


threads = list()
for index in PRIMES_TEST_RANGE:
    logging.info("Main    : create and start thread %d.", index)
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    logging.info("Main    : before joining thread %d.", index)
    thread.join()
    logging.info("Main    : thread %d done", index)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(thread_function, PRIMES_TEST_RANGE)


        #
        #
        #
        #
        #    with Pool(2) as p:
        #       r = list(tqdm.tqdm(p.imap(functions.iter_list, PRIMES_TEST_RANGE), total=PRIME_TEST_LEN))
        # for i in tqdm(range(PRIMES_TEST_RANGE)):
        #     sleep(3), print(i)
        #     print(r)
