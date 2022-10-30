# simple linear regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

###### DIFFERENT MODELING TECHNIQUIES #######
#### Simple Lineawr Model (SLR) ##########
####### Plynomial Fit ####################
############# Multiple Linear Regression ##############

######### THIS IS IN SAMPLE EVAULATION ########
##### It tells us how well our model fits the data to train it #########
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
#########################################

##Fit a linear regression model to predict the <code>'price'</code> using the list of features:
features = ["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
X = df[features]
Y= df['price']
lm = LinearRegression()
lm.fit(X, Y)
lm.score(X, Y)

###### multi linear regression
## first create variable  for predictor from dataframe (columes)
## then fit the variable and y value into .fit
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(Z, df['price'])

## to find value of intercept (a)

# What is the equation of the predicted line?
# You can use x and yhat or "engine-size" or "price".

Click here for the solution
# using X and Y
Yhat=-7963.34 + 166.86*X

Price=-7963.34 + 166.86*engine-size

##### MODEL Evaluation using VIZUALIZATION
## use regression plots when evaluation simple regression models.
## Import seaborn
# visualization package: seaborn
import seaborn as sns
%matplotlib inline

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)


### comparing regression plots
plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
### given the plots on above tables, use .corr to give data on correlation
df[["peak-rpm","highway-mpg","price"]].corr()


########### Residuital plot ###############
###### TO MEASURE VARIANCE OF THE DATASET #######
### a residual is the difference between the observed value 9y0 and the predicted  value Yhat
## the difference between obserevd value (y) and predicted value (yhat)
## a resdiual plot is a graph that shows the resudals on the verticle and indipednet on x axis


### Residual Plot -- DIFFERNET BTWEEN Y AND Yhat

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()


########## ---Graphing Multi Linearar Regression Models--- ############
### USE DISTRIBUTION PLOTS ######

### First make a prediction ####--- Y_Hat is predited value
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']] ## from above ^
Y_hat = lm.predict(Z)  #### REMEMBER - Y_hat is what we want to predict for (x axis - price)

####
#Plot the graph here
plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()

#### POLYNOMIAL REGRESSION AND PIPELINES ####
# polynomial regression renders non linear it renders linear lines
## you get the relationship by squaring or setting higher odered terms for the
# predicotr variables

### differt orders of polynomial regression
## 1. quadriatic -2nd orders##
#2. cubic - 3rd orders
#3. higher-orders


### MULTI-LINEAR REGRESSION cannot be izualed with regression or residual plot
### it can only be looked at by using DISTRIBUTION PLOTS
#### MUST CREATE A PREDICTION


def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']


## EXAMPLE:: Create and train a linear regression model lm2 where:
## The response variable is price and teh preictor varible is "normalized losses"
### simple regression
lm2 = LinearRegression()
lm2.fit(df[['normalized-losses' , 'highway-mpg']],df['price'])

## find the coeefeciant of the model:
lm2.coef_ # reteruns the coeffeciant of predictor Variables


######### MODEL EVALUATION USING VIZUALIZATION ########
### for simple linear regression --- use scatter plots AKA regression plots ###
##
# import the visualization package: seaborn
import seaborn as sns
%matplotlib inline

## settup vizualization
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)

###  -- Comparing Regressions -- ##
plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

## Print data correlation #### < ---------- DO NOT FOR GET THIS
df[["peak-rpm","highway-mpg","price"]].corr()


###################  MULTI  LINEAR REGRESSINO ###########
### Can only visualise with distrubation model
# first build a prediction

Y_hat = lm.predict(Z)

plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()


########### POLYNOMIAL REGRESSION AND PIPELINES ######
### we get polynomial regression by squaring
## we can gert non linear realtionships by sqwuaring (or setting higher exponenets)
## for the predictor variable

######## USE THIS TO GET BETTER ACCURACY. ADDD MORE DATA POINTS #############


## function to plot data --
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

#Getting Variables
x = df['highway-mpg']
y = df['price']

## Here we use a polynomial of the 3rd order (cubic)
### .polyfit cubes and squares values (x^3) + (x^2) - (x)
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

PlotPolly(p, x, y, 'highway-mpg') ## plots and displays curve regressihion graph.

