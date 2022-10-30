'''
This python code creates a numerical version of the demo dataset

based on: https://towardsdatascience.com/feature-engineering-in-python-part-i-the-most-powerful-way-of-dealing-with-data-8e2447e7c69e

https://github.com/Shivanandroy/CategoricalEmbedder/blob/master/example_notebook/Example%20Notebook.ipynb


'''

#import modules 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import os.path
import categorical_embedder as ce
from sklearn.model_selection import train_test_split

import subprocess

#check if the demo dataset exist. If not, create it
path = 'original_dataset_demo.csv'
if not os.path.isfile(path):
  exec(open("create_spotify_dataset.py").read())
  
#load the original (demo) dataset
features = pd.read_csv('original_dataset_demo.csv', index_col=[0])

#removing null values in Name column from the data
features = features.drop(features.loc[features["Name"].isnull()].index)

#removing null values in Artist column from the data
features = features.drop(features.loc[features["Artist"].isnull()].index)

#the feature Release Date does not give any information to the model, since its just raw data and no numberical value
#it can be exploited by creating two new features: mounth and year 
features['Release_Month'] = pd.to_datetime(features.Release_date, format='%Y-%m-%d').dt.month_name()
features['Release_Year'] = pd.to_datetime(features.Release_date).dt.year
features.drop('Release_date', axis=1, inplace=True)

#features key, mode and release year as few different categories. 
#They are also already int values and can be kept as they are 

#the feature release_month have few categories and are object type
#it can be replaced by numerical values manually
#1 will represent January, 2 February, etc. 
replace_map = {'Release_Month' : {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}}
labels = features['Release_Month'].astype('category').cat.categories.tolist()
replace_map_comp = {'Release_Month' : {k: v for k, v in zip(labels, list(range(1, len(labels)+1)))}} 
features.replace(replace_map_comp, inplace=True)

#defining features
X = features.drop(['Popularity'], axis=1)
y = features['Popularity']

# ce.get_embedding_info identifies the categorical variables, # of unique values and embedding size and returns a dictionary
embedding_info = ce.get_embedding_info(X, categorical_variables=["Genre", "Artist", "Name", "Album"])

# ce.get_label_encoded_data integer encodes the categorical variables and prepares it to feed it to neural network
X_encoded,encoders = ce.get_label_encoded_data(X, categorical_variables=["Genre", "Artist", "Name", "Album"])

# splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X_encoded,y)

# ce.get_embeddings trains NN, extracts embeddings and return a dictionary containing the embeddings
embeddings = ce.get_embeddings(X_train, y_train, categorical_embedding_info=embedding_info, 
                            is_classification=True, epochs=100,batch_size=256)

# converting to dataframe for easy readibility
dfs = ce.get_embeddings_in_dataframe(embeddings=embeddings, encoders=encoders)

# including embeddings in the dataset:
data = ce.fit_transform(features, embeddings=embeddings, encoders=encoders, drop_categorical_vars=True)

#adding popularity back to the dataset
data.append(y)

data.to_csv('numerical_dataset_demo.csv')
                        
