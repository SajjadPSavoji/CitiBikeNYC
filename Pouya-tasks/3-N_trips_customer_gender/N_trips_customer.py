#!/usr/bin/env python
# coding: utf-8

# # Number of Trips, Number of Customer Type Usage

# ## Import Packages

# In[1]:


import numpy as np
import pandas as pd
import os
import glob
from pathlib import Path


# ## Main Function

# In[2]:


def N_trips_customer(datasets_address, output_address):
    
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(datasets_address, "*.csv"))

    col = ['Date', 'Number of Trips', 'Number_of_Members','Number_of_Rentals', 'Male', 'Female', 'Unknown_gender']
    export_data = pd.DataFrame(columns= col)

    j = 0
    for i in csv_files:

        data = pd.read_csv(i)
        number_of_trips = len(data)

#         if ('usertype' in data.columns) == True:                      Since we are about to consider datasets between 2013-2020

        number_of_members = data.loc[:,'usertype'].value_counts()['Subscriber']
        number_of_rentals =  number_of_trips - number_of_members   
        
        male_trips =  data.loc[:,'gender'].value_counts()[1]
        female_trips = data.loc[:,'gender'].value_counts()[2]
        unknown_gender_trips = data.loc[:,'gender'].value_counts()[0]
        
        date = Path(i).name[0:4]

#         else:

#             number_of_members = data['member_casual'].value_counts()['member']
#             number_of_rentals =  number_of_trips - number_of_members
#             date = data.loc[0,'started_at'][0:7]

        export_data.loc[j,:] = [date, number_of_trips,number_of_members,number_of_rentals,                                male_trips,female_trips,unknown_gender_trips]
        j+=1

        
    ## Eport the DataFrame
    export_data.to_csv(output_address, index = False)

