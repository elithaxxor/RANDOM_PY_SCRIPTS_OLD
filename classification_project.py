import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing
import seaborn as sns

'''
!wget -O loan_train.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/loan_train.csv
!conda install -c anaconda seaborn -y
%matplotlib inline

'''


'''
1. load df 
2. convert dates to  datetime objects 
3. determine how much of each class per column (value_counts())
4. plot with seaborns -- hue = loanstatus ; col = gender 
5. #5 PRE-PROCESSING / FEATURE SELECTION 
6. Feature binarization (using lamda) to set threshold less than 4 
7. Convert Categorical Features to numerical values (gender to 0s and 1s) 
8. One hot encoding create input values (numerical vars) by convert categocial (nomial) values 
#9- Feature Selection 
10. NORMALIZE DATA (should be done after test/train split) --> gives data zero mean and unit variance. 
'''


df = pd.read_csv('loan_train.csv')
df.head()
print(df.shape)

#2
df['due_date'] = pd.to_datetime(df['due_date'])
df['effective_date'] = pd.to_datetime(df['effective_date'])
df['dayofweek'] = df['effective_date'].dt.dayofweek


df.head()
print(df['effective_date'])
print(df['due_date'])
#3
print(df['loan_status'].value_counts())
#4
bins = np.linspace(df.age.min(), df.age.max(), 10)
g = sns.FacetGrid(df, col="Gender", hue="loan_status", palette="Set1", col_wrap=2)
g.map(plt.hist, 'age', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()


#5 PRE-PROCESSING / FEATURE SELECTION
df['dayofweek'] = df['effective_date'].dt.dayofweek
bins = np.linspace(df.dayofweek.min(), df.dayofweek.max(), 10)
g = sns.FacetGrid(df, col="Gender", hue="loan_status", palette="Set1", col_wrap=2)
g.map(plt.hist, 'dayofweek', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()

#6
df['weekend'] = df['dayofweek'].apply(lambda x: 1 if (x>3)  else 0) ##set threshold under <4
df.groupby(['Gender'])['loan_status'].value_counts(normalize=True) ## display loan statistics based on gender
df.head()

#7- simple categorical conversion, and one hot encoding
df['Gender'].replace(to_replace=['male','female'], value=[0,1],inplace=True) # simple categorical convert
df.head()
#8 one hot encoding
Feature = df[['Principal','terms','age','Gender','weekend']]
Feature = pd.concat([Feature,pd.get_dummies(df['education'])], axis=1)
Feature.drop(['Master or Above'], axis = 1,inplace=True)
Feature.head()

#9- Feature Selection
Feature = df[['Principal','terms','age','Gender','weekend']]
Feature = pd.concat([Feature,pd.get_dummies(df['education'])], axis=1)
Feature.drop(['Master or Above'], axis = 1,inplace=True)
Feature.head()
X = Feature
print(X[0:5])
y = df['loan_status'].values
print(y[0:5])


#10- Normalize Data
X= preprocessing.StandardScaler().fit(X).transform(X)
print(X[0:5])















