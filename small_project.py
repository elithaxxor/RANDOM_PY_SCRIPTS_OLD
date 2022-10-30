from sklearn.neighbors import KNeighborsClassifier
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing
#%matplotlib inline

'''
!wget -O loan_train.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/loan_train.csv
'''
# setting the random seed for similar results on each run
np.random.seed(7)

df = pd.read_csv('loan_train.csv')
df.head()
df.shape

# conver to dt object
df['due_date'] = pd.to_datetime(df['due_date'])
df['effective_date'] = pd.to_datetime(df['effective_date'])
df.head()

# vizulaizaton
df['loan_status'].value_counts()
import seaborn as sns

bins = np.linspace(df.Principal.min(), df.Principal.max(), 10)
g = sns.FacetGrid(df, col="Gender", hue="loan_status", palette="Set1", col_wrap=2)
g.map(plt.hist, 'Principal', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()


bins = np.linspace(df.age.min(), df.age.max(), 10)
g = sns.FacetGrid(df, col="Gender", hue="loan_status", palette="Set1", col_wrap=2)
g.map(plt.hist, 'age', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()


## preprocessing / feature extration && vizualization
## day of the week people get the loan
df['dayofweek'] = df['effective_date'].dt.dayofweek
bins = np.linspace(df.dayofweek.min(), df.dayofweek.max(), 10)
g = sns.FacetGrid(df, col="Gender", hue="loan_status", palette="Set1", col_wrap=2)
g.map(plt.hist, 'dayofweek', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()

## months people get the loan
df['Month'] = df.due_date.dt.month
bins = np.linspace(df.Month.min()-1, df.Month.max()+1, 10)
g = sns.FacetGrid(df, col="Gender", hue="loan_status", palette="Set1", col_wrap=2)
g.map(plt.hist, 'Month', bins=bins, ec="k")
g.axes[-1].legend()
plt.show()


## apply lambda to set day thershold to 4
df['weekend'] = df['dayofweek'].apply(lambda x: 1 if (x>3)  else 0)
df.head()


#### FEATURE BINARIZATION ###
## convert categorical to numerical
df.groupby(['Gender'])['loan_status'].value_counts(normalize=True)

## CONVERTS MALE = 0 FEMALE = 1
df['Gender'].replace(to_replace=['male','female'], value=[0,1],inplace=True)
df.head()

## CREATE NEW COLUMN DEALDINE (subctract duedate from effective date)
df['deadline']=df['due_date']-df['effective_date']
df.head()
## make new col ['deadlines'] date friendly (day, month year)
df['deadline']=df['deadline'].dt.days
df.head(3)


## ONE HOT ENCODING
df.groupby(['education'])['loan_status'].value_counts(normalize=True)

## DROP USELESS DATASETS
len(df[df.education=='Master or Above'])
## (produces 2)

Feature = df[['Principal','terms','age','Gender','weekend','dayofweek']]
Feature = pd.concat([Feature,pd.get_dummies(df['education'])], axis=1)
Feature.drop(['Master or Above'], axis = 1,inplace=True)
Feature.head()

bestScore = 0.0
accList = []
for k in range(3, 12):
    clf_knn = KNeighborsClassifier(n_neighbors=k, algorithm='auto')

    # using 10 fold cross validation for scoring the classifier's accuracy
    scores = cross_val_score(clf_knn, X, y, cv=10)
    score = scores.mean()
    accList.append(score)

    if score > bestScore:
        bestScore = score
        best_clf = clf_knn
        bestK = k

print("Best K is :", bestK, "| Cross validation Accuracy :", bestScore)
clf_knn = best_clf

clf_knn.fit(X_train,y_train)
y_pred=best_clf.predict(X_train)
trainScores['KNN-jaccard']=jaccard_similarity_score(y_train, y_pred)
trainScores['KNN-f1-score']=f1_score(y_train, y_pred, average='weighted')
trainScores
plt.plot(range(3,12),accList)
plt.xlabel('K')
plt.ylabel('CV Accuracy')
plt.show()



## DECISION TREE
from sklearn import tree
from sklearn import tree
#!pip install graphviz
#!pip install pydotplus
import graphviz
import pydotplus

clf_tree = tree.DecisionTreeClassifier()
clf_tree = clf_tree.fit(X_train, y_train)
y_pred=clf_tree.predict(X_train)

clf_tree = tree.DecisionTreeClassifier()
clf_tree = clf_tree.fit(X_train, y_train)
y_pred=clf_tree.predict(X_train)
trainScores['Tree-jaccard']=jaccard_similarity_score(y_train, y_pred)
trainScores['Tree-f1-score']=f1_score(y_train, y_pred, average='weighted')
trainScores


## VIZUALIZE TREE
dot_data = tree.export_graphviz(clf_tree, out_file=None,
                     feature_names=['Principal',
                                    'terms','age',
                                    'Gender',
                                    'weekend',
                                    'Bechalor',
                                    'High School or Below',
                                    'college',
                                    'dayofweek',
                                     #'deadline'
#                                     ,'Month'
                                   ],
                     class_names='loan_status',
                     filled=True, rounded=True,
                     special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)
graph.set_size('"8,8!"')
gvz_graph = graphviz.Source(graph.to_string())

gvz_graph

### SUPPORT VECTOR MACHINE ###
from sklearn import svm
y_train=y_train.astype(float)
clf_svm = svm.LinearSVC(random_state=7)
clf_svm.fit(X_train, y_train)
y_pred=clf_svm.predict(X_train)
trainScores['SVM-jaccard']=jaccard_similarity_score(y_train, y_pred)
trainScores['SVM-f1-score']=f1_score(y_train, y_pred, average='weighted')
trainScores


###  LOGICAL REGRESSION ####
from sklearn.linear_model import LogisticRegression
clf_log = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
clf_log.fit(X_train, y_train)
y_pred=clf_log.predict(X_train)
y_proba=clf_log.predict_proba(X_train)
testScores['LogReg-logLoss']=log_loss(testy, proba)
trainScores['LogReg-jaccard']=jaccard_similarity_score(y_train, y_pred)
trainScores['LogReg-f1-score']=f1_score(y_train, y_pred, average='weighted')
trainScores['LogReg-logLoss']=log_loss(y_train, y_proba)
trainScores

### MODEL EVALUATION
test_df = pd.read_csv('loan_test.csv')
test_df.head()
test_df['due_date'] = pd.to_datetime(test_df['due_date'])
test_df['effective_date'] = pd.to_datetime(test_df['effective_date'])
test_df['dayofweek'] = test_df['effective_date'].dt.dayofweek
test_df['weekend'] = test_df['dayofweek'].apply(lambda x: 1 if (x>3)  else 0)
test_df['Gender'].replace(to_replace=['male','female'], value=[0,1],inplace=True)

# test_df['Month'] = test_df.due_date.dt.month
# test_df['deadline']=test_df['due_date']-test_df['effective_date']
# test_df['deadline']=test_df['deadline'].dt.days

Feature = test_df[['Principal','terms','age','Gender','weekend','dayofweek']]
Feature = pd.concat([Feature,pd.get_dummies(test_df['education'])], axis=1)
Feature.drop(['Master or Above'], axis = 1,inplace=True)

X = Feature
y = test_df['loan_status'].replace(to_replace=['PAIDOFF','COLLECTION'], value=[0,1]).values

testy=y.astype(float)
testX= preprocessing.StandardScaler().fit_transform(X)

testScores={}
knn_pred=clf_knn.predict(testX)
testScores['KNN-jaccard']=jaccard_similarity_score(testy, knn_pred)
testScores['KNN-f1-score']=f1_score(testy, knn_pred, average='weighted')

tree_pred=clf_tree.predict(testX)
testScores['Tree-jaccard']=jaccard_similarity_score(testy, tree_pred)
testScores['Tree-f1-score']=f1_score(testy, tree_pred, average='weighted')

svm_pred=clf_svm.predict(testX)
testScores['SVM-jaccard']=jaccard_similarity_score(testy, svm_pred)
testScores['SVM-f1-score']=f1_score(testy, svm_pred, average='weighted')

log_pred=clf_log.predict(testX)
proba=clf_log.predict_proba(testX)
testScores['LogReg-jaccard']=jaccard_similarity_score(testy, log_pred)
testScores['LogReg-f1-score']=f1_score(testy, log_pred, average='weighted')
testScores['LogReg-logLoss']=log_loss(testy, proba)

trainScores
testScores
list(Feature.columns)















