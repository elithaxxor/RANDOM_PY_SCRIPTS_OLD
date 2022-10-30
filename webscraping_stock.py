import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import yfinance as yf

use read_html to parse html tables to pandas
dataframe_list = pd.read_html(url, flavor='bs4')


## using read to parse HTML table and creating custom columes.
#print(soup.find_all("tbody"))[1]
tesla_revenue = pd.read_html(str(tables[5]), flavor='bs4')[1]



pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
tesla_revenue = pd.DataFrame(columns= {'date', 'revenue'})
tesla_revenue = pd.read_html(url)[1]
tesla_revenue

###############################################
### prints as bs4 element
gme_revenue = soup.find_all('tbody')[1]
print(type(gme_revenue))
#print(gme_revenue)

### prints as list to iterate
gme_revenue2= pd.read_html(url) # trey prettify too
print(type(gme_revenue2))


# extract data using get() method
#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
url = "https://finance.yahoo.com/quote/TSLA/key-statistics?p=TSLA"
html_data  = requests.get(url).text

# parse text into soup. set method BeatifulSoup to soup
##### use this to BEATIFULSOUP through webpage, store them to .CSV
soup= bs(html_data, 'html.parser') ### may have to changehtml

#################################

company = 'AAPL'
statistics = pd.read_html(f'https://finance.yahoo.com/quote/{company}/key-statistics?p={company}')
print (statistics)
################################################

# tag attributes
# Tag.name        #name the name of your tag
# Tag.attrs   # dictionary of key:value Attribute
# Tag.tagname # th enext tag ofbect of specified tag
# Tag.contents    # a list of children element sof the Tag
# Tag.text    # a string of all text content inside a tag
# Tag.findParent  # parent tag of this tag
# Tag.parent  # next sibling tag of this tag
# Tag.next_siling # previous sibling tag of this tag
# Tag.next_element    # next sinbling eleemnt of tag
# Tag.previous_element # previous sibling element of tag
#

# generator tag - to set up a loop to iterate ( for)
#### ----- ARE PLURAL -------- ###
# # Tag.children - children of the tag
# Tag.descendents - children and childrens children - used to go deep
# Tag.strings - string content of the tag (href links)
# Tag.stripped_strings - string content, with white space removed
#
# Tag.parents # parent and parents parent - goes up from being deep
# Tag.next_siblings - all next available siblings of the tag
# Tag.previous_siblings Tag.previous_siblings
# Tag.next_elements Tag.next_elements
# Tag.previous_elements tag.previous_elements



############################################################################

print (soup.body.prettify) # represents first tag for p - replace it with any HTML Tag
#print (soup.p.prettify)


# #print the dataframe:
# soup_title = soup.name
# soup_head = soup.head
# print(soup_title)
# print(soup_head)
#
 #list any href links
for link in soup.find_all('a', href = True): # <a> tag for HTML anchor - will return URL's
    x = link.get('href')        #.get returns the specified key
    print(x)


#
# tsla_revenue = soup.find_all('div', class_='D(ID)')
# for i in soup.find_all('div', class_='D(ID)'):
#     x = i.get('div')
#     print (x)
#
#

#
#
# # scroll through html and move to pandas dataframe use pd.DataFrame method
#
print('\n' * 10)
t_body = soup.find('tbody')
print(t_body)
print('\n' * 3)
print(type(t_body))

print(type(t_body.text))



# ## Html table into pandas dataframe
# table_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"]) # declare dict here for table.
#
# print(table_data)
#
# for row in soup.find("tbody").find_all('tr'): # Isolate body - use tbody (Html) to find table bodY.
#     col = row.find_all("td") #html for data cell <td> cell a </td>
#     date = col[0].text      # write to  corosponding tables
#     Open = col[1].text      # .text returns chld strings.
#     high = col[2].text      # replce with .string to clean up (no child string)
#     low = col[3].text
#     adj_close = col[4].text
#     volume = col[5].text
#
# ## pandas time - create dictionary, then append ^
#     table_data = table_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":adj_close, "Volume":volume}, ignore_index=True)
#         #for x in range(len(table_data)):  ## <---- insert data manip down the line
#
# print(table_data.head())
#
#
####
simple feature scaling python (data normalization)
df["col_1"] = df['col_1']/df["col_1"].max()

