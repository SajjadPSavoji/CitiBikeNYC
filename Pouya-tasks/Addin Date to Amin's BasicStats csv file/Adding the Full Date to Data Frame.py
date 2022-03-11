#!/usr/bin/env python
# coding: utf-8

# # Adding Full Date to Data Frame

# ## Import Packages

# In[89]:


import numpy as np
import pandas as pd


# In[90]:


df = pd.read_csv("C:/Users/adria/OneDrive/Desktop/CitiBikeNYC/Basic Stats/BasicStats.csv")
df['date'] = df['Year'].astype('str')+'-'+df['Month'].astype('str')
first_column = df.pop('date')
df.insert(0, 'Date', first_column)