#################
#### TO CREATE polynomial Model
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
print(p1)
PlotPolly(p1,x,y, 'Highway MPG')


## Multivariate Polynoial Function
### a multivariate pluynomial function is xomplicated (do research )

from sklearn.preprocessing import PolynomialFeatures

# create objects
pr=PolynomialFeatures(degree=2)
pr
# PolynomialFeatures(degree=2, include_bias=True, interaction_only=False)
Z_pr=pr.fit_transform(Z) ### ???? -- prior to transfor 201 and 4 feature, after tarnsfor 201 and 15
Z.shape  # RETURNS (201, 4)
Z_pr.shape # RETURNS (201, 15)


##### PIPELINES ####
## DATA PIPELEINS simpliofy the steps of preocessing data
### use standard scaler as a 'step' in pipelines

from sklearn.pipeline import Pipeline  ##### need to create a list to import to pipeline
from sklearn.preprocessing import StandardScaler

### create a pipeline by creating a list of tuples- including the nameof the model or estimator of
### corrosoing constructor

##### create a list to use as an argument  to the pipeline construtor
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model',LinearRegression())]
##  input the list
pipe=Pipeline(Input)
pipe

#### normalizing the data
# first convert the data to float
Z = Z.astype(float)
pipe.fit(Z,y)

### normalize the data and peforma  tranforme and produce predicition simulatinously
ypipe=pipe.predict(Z)
ypipe[0:4]

### Excersize ######
# Create a pipeline that standardizes the data, then produce a prediction using a
# linear regression model using the features Z and target y.

Input=[('scale',StandardScaler()),('model',LinearRegression())]
pipe=Pipeline(Input)
pipe.fit(Z,y)
ypipe=pipe.predict(Z)  #### producing prediction
ypipe[0:10]


################ MODEL EVALUATION #######################
##### MEASURES FOR IN-SAMPLE EVALUTATION #########

### TO DISPLLAY A QUANTITIVE MEASURE OF HOW ACCURATE MODEL IS #####

## There are two very imporant measures in statistics to determine accurcay
# The:  R^2 / R-squared Mean Squared Error (MSE)
# R^2 is the coeffeciant determination, it is used to indaicate ow close the ate is to the Fitted
## regression line =
# the value of r^2 is the percetaage of varationof the response between the variable

#### The Mean Squared Error (MSE)
### Measures the averages of the swaures of errors.
### Difference between actual y and estimated y


################### MODELING SIMPLE LINEAR REGRESSION ###############
lm.fit(x, y)
# Find the R^2
print('The R-square is: ', lm.score(X, Y)) ### CALCULATES VARIATION


################## CALCULATING MSE #############################
## predict the output (Y_Hat) using x as variables
from sklearn.metrics import mean_squared_error
# create object
mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)
## create prediction ###
Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])



###################### MODELING MULTIPLE LINEAR REGRESSION #################
######### r vaue
# fit the model then calculate r  value
lm.fit(Z, df['price'])
print('The R-square is: ', lm.score(Z, df['price'])) ## calculates the r value
####### CALCULATE THE MSE #########
### produce a predeictor
## then Compare predicted results with actual results ###
Y_predict_multifit = lm.predict(Z)
print('The mean square error of price and predicted value using multifit is: ', \
      mean_squared_error(df['price'], Y_predict_multifit))


################ Polynomial Fit #######################
### polynomial fit uses r2_function

from sklearn.metrics import r2_score

r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)

######### PREDICTION AND DECISION MAKING ###############
# Insread of using the method .fit, we will use the methic .predict

import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

## create input
new_input=np.arange(1, 100, 1).reshape(-1, 1)
# fit the model
lm.fit(X, Y)
lm

yhat=lm.predict(new_input) ## Produce a prediction, creates datapoint "new input"
yhat[0:5]

### Plot the data ###
plt.plot(new_input, yhat)
plt.show()

############################ CHAPTER NOTES #####################
What is a good R-squared value?
When comparing models, the model with the higher R-squared value is a better fit for the data.

What is a good MSE?
When comparing models, the model with the smallest MSE value is a better fit for the data.
#########################'''