###
max-min (data normalization)
df["length'] = (df["length"]-def["length"].min())/
                (df["length"].max()-df["length"].min())

df["length"] = (df["length"]-df["length"].mean()) / df["length"].std()


###
data binning

#low - medium - high (binning)
#linspace - returns evenly spaced numebrs over specifed interval
bins = np.linspace(min(df["price]),max(df;"["price"]),4)
group_names = ["low", "Medium", "high"]
df["price-binned"] = pd.cut(df["price"], bins, labels = group_names, include_lowest=True)

###
categorical to dummy variables (written variable to binary)
pd.get_dummies(df['fueld'])


filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)
df.head()

df = pd.read_csv(filename, names = headers)


##
# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

# evaluating for missing data
## true = missing, false = not missing

missing_data = df.isnull()
missing_data.head(5)

# Count missing values in each column
## this calclulates the # of missing columens in a data set

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts()) ## counts the umber of true values
    print("")


# to calculate the mean value for the "normalized losses" column
## .astype foces pandas to cast as a type- float
## axis 0 = row 1 = column

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

# dummy variables
## used to convert categorical variables to regular
# list to check data type
df.dtypes # to check data types
.astype() to change datatype.

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


#######################
## Data standardization  - tranfomring numercal varibaels into discreete categorcal bins
## transforming data into a common format, so researchers can make comparassons
# Convert mpg to L/100km by mathematical operation (235 divided by mpg)

df['city-L/100km'] = 235/df["city-mpg"]  ## apply equation to colume
df.head()

######################
## Data Normalization
## transfomring values of seval variabels int a single range.
## normalizes
# replace (original value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


####################
## binning
## tranfomring numerical varibles into discreet siblings

## convert data to correct format
df["horsepower"]=df["horsepower"].astype(int, copy=True)

%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins

## to create bin columns
group_names = ['Low', 'Medium', 'High']

## to create bin array
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)
df["horsepower-binned"].value_counts()


## plot the distribution of each bin
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"]

plt.pyplot.xlabel("horsepower) # sets x label
plt.pyplot.ylabel("count") # sets y label
plt.pyplot.title("horsepower bins")

## to plot 3 bins of equal size - use the following structure:
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins

group_names = ['Low', 'Medium', 'High'] # set group names
                                        # apply cut to splice table
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

## bins visualizualization
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

##################################
dummy variable - use to convert categoraical data to numebracl database- best used for regression analasys
## change the columne names
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
dummy_variable_1.head()

dummy_variable_1 = pd.get_dummies(df["fuel-type"]) ## grab colume fuel - types
df = pd.concat([df, dummy_variable_1], axis=1) # merge data frame "df" and "dummy_variable_1"
df.drop("fuel-type", axis = 1, inplace=True) # drop original colume from data DataFrame










##########################################
make_graph(tesla_data, tesla_revenue, 'Tesla')
#
make_graph(tesla_data, tesla_revenue, 'Tesla')
df.describe (include = 'all')
#NAN  = not a number

tesla_revenue.describe(include ='all')
tesla_revenue.info() # top and bottom 30 rows
Use dataframes.dropna:
Use dataframe.replace(missing value, new value)

f[["price"]] = df[["price"]].astype("float"] # cast data frame to new type

# show the first 5 rows using dataframe.head() method

##  applying calculations to an entire columns
df["column_name"]= 235/df["colume_name"] # cre calculates colume with equation

# to identify data types
use dataframe.dtypes()


#For example, if you would save the dataframe df as automobile.csv to your local machine, you may use the syntax below,
#where index = False means the row names will not be written.
print("The first 5 rows of the dataframe")
df.head(5)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
df.head(5)

path="https://archive.ics.uci.edu/ml/machine-learning-database/autos/imports-85.data"
df = read_csv(path,header=None) # <-- assuming there are no header colums

path = 'C:/'
df.to_csv(path) #change csv to json excel or sql

dataframe.describe(tesla_data)
df.dropna(subset = [''], axis = 0, inplace = True) # axis = 0 is for frow. inplace = True initiates the change
database.info( _)
## read_html - takes HTML and makes it into PANDSAS DATAFRAME

#### ********************************************************** ###
#### NEED TO SET UP SSH/SSL VERIFICATION TOKEN FOR THIS TO WORK ###
# pandas read_htm function #
#********* impliment below****
pandas_data_matrix = pd.read_html(url) ## creates a table using .read_html, to read from URL, file or string.
pandas_data_print = pandas_data_matrix[0]                                     ##  change the paramaters // see panda documentation
type(pandas_data_print)
pandas_data_print                   ## for debugging - should be a list.
pandas_data_print[0]                       ##  access first element, will make iterable as program expands
pandas_data_print.head()                   ## returns 'n' rows - default, 5
