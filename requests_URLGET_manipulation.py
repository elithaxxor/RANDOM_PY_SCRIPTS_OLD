import requests


## SAMPLE WEBSITE https://archive.org/search.php?query=sega%20dreamcast ##


payload = {'query': 'sega dreamcast'}
r = requests.get('https://archive.org/search.php', params=payload)
print(r.text) ## to receieve response 
print(r.headers) 
print(r.url)



