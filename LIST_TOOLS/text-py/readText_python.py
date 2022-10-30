import os


print(f'.TXT SCANNER --> progfram')
website_list = []
count = 0
hrefdata = 'hrefdata.txt'
cwd = os.getcwd()
href_loc = str(cwd) + f'/{hrefdata}'
href_str = f'[SYSTEM]** Dump The Text Data To: [{href_loc}] ** [SYSTEM]'
print(href_str)

with open(href_loc) as f:
	for href in open(href_loc):
		website_list = f.readlines(count)
		index = 0
		count += 1
		for iterate in website_list:
			if index < count:
				print(f'[SYS]** ADDED {iterate}')
			else:
				break
		print(f'[SYSTEM] Found {count} items in .txt')
		break


print('Scanned List from .txt')
