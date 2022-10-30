import os, sys, tqdm


def scanDirs():
    print("Files and Directories in '% s':" )
    # glob.isglob to find all files recursivly
   # file_locs = []
   # file_list = []
    file_locs = {"Root": [], "File": []}
    file_list={'Files': []}
    p = os.getcwd()
    file_counter = 0
    ## try both isfile() and exists ##
    for root, dirs, files in os.walk(p, followlinks=True):
        # print(root)
        # print(dirs)
        # print(files)
        print('X'*50)
        print(str(root))
        print('X'*50)

        file_locs['Root'].append(root)
        file_locs['File'].append(files)
        file_list['Files'].append(files)
        file_counter+=1

        if dirs:
            pass
            #print(files)
            #file_list.append(str(root) + str(dirs) + str(files) + ('\n'))
           # file_locs.append(str(root) + str(dirs) + str(files))
        return file_counter, file_locs, file_list



count, file_locations, listof_Files = scanDirs()
print('X'*50)
print('Count', count)
print(file_locations)
print('X'*50)
print(file_locations.keys())
for key, val in file_locations.items():
    count = int(0)
    file_locations['Root'][0] = str(file_locations['Root'][0])
    file_locations['File'][count] = str(file_locations['File'][count])

    print(file_locations['File'][count])
    #print(file_locations['Root'][0] + file_locations['File'][count])
    count+=1

