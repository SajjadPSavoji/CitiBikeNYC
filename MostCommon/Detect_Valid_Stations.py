# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:10:01 2022

@author: afadaei
"""

import numpy as np
import pandas as pd
import os


def updateStartLocation(StartLocation, dataset, StartLat_string, StartLong_string, StartID_string):
    for i in range(len(dataset)):
        if((dataset[StartLat_string][i], dataset[StartLong_string][i]) not in StartLocation):
            StartLocation[(dataset[StartLat_string][i], dataset[StartLong_string][i])] = dataset[StartID_string][i]
        elif(StartLocation[(dataset[StartLat_string][i], dataset[StartLong_string][i])] != dataset[StartID_string][i]):
            print(StartLocation[(dataset[StartLat_string][i], dataset[StartLong_string][i])], dataset[StartID_string][i])
            print((dataset[StartLat_string][i], dataset[StartLong_string][i]), i)
            print("Something Wrong Mate")
    return StartLocation
    
def updateEndLocation(EndLocation, dataset, EndLat_string, EndLong_string, EndID_string):
    temp = dataset[EndLat_string].isnull()
    for i in range(len(dataset)):
        if(temp[i] == True):
            continue
        if((dataset[EndLat_string][i], dataset[EndLong_string][i]) not in EndLocation): 
            EndLocation[(dataset[EndLat_string][i], dataset[EndLong_string][i])] = dataset[EndID_string][i]
        elif(EndLocation[(dataset[EndLat_string][i], dataset[EndLong_string][i])] != dataset[EndID_string][i]):
            print(EndLocation[(dataset[EndLat_string][i], dataset[EndLong_string][i])], dataset[EndID_string][i])
            print((dataset[EndLat_string][i], dataset[EndLong_string][i]), i)
            print("Something Wrong mate")
    return EndLocation

def DoubleID_Same_Location(DIR_PATH):
    Start = {}
    End = {}
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        #if year == "2013" or year == "2014" or year == "2015" or year == "2016" or year == "2017" or year == "2018" or year == "2019":
         #   continue
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "start station latitude" in data:
                    updateStartLocation(Start, data, "start station latitude", "start station longitude", "start station id")
                    updateEndLocation(End, data, "end station latitude", "end station longitude", "end station id")
                elif "Start Station Latitude" in data:
                    updateStartLocation(Start, data, "Start Station Latitude", "Start Station Longitude", "Start Station ID")
                    updateEndLocation(End, data, "End Station Latitude", "End Station Longitude", "End Station ID")
                elif "start_lat" in data:
                    updateStartLocation(Start, data, "start_lat", "start_lat", "start_station_id")
                    updateEndLocation(End, data, "end_lat", "end_lng", "end_station_id")
                else:
                    print("No Data this year")
                print(year, month)
 
def add_dict(valid_dic, dataset, StartLat_string, StartLong_string, StartID_string, EndLat_string, EndLong_string, EndID_string, maximum_latitude, minimum_latitude, maximum_longitude, minimum_longitude):  
    for i in range(len(dataset)):
        if((dataset[StartLat_string][i] >= minimum_latitude and dataset[StartLat_string][i] <=maximum_latitude) and (dataset[StartLong_string][i] >= minimum_longitude and dataset[StartLong_string][i] <=maximum_longitude)):
            if(dataset[StartID_string][i] > -1):
                valid_dic[(dataset[StartLat_string][i], dataset[StartLong_string][i])] = dataset[StartID_string][i]

    temp = dataset[EndLat_string].isnull()
    for i in range(len(dataset)):
        if(temp[i] == True):
            continue
        if((dataset[StartLat_string][i] >= minimum_latitude and dataset[StartLat_string][i] <=maximum_latitude) and (dataset[StartLong_string][i] >= minimum_longitude and dataset[StartLong_string][i] <=maximum_longitude)):
            if(dataset[EndID_string][i] > -1):
                valid_dic[(dataset[StartLat_string][i], dataset[StartLong_string][i])] = dataset[EndID_string][i]
    return valid_dic
    

def Check_Range_Location(DIR_PATH, maximum_latitude, minimum_latitude, maximum_longitude, minimum_longitude):
    valid_dic = {}
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        #if year == "2013" or year == "2014" or year == "2015" or year == "2016" or year == "2017" or year == "2018" or year == "2019":
         #   continue
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "start station latitude" in data:
                    valid_dic = add_dict(valid_dic, data, "start station latitude", "start station longitude", "start station id", "end station latitude", "end station longitude", "end station id", maximum_latitude, minimum_latitude, maximum_longitude, minimum_longitude)
                elif "Start Station Latitude" in data:
                    valid_dic = add_dict(valid_dic, data, "Start Station Latitude", "Start Station Longitude", "Start Station ID", "End Station Latitude", "End Station Longitude", "End Station ID", maximum_latitude, minimum_latitude, maximum_longitude, minimum_longitude)
                elif "start_lat" in data:
                    valid_dic = add_dict(valid_dic, data, "start_lat", "start_lat", "start_station_id", "end_lat", "end_lng", "end_station_id", maximum_latitude, minimum_latitude, maximum_longitude, minimum_longitude)
                else:
                    print("No Data this year")
                print(year, month)
    return valid_dic
                   
def Save_OBJ(SAVE_OBJ, SAVE_PATH):
    np.save(SAVE_PATH, SAVE_OBJ) 
            
def Load_OBJ(LOAD_PATH):
    return np.load(LOAD_PATH,allow_pickle='TRUE').item()     
    

if __name__ == "__main__":
    DIR_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\DataSet";
    SAVE_PATH = 'Valid_Stations3.npy'
    maximum_latitude = 40.88226
    minimum_latitude =  40.604017 
    maximum_longitude = -73.88145
    minimum_longitude = -74.03571
    # Uncomment or Comment any one of the following functions to use them   
    DoubleID_Same_Location(DIR_PATH)
    valid_dic = Check_Range_Location(DIR_PATH, maximum_latitude, minimum_latitude, maximum_longitude, minimum_longitude)
    Save_OBJ(valid_dic, SAVE_PATH) 
    
    