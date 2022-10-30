!pip3 install beautifulsoup4
!pip3 install requests



import sys
import requests
from bs4 import BeautifulSoup as bs
import re
import unicodedata
import pandas as pd



def date_time(table_cells):
    """
    This function returns the data and time from the HTML  table cell
    Input: the  element of a table data cell extracts extra row
    """
    return [data_time.strip() for data_time in list(table_cells.strings)][0:2]

def booster_version(table_cells):
    """
    This function returns the booster version from the HTML  table cell
    Input: the  element of a table data cell extracts extra row
    """
    out=''.join([booster_version for i,booster_version in enumerate( table_cells.strings) if i%2==0][0:-1])
    return out

def landing_status(table_cells):
    """
    This function returns the landing status from the HTML table cell
    Input: the  element of a table data cell extracts extra row
    """
    out=[i for i in table_cells.strings][0]
    return out


def get_mass(table_cells):
    mass=unicodedata.normalize("NFKD", table_cells.text).strip()
    if mass:
        mass.find("kg")
        new_mass=mass[0:mass.find("kg")+2]
    else:
        new_mass=0
    return new_mass



    # use requests.get() method with the provided static_url
    # assign the response to a object
static_url = "https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922%22"
html_data  = requests.get(static_url).text

soup = bs(html_data, 'html.parser')

print(soup.title)

html_tables = soup.find_all('table')
print(html_tables)

first_launch_table = html_tables[2]
print(type(first_launch_table))
print(first_launch_table)


column_names = []


# def extract_column_from_header(row):
def extract_column_from_header(row):
    """
    This function returns the landing status from the HTML table cell
    Input: the  element of a table data cell extracts extra row
    """
    if (row.br):
        row.br.extract()
    if row.a:
        row.a.extract()
    if row.sup:
        row.sup.extract()

    colunm_name = ' '.join(row.contents)

    # Filter the digit and empty names
    if not(colunm_name.strip().isdigit()):
        colunm_name = colunm_name.strip()
        return colunm_name

        if(len(cells) > 0):
        postalCodeList.append(cells[0].text)
        boroughList.append(cells[1].text)
        neighborhoodList.append(cells[2].text.rstrip('\n'))


#column_name = soup.find_all()
first_launch_table = html_tables[2]


for row in soup.find(first_launch_table).find_all('th'): #or change to th
    
    extract_column_from_header(row)
    print(row)
    #cells = extract_column_from_header('row')
