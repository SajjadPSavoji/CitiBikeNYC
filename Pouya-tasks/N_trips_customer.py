#!/usr/bin/env python
# coding: utf-8

# # Number of Trips, Number of Customer Type Usage

# ## Import Packages

# In[115]:


import numpy as np
import pandas as pd
import os
import glob


# ## Main Function

# In[126]:


def N_trips_customer(datasets_address, output_address):
    
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(datasets_address, "*.csv"))

    col = ['Date', 'Number of Trips', 'Number_of_Members','Number_of_Rentals']
    export_data = pd.DataFrame(columns= col)

    j = 0
    for i in csv_files:

        data = pd.read_csv(i)
        number_of_trips = len(data)

        if ('usertype' in data.columns) == True:

            number_of_members = data['usertype'].value_counts()['Subscriber']
            number_of_rentals =  number_of_trips - number_of_members   
            date = data.loc[0,'starttime'][0:7]

        else:

            number_of_members = data['member_casual'].value_counts()['member']
            number_of_rentals =  number_of_trips - number_of_members
            date = data.loc[0,'started_at'][0:7]

        export_data.loc[j,:] = [date, number_of_trips,number_of_members,number_of_rentals]
        j+=1

        
    ## Eport the DataFrame
    export_data.to_csv(output_address, index = False)

