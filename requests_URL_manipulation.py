import requests
import json

## SAMPLE WEBSITE https://archive.org/search.php?query=sega%20dreamcast ##



### QUERY SEARCH ###
payload = {'query': 'sega dreamcast'}
r = requests.get('https://archive.org/search.php', params=payload)
print(),print()
print(r.text) ## to receieve response 


print(),print()
print(r.headers) ## to print headers 

print(),print()
print(r.url)


print(),print()
r_dict = r.json()
print(r_dict) ## to return in .json instead of .txt








