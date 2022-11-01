'''
This code implements gradient boosting regression on all dataset version. 

Based on code implementation from: https://vagifaliyev.medium.com/a-hands-on-explanation-of-gradient-boosting-regression-4cfe7cfdf9e

'''

#importing modules 
import pandas as pd
from sklearn import preprocessing
import plotly.express as px

import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import classification_report
from sklearn.ensemble import GradientBoostingClassifier

import matplotlib.pyplot as plt 
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4

import os
import sys
import time

#checking of dataset exists, if not exit
path = 'dataset/'
if not os.path.exists(path):
  print('Please run "setting up environment" cells to download dataset')
  sys.exit()

#loading original dataset
original_dataset_path = 'dataset/audio_features.csv'
original_dataset = pd.read_csv(original_dataset_path, index_col=[0])

#loading numerical dataset
numerical_dataset_path = 'dataset/embedded_features.csv'
numerical_dataset = pd.read_csv(numerical_dataset_path, index_col=[0])

#loading resampled dataset
resampled_dataset_train_path = 'dataset/train.csv'
resampled_dataset_test_path = 'dataset/test.csv'
resampled_dataset_train = pd.read_csv(resampled_dataset_train_path, index_col=[0])
resampled_dataset_test = pd.read_csv(resampled_dataset_test_path, index_col=[0])

# applying gradient boosting regression on original dataset

#dropping cateogircal (object) data
original = original_dataset.drop(['Genre', 'Name', 'Album', 'Artist', 'Release_date'], axis=1)

#applying normalization
scaler = preprocessing.MinMaxScaler()
names = original.columns
d = scaler.fit_transform(original)
original_scaled = pd.DataFrame(d, columns=names)
original_scaled.head(3)

#initializing features and target 
X, y = original_scaled.drop('Popularity', axis=1), original_scaled['Popularity']
#using 5 fold cross validation to split the dataset into a training set and a validation set 
kf = KFold(n_splits=5, random_state=42, shuffle=True)

for train_index, val_index in kf.split(X):
  X_train, X_val = X.iloc[train_index], X.iloc[val_index]
  y_train, y_val = y.iloc[train_index], y.iloc[val_index]

