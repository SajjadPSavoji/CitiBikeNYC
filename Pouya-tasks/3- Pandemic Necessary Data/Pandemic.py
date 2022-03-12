#!/usr/bin/env python
# coding: utf-8

# # Pandemic Basic Data (2018-2020)

# In[74]:


import numpy as np
import pandas as pd
import os
import glob
import ntpath


# In[75]:


def Pandemic_20182020(datasets_address,export_address):
    
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(datasets_address, "*.csv"))
    
    j=0
    col = columns=['Date','Year','Month','Number_of_Trips','Number_of_Trips_by_Subscribers','Number_of_Trips_by_Customers','Number_of_Bikes','Number_of_Used_Stations','MAN','WOMAN','Unknown_Gender']
    final_data = pd.DataFrame(columns = col)

    for i in csv_files:
        
        year = ntpath.basename(i)[0:4]
        month = ntpath.basename(i)[4:6]
        
        data = pd.read_csv(i)
        
        final_data.loc[j,'Date'] = year +'-' + month
        final_data.loc[j,'Year'] = year
        final_data.loc[j,'Month'] = month
        final_data.loc[j,'Number_of_Trips'] = len(data)
        final_data.loc[j,'Number_of_Trips_by_Subscribers'] = len(data[data.loc[:,'usertype']=='Subscriber'])
        final_data.loc[j,'Number_of_Trips_by_Customers'] = len(data) - len(data[data.loc[:,'usertype']=='Subscriber'])
        final_data.loc[j,'Number_of_Bikes'] = len(data.loc[:,'bikeid'].unique())
        final_data.loc[j,'Number_of_Used_Stations'] = len(np.unique(np.vstack((data.loc[:,'start station id'],data.loc[:,'end station id']))))
        final_data.loc[j,'MAN'] = len(data[data.loc[:,'gender']==1])
        final_data.loc[j,'WOMAN'] = len(data[data.loc[:,'gender']==2])
        final_data.loc[j,'Unknown_Gender'] = len(data) - len(data[data.loc[:,'gender']==1]) - len(data[data.loc[:,'gender']==2]) 
        j+=1
        

        
        
    final_data.to_csv(export_address,index=False)


# In[76]:


Pandemic_20182020('C:/Users/adria/OneDrive/Desktop/CSV_files','C:/Users/adria/OneDrive/Desktop/Pandemic_20182020.csv')


# In[ ]:




