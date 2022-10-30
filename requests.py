import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import yfinance as yf


# extract data using get() method
#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
url = "https://finance.yahoo.com/quote/TSLA/key-statistics?p=TSLA"
html_data  = requests.get(url).text

# parse text into soup. set method BeatifulSoup to soup
##### use this to BEATIFULSOUP through webpage, store them to .CSV
soup= bs(html_data, 'html.parser') ### may have to changehtml


print(type(html_data))
print(html_data)
