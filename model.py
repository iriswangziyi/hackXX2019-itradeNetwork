import sys
import scipy
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import itemfreq

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import recall_score
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import statsmodels.api as sm

from collections import Counter
from imblearn import under_sampling, over_sampling
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

df_features = pd.read_csv("df_features.csv")
df_features = df_features[df_features['Fruit Or Veg'].notna()]
df_features['90%rejected']=np.where(df_features['%fail']>=0.9, 1, 0)

df_features = df_features.loc[:15000,:]
# Sample data:
#   White Cabbages
#   Vendor  63b9d36c
#   Warehouse  e5847f7c
#   Inspector  4bb23bf2
#   3
#   spring

enc = OneHotEncoder(handle_unknown='ignore')

def train_unbalanced(features, model):
    # Get relevant columns: X is features, y is label
    print("Getting relevant columns")
    X = df_features[features]
    y = df_features['90%rejected']

    # one-hot encode the categorical features
    print("One-hot encoding categorical features")
    enc.fit(X)
    X = enc.transform(X)
    
    # Split 80/20 training and test data
    print("Splitting data")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X_train, y_train, test_size=0.10, random_state=12)
    
    # oversample training data
    print("Oversampling training data")
    sm = SMOTE(random_state=12, ratio = 1.0)
    X_train_res, y_train_res = sm.fit_sample(X_train2, y_train2)
    
    # Classify with given model
    print("Fitting training data to model")
    model.fit(X_train_res, y_train_res)
    
    # Validate: mean accuracy and recall score
    print('Validation Results')
    print(model.score(X_test2, y_test2), 'out of 1.00 predictions were correct')
    y_pred_2=model.predict(X_test2)
    #print(np.unique(y_pred_2))
    print(recall_score(y_test2, y_pred_2), 'out of 1.00 of bad data identified')
    print(y_pred_2.sum())
    
    print('\nTest Results')
    print(model.score(X_test, y_test), 'out of 1.00 predictions were correct')
    y_pred=model.predict(X_test)
    #print(np.unique(y_pred))
    print(recall_score(y_test, y_pred), 'out of 1.00 of bad data identified')
    print(classification_report(y_test, y_pred))
    print(y_pred.sum())
    
    print('training data Results')
    y_model=model.predict(X_train_res)
    print(classification_report(y_train_res, y_model))
    print(y_model.sum())
    
    return model

features=['Category Name', 'Vendor Name', \
          'Shipping Warehouse', 'Inspector', \
          'Shipping Time', 'Season']

model = train_unbalanced(features, \
    DecisionTreeClassifier(criterion="gini", random_state=12, \
                           max_depth=3, min_samples_leaf=5))