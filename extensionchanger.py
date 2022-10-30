import os
import time


print(os.get_terminal_size())  # returns the terminals size
width = os.get_terminal_size().columns  # set the width to center goods
width_len = width



cwd = os.getcwd()
path00 = input(f'This is your current working directory, copy it if the files are in here, otherwise enter the directory to work in: \n{cwd}')

old_ext = input('[SYS] Enter the file extension, leave blank if none.' )
new_ext = input('[SYS] Enter the new file extension, leave blank if none.' )
start_time = time.time()
print(f'[SYS] Commencing File Processing.. [SYS]'.center(width))

counter = 0
with os.scandir(str(path00)) as files:
    for file00 in files:
        if file00.is_file():
            cwd, ext = os.path.splittext(element.path)
            if ext == old_ext:
                new_path = cwd + new_ext

                os.rename(element.path, new_path)

                end_time = time.time()
                time_to_complete = end_time - start_time

                counter += 1

print(f'[SYS Parsing Info'.center(width))
print(f' Completed {counter} iterations in in {time_to_complete} \ and changed {old_ext} to {new_ext}')










