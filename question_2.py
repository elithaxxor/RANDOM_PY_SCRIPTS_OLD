import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import yfinance as yf

#Question 2 - Extracting Tesla Revenue Data Using Webscraping - 1 Points

# extract data using get() method
url = "https://finance.yahoo.com/quote/TSLA/key-statistics?p=TSLA"
html_data  = requests.get(url).text
soup= bs(html_data, 'lxml') ### or html5lib



print (soup.findAll('title'))
## Html table into pandas dataframe
#table_data = pd.DataFrame(columns=["Breakdown", "Current",]) # declare dict here for table.

#print(table_data)

# print(soup.findAll('html'))

print('\n' * 10)
#find first direct child
soup.find("li", { "class" : "test" }).find("a", recursive=False)
#soup.find("li", { "class" : "test" }).find('a')


#li = soup.find("li", { "class" : "test" })
children = li.find_all("a") # returns a list of all <a> children of li

#
# #li = soup.find('li', {'class': 'text'})
# #for child in li.children:
# #    print(child)
#
# #tables = soup.findAll("title")
# #for table in tables:
#      if table.findParent("table") is None:
#          print(table.findParent)
#


#print(tables)
#or row in soup.find("tbody").find_all('tr'): # Isolate body - use tbody (Html) to find table bodY.
#    breakdown = col[0].text #html for data cell <td> cell a </td>
#    # Open = col[1].text      # .text returns chld strings.
                       # replce with .string to clean up (no child string)

## pandas time - create dictionary, then append ^
#    table_data = table_data.append({"Breakdown":breakdown, "TTM":ttm}, ignore_index=True)
        #for x in range(len(table_data)):  ## <---- insert data manip down the line

#print(table_data.head())


# 12/31/2020 12/31/2019 12/31/2018 12/31/2017
