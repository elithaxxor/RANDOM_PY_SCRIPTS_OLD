import sys
import asyncio
import time
import threading
import traceback
#import antigravity

#webbrowser.open("https://xkcd.com/2258")



y = 10000
yy = range(0, 10000)
x = range(0, 10000)
y_list = list(range(y))
len_y_list = len(y_list)

print('X' * 50)
print('Current Iteration Depth: ', len_y_list)
time.sleep(1)
print('X' * 50)

try:
    def iter_list():
        for iter00 in (y_list):
            #print( iter00 #, sep = "\t")
            print(iter00, )

            if (iter00 + 1) == len_y_list:
                print('X' * 50)
                end00 = time.time()
                end_time00 = end00 - start00
                print(f'Thread Count: {threading.active_count()}')
                print(f'End time for singe threaded process, with [{threading.active_count()}] Active Threads')
                print(end_time00)
                break

            #return (iter00) # sep = '\n')



    t = threading.Thread(name = 'first_thread', target=iter_list, args=())
    start = time.time()
    t.start()
    global start00
    start00 = time.time()
    print(),print()
    print(type(t))


    time.sleep(3)

    print(), print()
    print('X' * 50)

    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####
    #### #### ####     #### #### ####     #### #### ####     #### #### ####     #### #### ####



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


