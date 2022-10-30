import time
import pyautogui


def sendMsg():
    time.sleep(5)
    text = open('spambot.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
sendMsg()


mport random
n = random.random()
print(n)



## generatinng random in a range 
import random
n = random.randint(1,50)
print(n)


 4
 5class TimerError(Exception):
 6    """A custom exception used to report errors in use of Timer class"""
 7
 8class Timer:
 9    def __init__(self):
10        self._start_time = None
11
12    def start(self):
13        """Start a new timer"""
14        if self._start_time is not None:
15            raise TimerError(f"Timer is running. Use .stop() to stop it")
16
17        self._start_time = time.perf_counter()
18
19    def stop(self):
20        """Stop the timer, and report the elapsed time"""
21        if self._start_time is None:
22            raise TimerError(f"Timer is not running. Use .start() to start it")
23
24        elapsed_time = time.perf_counter() - self._start_time
25        self._start_time = None
26        print(f"Elapsed time: {elapsed_time:0.4f} seconds")



