import pandas as pd
import numpy as np

 . fit() is use to train datasets
.fit_transform() and .transform are used together while scaling or standarding
 our training set

# .fit  is used to calculate mean and variance of each feature present in data
# the fit_transform method is tranforming all the features using the mean and variance (from fit)
# # .predict() is used to see the output of the model . ex:
#  .score () is used find the r^ of data -- negative r value is overfitting
#
yhat = poly.predict(x_test_pr)
yhat[0:5]


# Import clean data
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
df = pd.read_csv(path)


df.to_csv('module_5_auto.csv')


### Build distribution plot
def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))

    ax1 = sns.distplot(RedFunction, hist=False, color="r", label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')

    plt.show()
    plt.close()

    ##### Training Data ########

def PollyPlot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))


    #training data
    #testing data
    # lr:  linear regression object
    #poly_transform:  polynomial transformation object

    xmax=max([xtrain.values.max(), xtest.values.max()])

    xmin=min([xtrain.values.min(), xtest.values.min()])

    x=np.arange(xmin, xmax, 0.1)


    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plotplo(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()


######

# First in the model, should be splitting the data into training and testing data
## create two data frames ydata

from sklearn.model_selection import train_test_split
y_data = df['price'] ## target data frame
x_data=df.drop('price',axis=1) ## Drop the price from dataframe index, since it is
                                ### the target

##### This is to randomly split the data using the funciotn train_test_split
## test size makes is % of sample : training sample ratio
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
print("number of test samples :", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

### Example ###
## using the train_test_split
_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
print("number of test samples :", x_test1.shape[0])
print("number of training samples:",x_train1.shape[0])

## next, crate a linear regression model && fit  model
## the linear regression will be used to calculate P_SCORE and R^2
lre=LinearRegression()## fid tehe model using feature horsepowe
lre.fit(x_train[['horsepower']], y_train)
lre.score(x_test[['horsepower']], y_test) ###  to calculate the p_score
## output 0.36358755750788263
lre.score(x_test[['horsepower']], y_test) ## calculate the r^2

##### EXAMPLE #### - Find r^2 on the test data 50%
x_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.4,
                                                                        random_state=0)
lre.fit(x_train1[['horsepower']],y_train1)
lre.score(x_test1[['horsepower']],y_test1)

################# Cross Validation ################
from sklearn.model_selection import cross_val_score

#create object
Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)
Rcross
### caulculate mean  and standard dev. of object.
print("The mean of the folds are", Rcross.mean(),
    "and the standard deviation is" , Rcross.std())

### to calculate the negative squred erorr as a score.
-1 * cross_val_score(lre,x_data[['horsepower']], y_data,cv=4,scoring='neg_mean_squared_error')
#  Output
# [24]:
# array([20254142.84026702, 43745493.2650517 , 12539630.34014931,
#        17561927.72247591])
#
# Calculate the average R^2 using two folds, then find the average R^2 for
# the second fold utilizing the "horsepower" feature:
# cross_val_predict to predict the output

from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_predict

Rc=cross_val_score(lre,x_data[['horsepower']], y_data,cv=2) ## indicate 2 folds
Rc.mean()
## output: 0.5166761697127429
Rc=cross_val_predict(lre,x_data[['horsepower']], y_data,cv=2) ## to prdict the output
Rc.mean()
## output:13202.065033614697


####### OVERFITTING, UNDERFITTING AND MODEL SELECTION ########
## test data aka Out of sample data -- better model on how sample will work in real world
### because of over Fitting---> better for multile linear and plynomial regression

## first create multiple linear regression object and train model using columes
## second --- cast prdiction using trianing data --
lr = LinearRegression() # set up object as lr.
lr.fit(x_train[['horsepower', 'curb-weight', 'engine-size',
                'highway-mpg']], y_train) # train object
