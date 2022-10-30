'''
This python code creates a numerical version of the demo dataset
'''

#import modules 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import os.path

path = 'demo_audio_features.csv'
if os.path.isfile(path):
  print('exist')
else:
  print('no')


'''
original = audio_features.csv'
features = pd.read_csv(feature_list, index_col=[0])
features.head(3)

'''
