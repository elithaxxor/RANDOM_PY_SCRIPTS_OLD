import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

'''
import wget
!wget -O teleCust1000t.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv
%matplotlib inline
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv"
dataset = wget.download(url)
'''


df = pd.read_csv('teleCust1000t.csv')
head = df.head(12)
print(type(head))
print(head)
# basica vizualization
# value counts - returns a series containing amount of unique values
unique = df['custcat'].value_counts()
shape = df['custcat'].shape
size = df['custcat'].size
custcat = df['custcat'].values

# to read teh columns (the features)
cols = df.columns
print(cols)

print(),print()
print('X' * 50)
print('X' * 50)
print('shape\n',shape,'\n')
print(type(shape))
print('X' * 50)
print('size\n',size,'\n')
print(type(size))
print('X' * 50)
print('unique\n',unique,'\n')
print(type(unique))
print('X' * 50)
print('to view specific col [custcat]\n',custcat[0:10],'\n')
print('X' * 50)

print(),print(),print(),print(),print()
print('X'*50)

### CONVERT PANDAS ARRAY TO NUMPY *FOR SKLEARN
print('Convert PD to NP [for sklearn]')
X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
print(X[0:5])
print(type(X))


#### NORMALIZE DATA-- always needed for for computer to interpret
NORMALIZED = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
print(NORMALIZED[0:10])

#### SKLEARN TRAIN/TEST-SPLIT
# must achieve high out of sample accuracy to make correct predictions.
# the train/test split is an evaluation approach to improve out of sample accuracy.
X_train, X_test, y_train, y_test = train_test_splitneighbor = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
print('\n', 'X' * 50)
print('Training Set : \n', X_train.shape, X_train.size)
print('Testing Set : \n', X_train.shape, X_train.size)
print('X' * 50,'\n')

### K-NEAREST CLASSIFCATION - ## --- Start of Model Training --
# voting system to find the most relevant nodes within the array
# look out for anomolous data in the data (plot graph)
# keep increasing 'k' (knn) and read accuracy data.
# 1. Train Model and Predict
# 2. Predict.

#1 ## build model
print('\n', 'X' * 50)
k = 4
neighbor = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
print('K-Nearest Neighbor : ', neighbor)
#2 ## predict model
yhat = neigh.predict(X_test)
print(yhat[0:5])
print('X' * 50,'\n')
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neighbor.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))


## example 2 ##
k = 6
neigh6 = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
yhat6 = neigh6.predict(X_test)
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh6.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat6))

Ks = 10
mean_acc = np.zeros((Ks - 1))
std_acc = np.zeros((Ks - 1))



### to test multiple K's and represetn accuracy score ###
for n in range(1, Ks):
    # Train Model and Predict
    neigh = KNeighborsClassifier(n_neighbors=n).fit(X_train, y_train)
    yhat = neigh.predict(X_test)
    mean_acc[n - 1] = metrics.accuracy_score(y_test, yhat)

    std_acc[n - 1] = np.std(yhat == y_test) / np.sqrt(yhat.shape[0])

print(mean_acc)

### PLOT
plt.plot(range(1,Ks),mean_acc,'g')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.fill_between(range(1,Ks),mean_acc - 3 * std_acc,mean_acc + 3 * std_acc, alpha=0.10,color="green")
plt.legend(('Accuracy ', '+/- 1xstd','+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()

