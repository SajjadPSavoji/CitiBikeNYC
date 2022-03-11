#!/usr/bin/env python
# coding: utf-8

# In[94]:


import numpy as np
import pandas as pd
import os
import glob
import ntpath


# In[97]:


def features_unification(datasets_address):
    
    col = ['tripduration', 'starttime', 'stoptime', 'start station id',
           'start station name', 'start station latitude',
           'start station longitude', 'end station id', 'end station name',
           'end station latitude', 'end station longitude', 'bikeid', 'usertype',
           'birth year', 'gender']
    
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(datasets_address, "*.csv"))

    for i in csv_files:
        
        ## Features Unification
        
        data = pd.read_csv(i)
        data.columns = col
        
        ## Adding Age Column
        if ntpath.basename(i)[0:2] == 'JC':
            year = np.int(ntpath.basename(i)[3:7])
        else:
            year = np.int(ntpath.basename(i)[0:4])    
        
        
        data.loc[data.loc[:,'usertype']=='Subscriber','age'] = year - data[data.loc[:,'usertype']=='Subscriber'].loc[:,'birth year'].astype('int')
        
        ## Export
        data.to_csv(i, index = False)


# In[98]:


features_unification('C:/Users/adria/OneDrive/Desktop')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




