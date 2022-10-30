import os, traceback, time
import cv2
import numpy as np
import xml.etree.ElementTree as ET

path = '/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/mydata'
textList = os.listdir(r"/Users/adelal-aali/Documents/CS/PROJECT/IP_CHECK/mydata")
textLen = len(textList)
print(f'[+] Found [{textLen}] files in: \n[+]* \n [{path}]\n[{textList}]')
files = []
#### CREATE FOLDERS WITH KEY VALUES #####
### loading videos / images for video parser
myList = os.listdir(path);
noOfClasses = len(myList)
print(f'[+]** FOUND [{noOfClasses}] Items')
AV = []; classNo = []
class_count=0
print(f'[+]* Importing Classes ')
try:
    for x in range(0, (noOfClasses - 1)):
        #   file_list = os.mkdir(path+"/"+str(x)) ## change
        myPicList = os.listdir(path)  ## store in list
        print('[+] List of Item in Dir:\n ', myPicList)
        class_count+=1

        for pics in myPicList:
            pic = myPicList[class_count]
            print(f'\nProcessing : [{pic}] ')
            current_image_path = path + '/' + pic
            curImg = cv2.imread(current_image_path)
            AV00 = np.array(AV00)
            classNo00 = np.array(classNo00)
            print('[+] AV Shape: ', AV00.shape); print('[+] ClassNo Shape ', classNo00.shape)
            # curImg = curImg ## ADD LOGIC FOR MANIP LATER
            AV.append(curImg)  ## append imge
            classNo.append(x)  ### append key values
        print(x, sep='[+] ', end='')

    time.sleep(.001), print()
    AV = np.array(AV)
    classNo = np.array(classNo)
    print('[+] AV Shape: ', AV.shape); print('[+] ClassNo Shape ', classNo.shape)
except Exception as err:
    errname = type(err).__name__
    print(f'[+] Error Detected: -- [{errname}] \n [{err}]\n[{traceback.print_exc()}]')
    if (errname == 'OSError') and (errnum == errno.ENAMETOOLONG):
        print(f'[-] Error List Name Too Long')



try:
    folder_count = 0
    for folders in range(0, textLen):
        file_list = os.mkdir(path + "/" + str(folders))  ## change
        file_keys = os.listdir(path + "/" + str(folders))  ## store in list
        folder_count += 1
        for y in file_keys:
            # print(y)
            files.append(y)
        file_list_len = len(files)
        print(folders, sep='key # ', end=''), print()
    numFolders = len(files)
    print(f"\n[+] Sys Created : [{folder_count}] Folders\n")
except Exception as err:
    errname = type(err).__name__
    # errnum = err.errno
    print(f'[+] Error Detected: -- [{errname}] \n [{err}]\n[{traceback.print_exc()}]')
    if (errname == 'OSError') and (errnum == errno.ENAMETOOLONG):
        print(f'[-] Error List Name Too Long')
