# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 20:21:22 2022

@author: afadaei
"""
import numpy as np
import pandas as pd
import os


def Load_Valid_Stations(VALID_PATH):
    Valid_Stations = np.load(VALID_PATH ,allow_pickle='TRUE').item()
    return Valid_Stations 

def Measure_Trip(Trip, dataset, valid, Feature_Lat_S, Feature_Long_S, Feature_Lat_E, Feature_Long_E):
    for i in range(len(dataset)):
        if(((dataset[Feature_Lat_S][i], dataset[Feature_Long_S][i]) in valid) and ((dataset[Feature_Lat_E][i], dataset[Feature_Long_E][i]) in valid)):
            if((dataset[Feature_Lat_S][i], dataset[Feature_Long_S][i], dataset[Feature_Lat_E][i], dataset[Feature_Long_E][i]) in Trip):
                Trip[(dataset[Feature_Lat_S][i], dataset[Feature_Long_S][i], dataset[Feature_Lat_E][i], dataset[Feature_Long_E][i])] += 1
            else:
                Trip[(dataset[Feature_Lat_S][i], dataset[Feature_Long_S][i], dataset[Feature_Lat_E][i], dataset[Feature_Long_E][i])] = 1
    return Trip

def Count_Number_Trip(DIR_PATH, Valid_Stations):
    Trip = {}
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        #if year == "2020":
         #   break
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "start station latitude" in data:
                    Trip = Measure_Trip(Trip, data, Valid_Stations, "start station latitude", "start station longitude", "end station latitude", "end station longitude")            
                elif "Start Station Latitude" in data:
                    Trip = Measure_Trip(Trip, data, Valid_Stations, "Start Station Latitude", "Start Station Longitude", "End Station Latitude", "End Station Longitude")
                elif "start_lat" in data:
                    Trip = Measure_Trip(Trip, data, Valid_Stations, "start_lat", "start_lat", "end_lat", "end_lng")
                else:
                    print("No Data this year")
                print(year, month)
    return Trip
        
def Make_Trip_DataFrame(Trip_List):
    Start_Lat = [i[0] for i in Trip_List]
    Start_Long = [i[1] for i in Trip_List]
    End_Lat = [i[2] for i in Trip_List]
    End_Long = [i[3] for i in Trip_List]
    d = {"Start Latitude": Start_Lat, "Start Longitude": Start_Long, "End Latitude": End_Lat, "End Longitude": End_Long, "Number Trips": Trip_List.values()}
    df = pd.DataFrame(data=d)
    return df
        
def Save_CSV(SAVE_OBJ, SAVE_PATH):
    SAVE_OBJ.to_csv( SAVE_PATH)
    
def Save_OBJ(SAVE_OBJ, SAVE_PATH):
    np.save(SAVE_PATH, SAVE_OBJ) 

def Load_OBJ(LOAD_PATH):
    return np.load(LOAD_PATH,allow_pickle='TRUE').item()


if __name__ == "__main__":
    DIR_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\DataSet";
    VALID_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\Valid_Stations3.npy"
    SAVE_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\Trip.csv"
    TRIP_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\Trip.npy"
    # Uncomment or Comment any one of the following functions to use them   
    Valid_Stations = Load_Valid_Stations(VALID_PATH)
    Trip = Count_Number_Trip(DIR_PATH, Valid_Stations)
    DF = Make_Trip_DataFrame(Trip)
    Save_OBJ(Trip, TRIP_PATH)
    Save_CSV(DF, SAVE_PATH)
    
   
    
    