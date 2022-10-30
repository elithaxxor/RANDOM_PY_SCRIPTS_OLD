from bs4 import BeautifulSoup #  web scrapping.
import requests  # this module helps us to download a web page


# and add search function to find all input
# will aggregate information using numpy charts

## add request from user for 'url' string.
url = "https://www.ticketmaster.com/joe-bonamassa-san-diego-california-08-03-2021/event/0A00584EBA8C51C4"
data = requests.get(url).text
soup = BeatifulSoup(data, "html5lib") # soup object using var data

# Attribute Finder #
###### NOTE - The html ID's are unique. EITHER manually search for ID and Parse, or
table_bs.find_all(id="find ID")

# Link Scrapper #
for link in soup.find_all('a', href = True) # <a> tag for HTML anchor - will return URL's
  print(link.get('href'))          #.get returns the specified key


# Image Scraper #
## Request input for specific input. Add to fund_all parater
for link in soup.find_all('img' )
  print(link)
  print(link.get('src'))


# Table Scraper #
## Request Input for data. Add to find_all paramter.
## color schema, ticket price, etc. ##

# data  = requests.get(url).text
soup = BeatifulSoup(Data, "html5lib")

# scrape for table
table = soup.find('table') # HTML tag

for row in table.find_all('tr'): # HTML Tag - Table Row
  #fetch columns in the row
  column = row.find_all('td') # HTML Tag - Table Column

#  ********** store values in matrx, print to screen ***** #
# ********************************************************* #
  color_name = column[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
