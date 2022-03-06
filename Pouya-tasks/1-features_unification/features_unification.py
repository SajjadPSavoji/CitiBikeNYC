#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import glob


# In[6]:


def features_unification(datasets_address):
    
    col = ['tripduration', 'starttime', 'stoptime', 'start station id',
           'start station name', 'start station latitude',
           'start station longitude', 'end station id', 'end station name',
           'end station latitude', 'end station longitude', 'bikeid', 'usertype',
           'birth year', 'gender']
    
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(datasets_address, "*.csv"))

    for i in csv_files:
        
        data = pd.read_csv(i)
        data.columns = col
        data.to_csv(i, index = False)
    
    

