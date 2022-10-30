
print("\033[0;37;40m Normal text\n")
print("\033[2;37;40m Underlined text\033[0;37;40m \n")
print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")

print(
    "\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
print(
    "\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
print(
    "\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
print(
    "\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
print(
    "\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
print(
    "\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print(
    "\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
print(
    "\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
print(
    "\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

import traceback
import logging
import sys
import asyncio
import time
import os
import threading
import shutil
import concurrent.futures
import urllib.request
import math
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import sys
import asyncio
import time
import threading
import traceback
import antigravity

from time import sleep
from tqdm import tqdm
from multiprocessing import Pool
import tqdm
import time
import ipchecker as IPx
from IPximport import *


class LIST_FUNC():
    def __init__(self, delay=None):
        def iter_list():
            for iter00 in (PRIME_TEST_LIST):
                # print( iter00 #, sep = "\t")
                print(iter00, )
                if (iter00 + 1) == len_y_list:
                    print('X' * 50)
                    end00 = time.time()
                    end_time00 = end00 - start00
                    print(f'Thread Count: {threading.active_count()}')
                    print(f'End time for singe threaded process, with [{threading.active_count()}] Active Threads')
                    print(end_time00)
                    break

        def search(self):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 10000):
            if n % i == 0:
                return False
        return True

    def check_sleep(amount):
        start = datetime.now()
        time.sleep(amount)
        end = datetime.now()
        delta = end - start
        return delta.seconds + delta.microseconds / 1000000


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

            ######### CLASSES ##########

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    ######### CLASSES ##########


# SELF_IP =
# requests.get('https://api.ipify.org').text  # api to pull self ip via text
# gip = pygeoip.GeoIP('Geolitecity.dat')
# res = gip.record_by_addr('')

A = IPx.SELF_IP()  # = SELF_IP
B = IPx.gip()
C = IPx.res()

print(A)
print(B)
print(C)

system_info = platform.platform()
width = os.get_terminal_size().columns  # set the width to center goods
terminal = os.get_os
width_len = width
cwd = os.getcwd()
os_name = platform.system()
print(os_name)
current_version = os.platform.release()
system_info = os.platform.platform()
os_name = os.platform.system()
print(os_name)

print('X' * 50)
print('X' * 50)
print(f'\033[0;35;47m Magenta\t\t[{current_version}]  ...? \033[0m 0;35;47m')
print(f'\033[0;35;47m Magenta\t\t[{os_name}] + [{terminal}] ...? \033[0m 0;35;47m')
print(f'\033[0;35;47m Magenta\t\t[{system_info}]  ...? \033[0m 0;35;47m')
print(f'\033[0;35;47m Magenta\t\t[{current_version}]  ...? \033[0m 0;35;47m')  ### ADDD YOUR IP
print('X' * 50)
print('X' * 50)

# print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
spinner = Spinner()
spinner.spinning_cursor()
prime_num = find_prime()
PRIME = find_prime.search()

TICKER = 0
PRIMES = list(range(0, 10000))
print(f"{'X' * 100}")
print()
print('\033[1;34;40m If the program wheel freezes, then youve overloaded your system...  \033[0m 1;34;40m    \t\t')
print(f'Enter The Testing Range: '.center(width))
print(f"{'X' * 25}".center(width))

PRIMES_TEST_RANGE_INPUT = input()
PRIMES_TEST_INT = int(float(PRIMES_TEST_RANGE_INPUT))
PRIMES_TEST_RANGE = range(PRIMES_TEST_INT)
PRIME_TEST_LEN = len(PRIMES_TEST_RANGE)

PRIMES_TEST_LIST = list(PRIMES_TEST_RANGE)

print(type(PRIMES_TEST_RANGE_INPUT))
print(type(PRIMES_TEST_INT))
print(type(PRIMES_TEST_RANGE))
print(type(PRIMES_TEST_LIST))

print('Initiating Boat'.center(width))
print(f"{'X' * 25}".center(width))
print('Recursion Lenght: ', PRIMES_TEST_RANGE)
print('Current Iteration Depth: ', PRIME_TEST_LEN)

time.sleep(1.5)

start = time.time()
start00 = time.time()
cry_time = time.ctime(start)


def _foo(my_number):
    square = my_number * my_number
    time.sleep(1)
    return square


if __name__ == '__main__':
    with Pool(2) as p:
        r = list(tqdm.tqdm(p.imap(_foo, PRIMES_TEST_RANGE_INPUT), total=PRIME_TEST_LEN))
for i in tqdm(range(PRIMES_TEST_RANGE)):
    sleep(3), print(i)
    print(r)

period_list = ['..........']
period_list *= 100
len_period_list = len(period_list)
print(len_period_list)
print(period_list)

print(), print(), print()

print(" ### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "                ##                  ##              ##                  ##                ",
      "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ",
      " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ", print('...?'),
      )

print(
    "\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print(
    "\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")

print("\033[1;34;40m Bright Blue    '\033[1;34;40m \033[0m 1;34;40m]")

print(f"{'X' * 50} \n\n")
print(
    '\t\t \033 The program calculates prime #s using Threading, Hyperthreading (if available), Multi-Threading & Multi-Processsing.\033 \n'
    '\t\t Too High of a range will result in CPU hangup / over-utilization'
    '\t\t \033[1;34;40m Bright Blu Stay off Drugs Kidz, mmkay? \033[1;34;40m \033[0m 1;34;40m]'
    '\t\t: '), print(), print('\t\t\t', )
print(f"{'X' * 50}".center(width))

print(" ### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "                ##                  ##              ##                  ##              ##  ",
      " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####",
      "#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### ",
      " #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### #### "
      )

print('X' * 50)
print('Current Iteration Depth: ', len_y_list)
time.sleep(1)
print('X' * 50)

print(f"{'X' * 50}".center(width))
print(f'[{TICKER}] :: Starting multi-processing with daemon on :: [{TICKER}]  '.center(width))
print(
    f'This is Multi-Processing, this may be more effeciant than the former, depending on the Test Algo.'.center(width))
print(f"{'X' * 50}".center(width))

threading_prime = find_prime.search()

try:

    # return (iter00) # sep = '\n')

    t = threading.Thread(name='first_thread', target=iter_list, args=())
    start = time.time()
    t.start()
    global START
    START = time.time()
    current_time = ctime(START)

    print(), print()
    print(type(t))

    time.sleep(3)

    print(), print()
    print('X' * 50)

    print(), print()
    print('X' * 50)

    print('starting sequence 2')
    time.sleep(.5)

    print('X' * 50)

    start = time.time()

    for list00 in range(y):
        print(list00)

    print(), print()
    print('X' * 50)

    end = time.time()
    end_time00 = end - start
    print('iteration for hyper-thread, should be the fastest!')
    print(end_time00)
    print('X' * 50)
    print(), print()
    time.sleep(3)

    print('Starting Next Iteration')
    tine.sleep(.5)
    start05 = time.time()

    for list00 in range(y):
        async def fetch_data02(yy):
            task = asyncio.create_task(read_data(yy))
            await task
            await asyncio.sleep(.000001)


        async def read_data(yy):
            print(yy)
            await asyncio.sleep(.00000001)


        print(list00)

    print(), print()
    print('X' * 50)

    end05 = time.time()
    end_time00 = end05 - start05
    print(
        'iteration for multi-threaded process (should be slower, slightly optimized, depending on variable / function)')

    print(end_time00)

    print(), print()
    print('X' * 50)

    time.sleep(3)

    start00 = time.time()
    for list00 in range(len(x)):
        print(list00)

    print(), print()
    print('X' * 50)

    end00 = time.time()
    end000 = end00 - start00
    print('synchronous threading, maxing out a single clock:, just range ')
    print(end000)
    time.sleep(3)
    print(), print()
    print('X' * 50)

    time.sleep(1)
    start01 = time.time()

    for new_line in range(len(x)):
        print(x[new_line])

    print('Synrchousoues threading, as before, but with range-len ')

    print(), print()

    print('X' * 50)
    end01 = time.time()
    end_time01 = end01 - start01
    print(end_time01)
    time.sleep(3)
    print('X' * 50)

    print(), print()

    print('starting sequence 2')
    time.sleep(1)
    start02 = time.time()


    async def fetch_data():
        print('start fetching ')
        task00 = asyncio.create_task(another_thread())
        value00 = await task00
        #  print(value00)
        await asyncio.sleep(.000000000000000001)
        print('done fetching')

        return {'Data ': 1}


    async def another_thread():
        print('antoher fucking thread')
        print('X' * 50)
        await asyncio.sleep(.00000000000000000001)


    async def print_numbers():
        for i in range(0, 100000):
            print(i)
            await asyncio.sleep(0.00000000000000000001)


    async def main00():  ## creating tasks // futures -- a place holder for a value that will exist in the future.
        print('starting sequence on value01 ')

        task01 = asyncio.create_task(fetch_data())
        task02 = asyncio.create_task(print_numbers())
        value01 = await task01
        print(value01)

        await task02


    #   print('startin sequence on value02 ')
    #    value02 = await task02
    #   print(value02)

    asyncio.run(main00())
    end02 = time.time()
    end_time02 = end02 - start02
    print('thread inside of a thread:: (SHOULD BE THE SLOWEST) ')
    print(end_time02)
    time.sleep(3)
    print(), print(), print()

    print('startin sequence 3: ')
    start03 = time.time()


    async def main01():
        print('adel')
        # await foo('text') ## makes async func wait for foo func to execute.
        task = asyncio.create_task(foo('text'))
        await task
        await asyncio.sleep(.000001)  ## we are pausing the execution to function, and then run the asncio task above
        print('finished')


    async def foo(text):
        for fast in range(0, 100000):
            print(fast)
        await asyncio.sleep(.000001)


    asyncio.run(main01())

    print('Just as single thread, no hyperthreading! ')
    end03 = time.time()
    end_time03 = end03 - start03
    print(end_time03)
    time.sleep(3)
    print(), print(), print()

    print(), print(), print()


    def print_to_stderr(*a):
        print(*a, file=sys.stderr)
        print_to_stderr("Hello World")


    def print_to_stdout(*a):
        print(*a, file=sys.stdout)


    print_to_stdout("Hello World")

    ##
    totaltotal = time.time()
    total_end = start - totaltotal
    print('END OF SEQUENCE')
    print(total_end)


except Exception as f:
    traceback.print_exc()
    print(str(f))

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

try:
    with Spinner():
        print(f'[{[TICKER]}][## STARTING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print("f{'X' * 50}".center(width))

        print('Calculating UNIX-CLOCK and Thread Clock Variance')
        print('This is a test will return the the response time from daemon to executed thread')
        print(f'Gettting to Work'.center(width))
        time.sleep(.1)
        print(f'\t\t You entered:: {PRIMES_TEST_RANGE}')
        print(f"{'X' * 20}".center(width))
        time.sleep(.5)

        start00 = time.time()
        start_time00 = time.ctime(start00)
        print('Calculation Start Time: ', start_time00)
        error = sum(abs(check_sleep(0.050) - 0.050) for i in PRIMES_TEST_RANGE)
        end00 = time.time()
        end_time00 = end00 - start00
        cry_time00 = time.ctime(end_time00)
        print(f'[{[TICKER]}][## ENDING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print(f'\t\t Captured date-time: {cry_time}')

        print('X' * 50)
        print('X' * 50)

        print(
            f'\nThe Average Clock Variance, from UNIX-CLOCK and CPU threads Thread: (Average is 16ms) \n Average Error is [%{error}]')
        print(f'The Test Range : [{PRIMES_TEST_RANGE}]')
        print(f'Task  completed in: [{end_time00}]')
        print(f'Task  completed at: [{cry_time00}]')
        print('X' * 50)
        print('X' * 50)

        TICKER += 1
        time.sleep(4)

except Exception as f:
    traceback.print_exc()
    print(str(f))

#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
###                  ###                ###                ###
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####


##### ###### ###### ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######


#### PRIME #S START

try:
    with Spinner():
        time.sleep(20)

        print(f'[{[TICKER]}][## STARTING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print(f'\t\t [TEST RANGE:]  {PRIMES_TEST_RANGE}')
        print('X' * 50)
        print(f'[{TICKER}] \t\t Starting New Thread / Process \t\t [{TICKER}]')
        print(f'Captured date-time: {cry_time}')
        print('X' * 50)
        time.sleep(1)


        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False

            sqrt_n = int(math.floor(math.sqrt(n)))
            for i in range(3, sqrt_n + 1, 10000):
                if n % i == 0:
                    return False
            return True


    def main():
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
                print('%d is prime: %s' % (number, prime))
        #
        # if __name__ == '__main__':
        #      main()

        main()

        print('X' * 50)

        print(type(main))
        end0 = time.time()
        end_time0 = end0 - start
        print(end_time0)
        print(), print()
        print('End time for MULTIPROCESS')

        print(end_time0)
        TICKER += 1
        time.sleep(2.5)


    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

    with Spinner():
        try:
            start00 = time.time()
            #  for i in PRIMES:
            for i, d in zip(PRIMES, map(is_prime, PRIMES)):
                t.start()
                print('%d is prime: %s' % (i, d))  ## may have to chagne %d and %s
            print('X' * 50)
            print(type(t))
            print(f'Thread Count: {threading.active_count()} ')

            print(), print()
            end00 = time.time()
            end_time00 = end00 - start00
            print(f'End time for multi/single threaded process, with [{threading.active_count()}] Active Threads')
            print(end_time00)
            TICKER += 1
            time.sleep(3)
            id00 = threading.get_ident()
            print('[TRHEAD ID]** ', id00)

            # id00 = threading.get_ident()
            # print('[TRHEAD ID]** ', id00)

        except Exception as f:
            traceback.print_exc()
            print(str(f))

        #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

        try:
            with Spinner():
                start05 = time.time()
                for i, d in zip(PRIMES, map(is_prime, PRIMES)):
                    async def fetch_data02(PRIMES):
                        task = asyncio.create_task(read_data(PRIMES))
                        await task
                        await asyncio.sleep(.00000000000001)


                    async def read_data(PRIMES):
                        print(PRIMES)
                        await asyncio.sleep(.00000000000001)


                    print(i, d)

                end05 = time.time()
                end_time00 = end05 - start05
                print(
                    'iteration for multi-threaded process (should be slower, or slightly optimized, depending on variable / function)')

                print(end_time00)
                TICKER += 1
                time.sleep(3)

        except Exception as f:
            traceback.print_exc()
            print(str(f))


except Exception as z:
    traceback.print_exc()
    print(str(z))

##### ###### ###### ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######
##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######


try:
    with Spinner():
        print(f'[{[TICKER]}][## STARTING \033 ANOTHER \033 CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print("f{'X' * 50}".center(width))

        print(), print()

        print(f"{'X' * 50}".center(width))
        print('Calculating UNIX-CLOCK and Thread Clock Variance')
        print('This is a test will return the the response time from daemon to executed thread')
        print(f'Gettting to Work'.center(width))
        time.sleep(.1)
        print(f'\t\t You entered:: {PRIMES_TEST_RANGE}')
        print(f"{'X' * 20}".center(width))
        time.sleep(.5)

        start00 = time.time()
        start_time00 = time.ctime(start00)
        print('Calculation Start Time: ', start_time00)
        error = sum(abs(check_sleep(0.050) - 0.050) for i in PRIMES_TEST_RANGE)
        end00 = time.time()
        end_time00 = end00 - start00
        cry_time00 = time.ctime(end_time00)
        print(f'[{[TICKER]}][## ENDING CPU VARIANCE CALCULATION ##[{[TICKER]}]\t\t'.center(width))
        print(f'\t\t Captured date-time: {cry_time}')

        print('X' * 50)
        print('X' * 50)

        print(
            f'\nThe Average Clock Variance, from UNIX-CLOCK and CPU threads Thread: (Average is 16ms) \n Average Error is [%{error}]')
        print(f'The Test Range : [{PRIMES_TEST_RANGE}]')
        print(f'Task  completed in: [{end_time00}]')
        print(f'Task  completed at: [{cry_time00}]')
        print('X' * 50)
        print('X' * 50)

        TICKER += 1
        time.sleep(4)

except Exception as f:
    traceback.print_exc()
    print(str(f))

print(f"{'X' * 50}".center(width))
print(f'{TICKER}\033 ::starting multi-processing with daemon off:: \033 {TICKER} '.center(width))
print(
    f'This is Multi-Processing, this may be more effeciant than the former, depending on the Test Algo.'.center(width))
print(f"{'X' * 50}".center(width))


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(.000000000001)
    id00 = threading.get_ident()
    print(id00)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    start = time.time()
    logging.info("Main    : before creating thread")

    X = threading.Thread(name='thread04', target=is_prime, args=(i,))

    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, prime))
    #

    for i, d in zip(PRIMES, map(is_prime, PRIMES)):
        logging.info("Main    : before running thread")
        X.start()
        print('%d is prime: %s' % (i, d))

        logging.info("Main    : wait for the thread to finish")
        X.join()
        logging.info("Main    : all done")

    end = time.time()
    end_time = end - start
    cry_end = time.ctime(end)
    print(f'End Time: [{cry_end}]')
    print(f'Time to complete:  [{end_time}]')
    TICKER += 1

##### ###### ###### ##### ###### ########### ###### ########### ###### ########### ###### ########### ###### ########### ###### ######


print(f'[{TICKER}] :: Starting multi-processing with daemon on :: [{TICKER}]  '.center())
print(f'This is Multi-Processing, this may be more effeciant than the former, depending on the Test Algo.')


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(.000000000001)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    start = time.time()
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join
    logging.info("Main    : all done")

    end = time.time()
    end_time = end - start
    cry_end = time.ctime(end)
    print(f'End Time: [{cry_end}]')
    print(f'Time to complete:  [{end_time}]')
    TICKER += 1

######################
#################

x = threading.Thread(name='thread01', target=lambda a: sys.stdout.write("\n".join(a) + "\n"))
try:
    for i in range(PRIMES_RANGE):
        t = threading.Thread(target=is_prime, args=(i,))
        t.start()
    print('main thread end!')
    if action(is_prime):
        sys.exit(1)
except IOError as f:
    print(str(f))

x.start()

print('System End... Lets go to the sky.. ')
timer.sleep(1)
webbrowser.open("https://xkcd.com/2258")
timer.sleep(2)
sys.exit()


def prime():
    time.sleep(.1)
    print(b.result())  # b will never complete because it is waiting on a.
    return .1


def not_prime():
    time.sleep(.01)
    print(a.result())  # a will never complete because it is waiting on b.
    return .01


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(even)
b = executor.submit(odd)

if True:
    sys.exit()
else:
    sys.exit()

#
#
# def wait_on_future():
#     f = executor.submit(pow, 5, 2)
#     # This will never complete because there is only one worker thread and
#     # it is executing this function.
#     print(f.result())
#
# executor = ThreadPoolExecutor(max_workers=1)
# executor.submit(wait_on_future)
#
#
# # establish paralell task
# def task_iseven(num00):
#     for num00 in var_list:
#         return num00


#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
##              ##                 ##                 ##                ###               ###
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####

#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
#### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####


#
#
# sys.exit()
#
#
# # ## define multi-threading function
# # def countHighFrequencyItem(var_list):
# #     if len(var_list) == 0:
# #         return 0
#
#
# # all_tasks = []
# #
# # with ThreadPoolExecutor(max_workers=4) as executor:
# #     for index in range(len(var_list)):
# #         all_tasks.append(
# #             executor.submit(
# #                 task,
# #                 var_list[index],
# #                 index))
# #         temp_res = list(range(len(var_list)))
# #
# #     # parse the completed tasks
# #     for future_var in as_completed(all_tasks):
# #         tooFrequent, index00 = future_var.result()
# #         temp_res[index00] = tooFrequent
# #
# #     count = 0
# #     for is_frequent in temp_res:
# #         if is_frequent:
# #             print(temp_res)
# #             count += 1
# #            # return count
# #
#
#
#
#
#
#
# # x = lambda x=var_list: sys.stdout.write("\n".join(var_list) + "\n")
# # print(x)
# # x()
#
#
# ###
#
# ## for loop i lambda
# x = threading.Thread(name ='thread01', target = lambda x = var_range: list(map(print, x)))
#
#
# print (threading.currentThread().getName()) ## to get thread name ##
#
# # x()
#
#
# if True:
#     print('goodbye')
#     sys.exit()
#
# #
# # # for loop in threading lambda
# # t= threading.Thread(name='func'+str(i), target=lambda i=i: func())
# #
# # ## my version
# #
# #
# #
# #
# #
# #
# # if xy:
# #     print('v working')
# # else:
# #     print('v not working')
# #
# # if t:
# #     print('t working')
# # else:
# #     print('t not working')
# #
# # if x:
# #     print('x working')
# #     sys.exit
# #
# # else:
# #     print('v not working')
# #     sys.exit()
#
#
#
#
#
# # if x:
# #     print('working')
# #     sys.exit(1)
# # else:
# #     print('not working')
# #     sys.exit(0)
# #
#
#
#
#
#
#
#
#
#
# #- Method 1: pass the method to be executed as a parameter to the Thread The construction method of the model
# ## SPAWN A THREAD AND PASS IT ARGUMENTS, TO TELL WORK WHAT TO DO
#
# def action(arg):
#     time.sleep(1)
#     print('the arg is:% ', arg)
#
# for i in range(4):
#     t =threading.Thread(target=action,args=(i,))
#     t.start()
#
# print('main thread end!')
#
# if action(arg):
#     sys.exit(1)
#
# #### METHOD 2 ### A LITTLE BIT MORE COMPLEX THREAD, WHERE EACH THREAD IS NAMED
#
# def worker():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(2)
#     print(threading.currentThread().getName(), 'Exiting')
#
# def my_service():
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(3)
#     print(threading.currentThread().getName(), 'Exiting')
#
# t = threading.Thread(name='my_service', target=my_service)
# w = threading.Thread(name='worker', target=worker)
# w2 = threading.Thread(target=worker) # use default name
#
# w.start()
# w2.start()
# t.start()
#
#
# #- Method 2: from Thread Inherit and rewrite run()
# class MyThread(threading.Thread):
#     def __init__(self,arg):
#         super(MyThread, self).__init__()#Note: be sure to explicitly call the initialization function of the parent class.
#         self.arg=arg
#     def run(self):#Define the function to run for each thread
#         time.sleep(1)
#         print('the arg is:%s\r' % self.arg)
#
# for i in range(4):
#     t =MyThread(i)
#     t.start()
#
# print('main thread end!')
#
#
#
#
# ### Method 3 ## Creating thread using threading Module
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, 5, self.counter)
#       print ("Exiting " + self.name)
#
# def print_time(threadName, counter, delay):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# print("Exiting Main Thread")
#
#
#
#
