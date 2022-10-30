import os
import os.path
from pathlib import Path
import time
from datetime import date
import traceback, sys

'''
1. prelimnary scan 
2. deeper scan, write file to txtr
3. take .txt and hash filepatths
4. use algo below to compare .txt lines 
5. 
'''
## finding duplicates within a set
with open('file') as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line)
        else:
            seen.add(line_lower)



try:
    print(f'Current Working Directory: {path00}'.center(width))
    print(), print()
    print(f'[SYS] Current Directory Listing\n {os.listdir(path00)}'.center(width))
    print(), print()
    print(os.scandir(path00))

    for x in os.scandir():
    for x in os.scandir():
        print(x)

    p = Path(path_input)
    os.chdir(p)
    print(p.parent)

    print(f'[SYS] [PRELIM DIR-SCAN]\n {os.listdir(path00)} +"\n"'.center(width))
    print(f'[SYS] [PRELIM INDEPTH DIR-SCAN] \n {os.scandir(path00)} +"\n"'.center(width))
    print(f'Changed working directory:  {path00}'.center(width))
    print(), print()


    ## preliminary test before hashing.
    def checkIfDuplicates_2():
        start = time.ctime()
        print(f'[+] Prelinary Duplicate Scan for Approximations. [+]')
        with open('duplicate_firstRun.txt', 'a') as f:
            dir_list = os.listdir(path00)
            f.writelines(os.listdir(path00))
            ticker = 0
            dirSet = set(dir_list)
            with open('duplicate_secondRun.txt', 'r') as f:
                listOfElems = f.readlines()
                for elem in listOfElems:
                    if elem in dirSet:
                        print(f'Duplicate Found :: writing to .txt :: [{elem}] ')
                        ticker+=1
                        return True
                    else:
                        ticker+=1
                        dirSet.add(elem)
                print()
                return False


    with open('file') as f:
        seen = set()
        for line in f:
            line_lower = line.lower()
            if line_lower in seen:
                print(line)
            else:
                seen.add(line_lower)

    counter = 0
    part_path = [] ## add partial chunk, use condition to check the end
    print(list(p.glob('**/**.py')))
    p = Path(os.getcwd())
    print(p.resolve(x))

    print(), print()
    if os.path.exists:
        for x in os.listdir():
            print(f"{x}".center(width))
            print(f'The Directory Split as Tuple: '.center(width))
            print(f"{'*' * 50}".center(width))
            print(), print()
            for f in path.iterdir():
                meta_str = f'{f}:StreamName'
                meta = open('myfile.ext:StreamName').read()

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


    for y in os.iterdir():
        print(y)
    dir_files = []
    dir_len = len(os.listdir(path00))
    data_txt = f'file_list+{date.today}_{time.ctime}'
    counter = 0
    for x in os.walk():
        if x in os.walk():
            dir_files.append(x)
            dir_files.append('\n')
            counter+=1
            with open(data_txt, 'a') as f:
                f.write(''.join(str(x)) + path00+ '\n')
        print(f'[Content is stored in memory and on harddisk. \n [TXT-LOC] {path00} {data_txt} (]')
        print(f'[!] EOF.. sys.exit')
        print()
        sys.exit(1)

## chunking the file path
if os.path.exists:
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

#check if files share simular names
# check if chuck in ban list
# if simalr file and banned, remove

for x in os.walk(path, followlinks=True):
    print(path+x)




for x in os.listdir(path00):
    full_path = str(path00) + x
    name_chunks = full_path.split(_)
    ## set up for comparrason
    old_path = new_part[0] + new_part[1] + ip_part[-2] + str(x)
    new_path = new_part[0] + new_part[1] + ip_part[-2] + str(x)
    print(ip_part[0] + ip_part[1] + ip_part[-2] + str(x))
    txt = 'path_info.txt'
    new_filenames = str(date.today()) + str(time.ctime()) + str(txt)
    with open(new_filenames, 'a') as f:
        f.write(f'{NEW_IP} \n')
    print(f'[+] Generation Complete, file info has been saved: \n [FILENAME] [{new_path}.txt')




    print(os.scandir(path00))
    for x in os.scandir():
        print(x)
    for y in os.listdir():
        print(y)
    print(os.scandir(path00))
    dir_files = []
    files = ''
    dir_len = len(os.listdir(path00))
    data_txt = f'file_list+{date.today}_{time.ctime}'
    counter = 0


   # writes files for hashing later
    print(f'[+]** Sys found [{dir_len}] items in CWD')
    for x in os.listdir():
        full_path = str(path00) + x
        if x in os.listdir():
            print(os.stat(full_path))
            dir_files.append(full_path)
            dir_files.append('\n')
            counter+=1
            with open(file_data.txt, 'a') as f:
                f.write(''.join(str(full_path)) + '\n')
            with open(file_stat.txt, 'a')
                f.writelines(os.stat(full_path))
        if counter == int(dir_len):
            print(f'[Content is stored in memory and on harddisk. \n [TXT-LOC] {path00} {data_txt} (]')
            print(f'[!] EOF.. sys.exit')
            print(dir_files)
            sys.exit(1)






path00=str(path00)
[x for x in p.iterdir() if os.path.isfile(str(path00)+str(x).is_file())]
print(x)

print(), print()


print(type(path00))
print(path00)
p = Path()
p.resolve()


#with open
# for x in p.iterdir(path):
#     print(x)

print(list(p.glob('**/**.py')))

counter = 0
print(), print()
