Matlab_intro

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

df_can.head()
df_can.head(10) # to specify 10 rows
df_can.info(verbose=False) # =True returns for every row
# #returns
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 195 entries, 0 to 194
# Columns: 43 entries, Type to 2013
# dtypes: int64(37), object(6)
# memory usage: 65.6+ KB

df_can.columns ## to get column heads.
df_can.index ## to get indexes
# output : angeIndex(start=0, stop=195, step=1)

df_can.columns.tolist() ## prints colume (or index) as a list
df_can.index.tolist()
# df_can.shape    ## determinines dimensions of DataFrame
# output: (195, 43)

# in pandas axis=0 represents rows (default) and axis=1 represents columns.

To drop columes
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

## Renaming Columns::
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

df_can['Total'] = df_can.sum(axis=1) # to create a 'total' in the database- use the .sum() call

df_can.isnull().sum() # .sum() renders a clean order. take out .sum to see individual cells

df_can.describe() # returns statistical stuff
#

############# INDEXING AND SELELECTION ###############
# ############# RETURN COLUMS ###################
df[['column 1', 'column 2']]  # returns dataframe
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
                                        # country is the index, dates are colume

########## RETURN INDEX ################
# There are two ways to seleect colums:
# Before selectiong row, it must be indexed.
# df.loc[label]    # filters by the labels of the index/colum
# df.iloc[index]   # filters by the positions of the index/column
df_can.index.name = None# optional: to remove the name of the index


df_can.set_index('Country', inplace=True)
df_can.loc['Japan'] # 1. the full row data (all columns)
#### OR -- (if the location is known)
df_can.iloc[87]


df_can[df_can.index == 'Japan'] # produces one row, with Japan and the corrosponding years
df_can.loc['Japan', 2013]

df_can.iloc[87, 36] # to pull specifici index

df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]] # 3. for years 1980 to 1985
df_can.iloc[87, [3, 4, 5, 6, 7, 8]] # Alternative Method

### Converting colume names to strings -- this helps mitigate confusion when using iloc()
df_can.columns = list(map(str, df_can.columns) # converts

print (type(x)) for x in df_can.columns.values #<-- uncomment to check type of column headers

# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years


################### FILTERING BASED ON CRITERA ##############################
## to filter a dataframe based on a condition, pass a boolean condition
# 1. creatr boolean series
condition = df_can['Continent'] == 'Asia'  ## Is 'Asia' in the colume continent?
conditition_2 = df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')] ### PASSES MULTIPLE ARGUMENTS
print(condition)
df_can[condition] ## pases the condition on to the dataframe

# ## Returns countries with true or false
# Return::
# Afghanistan        True
# Albania           False
# Algeria           False
# American Samoa    False


######################   DATA VIZUALIZATION WITH Matplotlib   ##########
# we are using the inline backend <---- backend to keep plots up to date without reprint
###### currently on script matplotlib - next is design
%matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt

print('Matplotlib version: ', mpl.__version__)  # >= 2.0.0 ## displays version of matlab


####  Plot a line graph of immigration from Hatai
# 1. create df for print the data for haiti
# 2.

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()
haiti.plot()

haiti.index = haiti.index.map(int) # changes to integer for plotting.
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show() # need this line to show the updates made to the figure


##################### TO ANNOT SPECIFIC PARTS ON A DATE ############

haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.text(2000, 6000, '2010 Earthquake') # YEARS ARE INT and '2010 Earthquake (the label on plot) is a strings
plt.show()

############## QUESTIONS FOR REVIEW ###############
#  Get the data set for China and India, and display the dataframe.
#  Then plot the graph
df_CI = df_can.loc[['India', 'China'], years]
df_CI ## returns a table
df_CI.plot(kind='line') ### plots it

df_CI = df_CI.transpose() ###### SWAPS ROWS AND COLUMS --- HELPFUL WHEN MANPULATING DATA AND
df_CI.head() # And having odd graphcs

########## PLOT THE DATAFRAME AFTER TRANSPOSING ####
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
    df_CI.plot(kind='line') ##### DF_CI was transposed and crated into a table above
    plt.title('Immigrants from China and India')
    plt.ylabel('Number of Immigrants')
    plt.xlabel('Years')

    plt.show()


############ Compare the trend of top 5 countries that contributed the most to immigration to Canada. #########

inplace = True # paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

df_top5 = df_can.head(5) # get the top 5 entries. use the .head method
df_top5 = df_top5[years].transpose() # transpose the dataframe
print(df_top5)

df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()
