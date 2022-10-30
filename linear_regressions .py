# simple linear regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# path of data
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

# create linear regression object
lm = LinearRegression()

### pretict help us predict how highway mpg can help us precit car prices
# create linear function
x=df[['highway-mpg']] # predictor value
Y = df['price'] # dependant variable

# fits the linear model using high-mpg
##
lm.fit(X,Y) #.fit trans the model

Yhat=lm.predict(X)
Yhat[0:5]

## to find the value of intercept a
lm.intercept_

## to find value of slope
lm.coef_


###### multi linear regression 
## first create variable  for predictor from dataframe (columes)
## then fit the variable and y value into .fit
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])

## to find value of intercept (a)
