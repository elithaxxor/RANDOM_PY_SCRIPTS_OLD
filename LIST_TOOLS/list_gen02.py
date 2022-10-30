import pandas as pd
import nltk, json, sys, traceback, platform, os
from collections import Counter
import nltk
import io, pprint
from pprint import pprint

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


    def _iter__(self):
        return self
    def _next__(self):
        if self.n <= self.max:

    def __str__(self):
       # self.f.close()
        return '{}({})'.format(type(self).__name__, ', '.join(repr(getattr(self, a)) for a in self._args))  ## guidelines for res
    def __repr__(self):
        return '{}({})'.format(type(self).__name__,', '.join(str(getattr(self, a)) for a in self._args))



    ### website_list = [x.strip() for x in content]   ####
    ### ADD LOGIC TO COUNT NUMBERS                    ####
    def text_file_len(self):
        with open(self.text_loc) as f:
            for line in open(self.text_loc):
                index = 0
                self.text_data = f.readlines(self.list_count)
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





