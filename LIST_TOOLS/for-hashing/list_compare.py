import os, sys 

code = '''
count = 0
thefile = open(thefilepath, 'rb')
while 1:
    buffer = thefile.read(8192*1024)
    if not buffer: break
    count += buffer.count('\n')
thefile.close(  )
'''

## the list counter will work well on Windows and Linux for .txt, line replace 18 and 22 with the code below
print('X' * 50, '\n**The list counter will work well on Windows and Linux for .txt, line replace 18 and 22 with the code below  ')
print(code), print()

with open('list.txt', 'r') as f:
    count_1 = len(open('list.txt').readlines()) # REMOVE THIS IF IT IS STRING-BOUND .TXT
    list_1 = f.readlines()

with open('list2.txt', 'r') as f:
    count_2 = len(open('list2.txt').readlines())
    list_2 = f.readlines()

res = [x for x in list_1 + list_2 if x not in list_1 or x not in list_2]
print('list one count: ', count_1 )
print('list two count: ', count_2 )
print(res)
if not res: print("Lists 1 and list 3 are equal")
else: print("Lists l1 and l3 are not equal")


print('X' * 50)

print(res)