############# TRAINING DATA ##############
## predict using training data && predict using test data
yhat_train = lr.predict(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_train[0:5] # training data
yhat_test = lr.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_test[0:5] # test data
                #### OUTPUT of TRAINED DATA ####
# array([ 7426.6731551 , 28323.75090803, 14213.38819709,  4052.34146983,
#        34500.19124244])
#
# array([11349.35089149,  5884.11059106, 11208.6928275 ,  6641.07786278,
#        15565.79920282])
#
#
######### PERFOMRING MODEL EVAULATION ########
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

### To perform model evaluation, use seasborns and distributionplot to vizualise trianed data
Title = 'Distribution  Plot of  Predicted Value Using Training Data vs Training Data Distribution'
DistributionPlot(y_train, yhat_train, "Actual Values (Train)", "Predicted Values (Train)", Title)
#
# The output shows the model respondoing well to the data. both lines are close to each together

## now we are going to output a model with more trained data
Title='Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution of Test Data'
DistributionPlot(y_test,yhat_test,"Actual Values (Test)","Predicted Values (Test)",Title)


##########################################################
def PollyPlot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))


    #training data
    #testing data
    # lr:  linear regression object
    #poly_transform:  polynomial transformation object

    xmax=max([xtrain.values.max(), xtest.values.max()])

    xmin=min([xtrain.values.min(), xtest.values.min()])

    x=np.arange(xmin, xmax, 0.1)


    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plotplo(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()
##### TESTING DTA SET WITH POLYNORMAL REGRESSION  ######
### OVERFITTING---> Occurs when the model fits the noise, but not the underlying preocessing
### too much noise means alot of variation
# sometimes these features can result in improved modeling performance, although at
# the cost of adding thousands or even millions of additional input variables.

########## CREATING A DEGREE 5 MODEL ############
 # 55 percent of the data for training and the rest for testing:
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data,
                                        test_size=0.45, random_state=0)

### CREATING A DEGREE 5 POLYOMIAL ON 'horsepower'
## pr.fit_transform
pr = PolynomialFeatures(degree=5)
x_train_pr = pr.fit_transform(x_train[['horsepower']]) ## fit_transform is used to
x_test_pr = pr.fit_transform(x_test[['horsepower']])   ##
pr
#PolynomialFeatures(degree=5, include_bias=True, interaction_only=False)
## create linear regression model 'molley' and train it.
## we are going to train x_train_pr and x_test_pr,
poly = LinearRegression()
poly.fit(x_train_pr, y_train) ### fitting the 5 degree polynomial
#
## use .predict() to show the output of the model
yhat = poly.predict(x_test_pr)
yhat[0:5]
## prints the first 5 predicted values and compares it to actual targest
print("Predicted values:", yhat[0:4])
print("True values:", y_test[0:4].values)
### OUTPUT ###
# Predicted values: [ 6728.68465468  7308.01690973 12213.81302023 18893.19052853]
# True values: [ 6295. 10698. 13860. 13499.]

### calling the function PollyPlot (defined earlier) to display trianing data
PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train, y_test, poly,pr)
## r^2 of training dat and test data
poly.score(x_train_pr, y_train) #training dta
poly.score(x_test_pr, y_test)   #test data
# 0.556771690250259 -->  r values of trainin data
# -29.871506261647205 -->> r value of test data -- negative r value is sign of OVERFITTING
#

########################## EXAMPLES #################
def f(order, test_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=test_data, random_state=0)
    pr = PolynomialFeatures(degree=order)
    x_train_pr = pr.fit_transform(x_train[['horsepower']])
    x_test_pr = pr.fit_transform(x_test[['horsepower']])
    poly = LinearRegression()
    poly.fit(x_train_pr,y_train)
    PollyPlot(x_train[['horsepower']], x_test[['horsepower']], y_train,y_test, poly, pr)'

## ALLOWS US TO TEST DIFFERNT POLYNOMIAL
interact(f, order=(0, 6, 1), test_data=(0.05, 0.95, 0.05))

<function __main__.f(order, test_data)>
### QUESTION CREATE A POLYNOMIAL TRANFOMATION WITH MORE THAN ONE FEATURE
pr1=PolynomialFeatures(degree=2)
### TRANSFORM THE TRAINING AND TTEST MODELS FOR ADDITIONAL FEATURS ##
x_train_pr1=pr1.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
x_test_pr1=pr1.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
#### QUESTION Find the dimenions of the new feature (features are variables) ###
x_train_pr1.shape
## output (110, 15) #15 features.
## QUESTION: CREATE LINEAR REGRESSION MODEL & TRAIN IT USING FIT
poly1=LinearRegression().fit(x_train_pr1,y_train)
## QUESTION:: USE THE METHOD PREDICT TO PREDICT AN OUTPUT ON THE POLYNOMIAL FEATURES
## THEN USE DISTIRBUTION PLOT TO DOPSPLAY DISTRIBUTION OF PREDICTED Test

