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

import subprocess




path = 'demo_audio_features.csv'
if not os.path.isfile(path):
  exec(open("create_spotify_dataset.py").read())
  



'''
original = audio_features.csv'
features = pd.read_csv(feature_list, index_col=[0])
features.head(3)

'''
