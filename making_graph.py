import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


#### coorelateion ###
## P -VALUE - The p-value is the probabilty value that the correlation between
# ## two variobales is statistically sagnaiicant
# p-value is  <
# <
#   0.001: we say there is strong evidence that the correlation is significant.
# the p-value is  <
# <
#   0.05: there is moderate evidence that the correlation is significant.
# the p-value is  <
# <
#   0.1: there is weak evidence that the correlation is significant.
# the p-value is  >
# >
#   0.1: there is no evidence that the correlation is significant.

path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/House_Sales_in_King_Count_USA.ipynb'
.
df.head()

# list the data types for each column
print(df.dtypes)

## to calculatoe the correlation between varioabbles int and float2
df.corr()
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()





## linear relationships ##
# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)


## using .corr() to find  any othe feathr most coreelated to price, other than prices
df.corr()['price'].sort_values()


## To find the coorelation of two colums
df[["engine-size", "price"]].corr()
df[["stroke","price"]].corr()


###################
# Cateogrical Variables
## box plots are great for categorical Variables
# the count of that variable
# the mean
# the standard deviation (std)
# the minimum value
# the IQR (Interquartile Range: 25%, 50% and 75%)
# the maximum value

sns.boxplot(x="body-style", y="price", data=df)

df['drive-wheels'].unique() ## returns what the colume is.
df.describe()
## by default - df describe does not include objects. you must specificy it.
df.describe(include=['object'])

## value count
## tells you how many units of each charitceris are in a value. cannot use double bracket
## see dataframe vs series
df['drive-wheels'].value_counts()
# conver thte series to a dataframe
df['drive-wheels'].value_counts().to_frame()
## renaming the index#

###
#This assigns variable to dataframe and renames columes
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
#rename the colume
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts

# Rename the index

drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

## same thing as ^^
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)

##########################################
##### GROUPING #####
#Groupby method grups data by differnt cateogires for futher analaysis.

## select colums of tabnle and assign to a group.
df['drive-wheels'].unique() ## to display what the colume is
df_group_one = df[['drive-wheels','body-style','price']] ## using the values found from above

# grouping results -- Calulcate the average result for each of the group coulums
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
df_group_one



# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1

### Grouping results
# 	drive-wheels	price
# 0	4wd	10241.000000
# 1	fwd	9244.779661
# 2	rwd	19757.613333
#

# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1

### groupiong with multiple coulums
# grouping results
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_test1
# Results
# drive-wheels	body-style	price
# 0	4wd	hatchback	7603.000000
# 1	4wd	sedan	12647.333333
# 2	4wd	wagon	9095.750000
# 3	fwd	convertible	11595.000000
# 4	fwd	hardtop	8249.000000
# 5	fwd	hatchback	8396.387755
# 6	fwd	sedan	9811.800000
# 7	fwd	wagon	9997.333333
# 8	rwd	convertible	23949.600000
# 9	rwd	hardtop	24202.714286
# 10	rwd	hatchback	14337.777778
# 11	rwd	sedan	21711.833333
# 12	rwd	wagon	16994.2222

####### PIVOT TABLES #####
# pivot tables are simalr to exccell spreads sheets,
# convert dataframes to pivtetables witwh .pivot(index, columes)
rouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
grouped_pivot
##### OUtput
# body-style	convertible	hardtop	hatchback	sedan	wagon
# drive-wheels
# 4wd	NaN	NaN	7603.000000	12647.333333	9095.750000
# fwd	11595.0	8249.000000	8396.387755	9811.800000	9997.333333
# rwd	23949.6	24202.714286	14337.777778	21711.833333	16994.222222


## Use the "groupby" function to find the average "price" of each car based on "body-style".
## using group by and pyplot
import matplotlib.pyplot as plt
%matplotlib inline

df_gptest2 = df[['body-style','price']]
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean()
grouped_test_bodystyle
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
grouped_pivot
##### Using a heatmap to vizualise gruped results::
#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
#

# The heatmap plots the target variable (price) proportional to colour with respect to the variables 'drive-wheel'
#  and 'body-style' on the vertical and horizontal axis, respectively. This allows us to visualize how the price
#   is related to 'drive-wheel' and 'body-style'.

###### SETTING UP A HEATMAP ##########
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')
#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index
#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)
#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)
#rotate label if too long
plt.xticks(rotation=90)
fig.colorbar(im)
plt.show()



########## COORELATIN AND P-VALUES
### TO CALCULATE P-VALUE
## Coorelation value requeres to columes to compare

From scipy import stats
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef,
" with a P-value of P =", p_value)
##
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value )


########## AANOVOA #######
## Anova - analays sofVariance
#F-test score - calculates a baseline and then how far the means of each deviate from baseline
#p-value - tests for statistical signicicance. strong variablility is high F-score low p-score

## first group the data
## grouped_test2 = is drive-wheels and price; and they are sorted by drive wheels
grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)


get_group() ## constructs data from a gorup
grouped_test2.get_group('4wd')['price']


# ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'],
grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])

print( "ANOVA results: F=", f_val, ", P =", p_val)

# #### results:
# ANOVA results: F= 130.5533160959111 , P = 2.2355306355677845e-23
# Let's examine the other groups.
#
