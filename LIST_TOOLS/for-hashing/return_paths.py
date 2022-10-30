import os, sys, tqdm

def scanDirs():
    print("Files and Directories in '% s':" )
    file_list = []
    file_locs = {"Root": [], "File": []}
    file_dict={'Files': []}
    p = os.getcwd()
    dir_length = len(os.listdir(p))
    file_counter = 0
    for root, dirs, files in os.walk(p, followlinks=True):
        print('X'*50)
        print(str(root))
        print('X'*50)
        file_locs['Root'].append(root)
        file_locs['File'].append(files)
        file_dict['Files'].append(files)
        file_list.append(files)
        file_counter+=1
        path = p
        if os.path.isdir(path):
            print('Passing on subdirs')
            pass
        return dir_length, file_locs, file_dict, file_list


def runScan():
    dir_len, file_locations, dictof_Files, listof_Files, = scanDirs()
    print('List Keys')
    for x in file_locations.keys():
        print(x)
    for y in dictof_Files.keys():
        print(y)

    print('Total files in dir: ', dir_len)
    print(listof_Files[0][0])
    counter = 0
    while counter <= dir_len:
        for count, root in file_locations.items():
            print(root)
            file_locations['Root'][0] = str(file_locations['Root'][0])
            print('x'*50)
            print(file_locations['Root'][0])
            for countin, files in dictof_Files.items():
                file_name_list = (dictof_Files["Files"][0])
                print('x'*50)
                file_name = file_name_list[counter]
                file_pathTo_hash =  str(file_locations['Root'][0]) + "/" + str(file_name)
                print(file_name)
                print(type(file_name))
                print(file_pathTo_hash)
                with open('hash_links.txt', 'a') as f:
                    f.write(file_pathTo_hash + '\n')
                counter += 1

if __name__ == '__main__':
    runScan()

