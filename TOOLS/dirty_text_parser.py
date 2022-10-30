import pandas as pd
import nltk, json, sys, traceback, platform, os
from collections import Counter
import nltk
import io, pprint
from pprint import pprint
from collections import OrderedDict


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

###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset
###########

class TextBuffer():
    def __init__(self):
        super(TextBuffer, self).__init__()
        self.os = os; self.io = io; self.json = json
        self.list_count = 0
        self._args = _args = []
        self.text_data = []
        self.current_platform = platform.platform
        self.io.DEFAULT_BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE
        print(f'[+] {self.current_platform} :: DEFAULT-BUFFER :: [{self.io.DEFAULT_BUFFER_SIZE}] [+]')
        self.text_file = input('')
        self.text_file = str(self.text_file)
        self.cwd = self.os.getcwd()
        self.text_loc = str(self.cwd) + f'/{self.text_file}'
        self.text_str = f'[SYSTEM]** Dump The Text Data To: [{self.text_file}] ** [SYSTEM]'

    def __enter__(self):
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'[-] [EXC_TYPE] \n{exc_value} \n\n[-] [exc_value]\n\n[-] [TRACEBACK-ERROR] \n[{traceback.format_exc}]')
    def __str__(self):
       # self.f.close()
        return '{}({})'.format(type(self).__name__, ', '.join(repr(getattr(self, a)) for a in self._args))  ## guidelines for res
    def __repr__(self):
        return '{}({})'.format(type(self).__name__,', '.join(str(getattr(self, a)) for a in self._args))
    ### website_list = [x.strip() for x in content]   ####
    ### ADD LOGIC TO COUNT NUMBERS                    ####
    
    def findDups(self):
        dups = list(OrderedDict.fromkeys(self.text_data))
        return dups 

    def text_file_len(self):
        with open(self.text_loc) as f:
            for line in open(self.text_loc):
                index = 0
                self.text_data = f.readlines(self.list_count)
                duplicates = findDups()
                print(str(duplicates))
                self.text_line = f.readline(self.list_count)
                self.text_len = len(self.text_data)
                self.list_count += 1
                print(f'{yellow}[+] --[READING]--\n[+] [{f.readline}]')
                index += 1
                for iterate in self.text_line:
                    print(f'[+] --Processing-- [#{index}]')
                    if index <= self.list_count:
                        print(f'[SYS]** FOUND [{iterate}] MATCHING FILES')
                    else:
                        break

                global text_len
                text_len = self.list_count
                print(f'[SYSTEM] Found --[{self.list_count}]-- Items in [{self.text_loc}]')
                break

    def start_Buffer(self):
        buffer_count = 0
        while buffer_count <= self.list_count:
            buffer_append = []
            matching_list = []
            with open(self.text_loc, buffering=200000) as f:
                self.current_process = f.readline()
                print(f'[+] Processing [#{self.text_len}] [+]')
                for line in f:
                    print(f'[+]--Line [{self.list_count}]')
                    buffer_append.append(line)
                if str(line) in buffer_append:
                    print('{red}[-] -[System Found Matching String]- [-]')
                    matching_list.append(str(line))
                    print(f'{yellow}[+]\t\t -[SCANNING-SYSTEM]- \t\t[+]{reset}\n\n\n [{matching_list}]')
                if buffer_count == self.text_len:
                    print(f'{red}[-] Reached The End of the List [-]\n[-] Exiting Buffer [-]{reset}')

    # return line
    ### CHEAP GENERATOR ###
    def cheap_Generator(self):
        n = 0
        list_count = self.list_count
        print(f'[+] Found [{self.list_count}] similar strings in the text doc')
        while n <= int(list_count):
            yield f'[{n}] {self.current_process}'
def main():
    try:
        yielded = []
        print('[+] --- [+]')
        print()
        TB = TextBuffer()
        textfile_len = TB.text_file_len()
        print(f'[+] Total Len Returned [{textfile_len}] [+]')
        TB.start_Buffer()
        yielded.append(TB.cheap_Generator())
        print(f'{bblue}[+] --[{yielded}]-- [+]{bblue}')
        print(f'[+] --[Confirming Total Len Returned]-- [{len(yielded)}] [+]\n\n {yielded} ')

    except Exception as e:
        print(str(e))
        print(f'{traceback.format_exc()} \n\n {sys.exc_info()[2]}')
        pass
if __name__ == '__main__':
    main()

    
    
