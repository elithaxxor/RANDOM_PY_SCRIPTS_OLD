## Model Evaluation ::::::
###### ------> representation of real world
#### Tells us how the module performs in the real world
#### build and train the model with a training set

#### if we us fewer data points to train the model and more to test the models
### the accuarcy of generalixation perfoamce will be less, but the model will ahve better precsion
####

### to over come the problem of having error estimates clos together, and far from true generalixation
## inolement the cross-validatin
#
# In contrast with bias, variance is an algorithm’s flexibility to learn patterns in
the observed data. Variance is the amount that an algorithm will change if a different
dataset is used.

# Bias is measured by the differences between the expected predicted values and the
# observed values, in the dataset D when the prediction variables are at the level
#  of x (X=x).
# #############
#
# Bias measures the deviation between the expected output of our model and the real values,
# so it indicates the fit of our model.
# Variance measures the amount that the outputs of our model will change if a
# different dataset is used. It is the impacts of using different datasets.
#
#
#
# ##### Over Fitting / Under Fitting ################
# ## I have to find the best model to determine the order of the polynoimial to provide
# the best function y(x)M

UNDERFITTING - OCCURS WHEN THE MODEL IS TOO SIMPLE IE- TRYING TO FIT POLY TO SIMPLE REGRESSIN
INCREASING THE XTH ORDER OF THE POLYNOMIAL TO FIT DATAPOINTS AND MODEL GRAPH


ERROR ---> TO NOISE

# ############## Ridge Regression
# Ridge regression is a regression that is employed in a Multiple regression model
#  when Multicollinearity occurs. Multicollinearity is when there is a strong relationship
#  among the independent variables. Ridge regression is very common with polynomial
#  regression.  The next video shows how Ridge regression is used to regularize and
#  reduce the standard errors to avoid over-fitting a regression model
#

## Ridge Regression controles the paramater of large coeefeciants by intorducing
## paramater alphas.
### if alpha is to large, the coeeficainots will apprach zro and underfit the data
## if alpha is 0, over fitting is evident ## alpha at .0001, the over fitting starts to
## subside,
###

## for appha to equal .01, the estimated funcation tracks the actial function.
## when alpha = 1, under fititng starts , it means the fucniotn does not have enough
## flexibililty,
### at alpha = 0, we see extreme underfitting.

###### INORDER TO SELECT ALPHA, USE CROSS VALIDATION.
###### INORDER TO SELECT ALPHA, USE CROSS VALIDATION.
    ### Train --> Predict ---> R^2

from sklearn.model_selectio import train_test_split

x_data-- is the features for training
y_data--- is the target

x_test & y_test are from the module.
''
