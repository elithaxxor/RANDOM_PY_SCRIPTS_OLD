import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np


'''
!wget -O FuelConsumption.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv
## simple regression - when one indepnedint var is used to predict another var 
## multople linear regression = 
'''

'''
1. read csv 
2. select features for regression
3. plot 
4. create training [80:20] test/split 
5. train data set 
6. [MULTIPLE LINEAR-REGRESSION]
7. OLS - use to estimate unknown paramaters in linear regression model. Minimizes sum of sqrt between predicted and dependant vars 
'''
#1
df = pd.read_csv("FuelConsumption.csv")
df.head(10)

#2
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(10)

#3
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

#4
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

#5
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


#6- create linear regresion model, and establish x/y coef
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)

#7 OLS -  test aqquracy
y_hat= regr.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Residual sum of squares: %.2f"
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))




'''
1. read csv 
2. select features for regression
3. plot 
4. create training [80:20] test/split 
5. train data set 
'''


#1
df = pd.read_csv("FuelConsumption.csv")
df.head(10)

#2
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
cdf.head(10)

#3
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

#4
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

#5
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

