import os
import os.path
from pathlib import Path
import time

start_time = time.time()
print(start_time)
print(os.get_terminal_size())  # returns the terminals size
print(os.name)
width = os.get_terminal_size().columns  # set the width to center goods
width_len = width
cwd = os.getcwd()
print(cwd)
print()


print(f' ----File Extension Change---- '.center(width))
path00 = input(str(f"This is your current working directory, copy it if the files are in here, otherwise enter the directory to work in: \n{cwd}\n "))
print()
# Initilize Path (do not use os.)
path = Path(path00)
print(path)
print(path.parent)
print(path)
print(path.is_file())


## Set params for old file:
old_ext = input('[SYS] Enter the file extension, leave blank if none. \n')
print(), print()
new_ext = input('[SYS] Enter the new file extension, leave blank if none. \n')
print(f'[SYS] Commencing File Processing.. [SYS]'.center(width))
os.chdir(path00)

print(f'Current Working Directory: {path00}'.center(width))
print(), print()
print(f'[SYS] Current Directory Listing\n {os.listdir(path00)}'.center(width))
print(), print()

counter = 0
print(), print()
if os.path.exists:
    try:
        for x in os.listdir():
            print(f"{x}".center(width))
            print(f'The Directory Split as Tuple: '.center(width))
            print(f"{'*' * 50}".center(width))
            print(), print()

            for f in path.iterdir():
                print(f'{f}'.center(width))
                directory = f.parent
                extension = f.suffix
                old_file = f
                old_name = f.stem
                print('FILE PARAMATERS'.center(width))
                print('Old File: ', old_file)
                print('Old Name: ', old_name)
                print('Directory: ', directory)
                print('Extension: ', extension)

                if extension == old_ext:
                    print('Found Matching Extension'.center(width))
                    print('xxxxxxxxxxxxxx'.center(width))
                    print('this is the new path', path)

                    file_name = old_name.split('.')
                    print(file_name)
                    print(type(file_name))

                    new_name = old_name + new_ext

                    f.rename(Path(directory, new_name))
                    print('renaming files')
                    counter += 1

                else:
                    end_time = time.time()
                    time_to_complete = end_time - start_time
                    print('[SYS] FILE EXTENSIONS HAVE BEEN CONVERTED [SYS] '.center(width))
                    print(f'[SYS] Time to complete: {time_to_complete}')
                    pass

    except Exception as e:
        print(str(e))

else:
    print('[SYS] PATH DOES NOT EXIST [SYS] '.center(width))






# print(f'[SYS Parsing Info'.center(width))
# print(f' Completed {counter} iterations in in {time_to_complete} \ and changed {old_ext} to {new_ext}')


# print(file_name), print(file_ext)
# file_name, file_ext = os.path.splitext(f)              # print(os.path.splitext(f)) ## gives list in tuple form            #file_name = str(file_name)
#             ### USE THIS TO CLEAN UP THE FILE ##
