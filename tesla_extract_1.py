import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import yfinance as yf

### Documentation Reference ##

gme_data.reset_index(inplace=True) -- reset index 

# creates object tsla
tsla = yf.Ticker("TSLA")

tesla_info = tsla.info
print(tsla)
print(tsla.info.keys()) ## returns keys
print("\n" * 2)
print(type(tesla_info))
print("\n" * 3)

print(tesla_info['totalRevenue'])  # enter whats here to return key value

print("\n" * 5)

tesla_financials = tsla.financials
print(tsla.financials.keys()) ## returns keys
print("\n" * 2)

print (tesla_financials)
print("\n" * 2)

print(type(tesla_financials))
print("\n" * 10)

#####
#Question 2 - Extracting Tesla Revenue Data Using Webscraping - 1 Points

# extract data using get() method
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data  = requests.get(url).text
soup= bs(html_data, 'html.parser') ### saves as a beatifulsop fil eneed to make array

print(soup.find("tbody"))
print(type(soup.find.prettify("tbody"))

### iterate through object soup.find(tbody)
### create an array

print(tsla.history)


tesla_data = tsla.history(period='max')
print(tesla_data)

print(type(tesla_data))




soup_table = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"]) # declare dict here for table.

for row in soup.find('tbody').find_all('tr'):
    col = row.find_all("td") #html for data cell <td> cell a </td>
    date = col[0].text      # write to  corosponding tables
    Open = col[1].text      # .text returns chld strings.
    high = col[2].text      # replce with .string to clean up (no child string)
    low = col[3].text
    adj_close = col[4].text
    volume = col[5].text
    soup_table = soup_table.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":adj_close, "Volume":volume}, ignore_index=True)

print(soup_table.head())

#tesla_revenue = pd.read_html('https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue')   #, flavor='bs4')[1]
#print(tesla_revenue)

to replace and move strings around
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
print(tesla_revenue)
print(tesla_revenue.tail(5))

#print(soup)
#soup_array = soup
#print(type(soup_array)
#print(type(soup))








####
#table_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
#tesla_revenue_chart = pd.DataFrame([])

#tesla_revenue = tesla_revenue_.get([2])
#print(tesla_revenue)

#for revenue in tesla_financials.get('')


#for link in soup.find_all('a', href = True): # <a> tag for HTML anchor - will return URL's
    #print(link.get('href'))           #.get returns the specified key




# Question 3 - Extracting GameStop Stock Data Using yfinance - 2 Points

#GameStop = yf.Ticker("GME")