yhat_test1=poly1.predict(x_test_pr1)
Title='Distribution  Plot of  Predicted Value Using Test Data vs Data Distribution'
        'of Test Data'
DistributionPlot(y_test, yhat_test1, "Actual Values (Test)",
                "Predicted Values (Test)", Title)


################# RIDGE RERESSION #################
## ridge regression is best used for multi-polinomial regression where
## mutliple variables and high degrres are used
from sklearn.linear_model import Ridge

## Create two degree polynoimail tranformation --- training methods using
pr=PolynomialFeatures(degree=2) ## create function por, with
x_train_pr=pr.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr=pr.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])

RigeModel=Ridge(alpha=1) ## creates ridge from module linear modules
RigeModel.fit(x_train_pr, y_train) ## fit the model same way as regression

yhat = RigeModel.predict(x_test_pr) ## to obtain prediction -->
                                    ## Yhat - is predictive model

### To compare models- predicted vs test set
### tqdm for nested bars https://tqdm.github.io

######## To find the alpha that minimizes test error -- Use Nested Loop ######
### includes progress bar, tqdm ###

Rsqu_test = []
Rsqu_train = []
dummy1 = []
Alpha = 10 * np.array(range(0,1000))
pbar = tqdm(Alpha)

for alpha in pbar:
    RigeModel = Ridge(alpha=alpha)
    RigeModel.fit(x_train_pr, y_train)
    test_score, train_score = RigeModel.score(x_test_pr, y_test), RigeModel.score(x_train_pr, y_train)

    pbar.set_postfix({"Test Score": test_score, "Train Score": train_score})

    Rsqu_test.append(test_score)
    Rsqu_train.append(train_score)


####
width = 12
height = 10
plt.figure(figsize=(width, height))
plt.plot(Alpha,Rsqu_test, label='validation data  ')  ### validation data
plt.plot(Alpha,Rsqu_train, 'r', label='training Data ') ### training data
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()

############### question #############
#### Perform Ridge Calculation and caulation r^2 using polnomial fatures
### use training and test data to test the model . Alpha parameter set to 10
RigeModel = Ridge(alpha=10) ## sets
RigeModel.fit(x_train_pr, y_train) # trains the model
RigeModel.score(x_test_pr, y_test) # tests the model for r^2


############### GRID SEARCH ############
# Gridserach uses hyperparameter for alpha.
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
#### Objective find the best hyperparameter simplifier #####
## create a list for alpha, then create ridge regression objec. after then,
## then set grid1 to Gridseachacv Object. See iID for exception.
## Finally, test the r^2 score use .score() methods
parameters1= [{'alpha': [0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000]}]
parameters1
RR=Ridge() ## ridge regression object
RR
#create a ridged grid search object:
Grid1 = GridSearchCV(RR, parameters1,cv=4, iid=None) ## sed iid to non to avoid deprication warning
Grid1.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_data) # fit the model
# test the model for r^2
BestRR.score(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_test)
## Output# 0.8411649831036152

########## QUESTIONS ####### ###
# Perform a grid search for the alpha paramater and the noramlaization paratmer
# Then find best values of the paramater.

parameters2= [{'alpha': [0.001,0.1,1, 10, 100, 1000,10000,100000,100000],'normalize':[True,False]} ]
Grid2 = GridSearchCV(Ridge(), parameters2,cv=4)
Grid2.fit(x_data[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']],y_data)
Grid2.best_estimator_


################## RIDGE REGRESSION EXAMPLE ################
### train data and create two sets
from sklearn.linear_model import Ridge

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

######
#
# Create and fit a Ridge regression object using the training data, set the regularization
# parameter to 0.1, and calculate the R^2 using the test data.

RidgeModel = Ridge(alpha = 0.1)
RidgeModel.fit(x_train, y_train)
RidgeModel.score(x_test, y_test)


############# CREATING 2ND TIER POLYNOMIAL RIDGS
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train)
x_test_pr = pr.fit_transform(x_test)
poly = Ridge(alpha=0.1)
poly.fit(x_train_pr, y_train)
poly.score(x_test_pr, y_test)
