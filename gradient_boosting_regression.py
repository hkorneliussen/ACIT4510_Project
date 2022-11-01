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

#checking of dataset exists, if not - downloading it 

path = 'dataset/'
if not os.path.exists(path):
  print('no')
else:
  print('yes')
