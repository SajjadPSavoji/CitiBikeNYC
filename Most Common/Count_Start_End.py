# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:50:38 2022

@author: afadaei
"""
import numpy as np
import pandas as pd
import os


def Load_Valid_Stations(VALID_PATH):
    Valid_Stations = np.load(VALID_PATH ,allow_pickle='TRUE').item()
    return Valid_Stations 
   
def update(valid, Station, dataset, Feature_Lat, Feature_Long):
    for i in range(len(dataset)):
        if((dataset[Feature_Lat][i], dataset[Feature_Long][i]) in valid):
            Station[(dataset[Feature_Lat][i], dataset[Feature_Long][i])] += 1
    return Station

def Count_Start_End(DIR_PATH, Valid_Stations):
    Start = dict.fromkeys(Valid_Stations, 0)
    End = dict.fromkeys(Valid_Stations, 0)
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
                    Start = update(Valid_Stations, Start, data, "start station latitude", "start station longitude")
                    End = update(Valid_Stations, End, data, "end station latitude", "end station longitude")
                elif "Start Station Latitude" in data:
                    Start = update(Valid_Stations, Start, data, "Start Station Latitude", "Start Station Longitude")
                    End = update(Valid_Stations, End, data, "End Station Latitude", "End Station Longitude")
                elif "start_lat" in data:
                    Start = update(Valid_Stations, Start, data, "start_lat", "start_lat")
                    End = update(Valid_Stations, End, data, "end_lat", "end_lng")
                else:
                    print("No Data this year")
                print(year, month)
    return Start, End

def Make_StartEnd_DataFrame(Starting_Stations, Ending_Stations):
    Start_Lat = [i[0] for i in Starting_Stations]
    Start_Long = [i[1] for i in Starting_Stations]
    #The lines below are not needed since both Starting_Station and Ending_Station are sorted in the same way
    #End_Lat = [i[0] for i in Ending_Stations]
    #End_Long = [i[1] for i in Ending_Stations]
    d = {"Start Latitude": Start_Lat, "Start Longitude": Start_Long, "Number Out": Starting_Stations.values(), "Number In": Ending_Stations.values()}
    df = pd.DataFrame(data=d)
    return df
            
def Save_CSV(SAVE_OBJ, SAVE_PATH):
    SAVE_OBJ.to_csv(SAVE_PATH)  
   
def Save_OBJ(SAVE_OBJ, SAVE_PATH):
    np.save(SAVE_PATH, SAVE_OBJ)      

def Load_OBJ(LOAD_PATH):
    return np.load(LOAD_PATH,allow_pickle='TRUE').item()    

if __name__ == "__main__":
    DIR_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\DataSet";
    VALID_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\Valid_Stations3.npy"
    SAVE_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\Start_End.csv"
    START_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\Start.npy"
    END_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\Code\End.npy"
    # Uncomment or Comment any one of the following functions to use them   
    Valid_Stations = Load_Valid_Stations(VALID_PATH)
    Start, End = Count_Start_End(DIR_PATH, Valid_Stations)
    DF = Make_StartEnd_DataFrame(Start, End)
    Save_OBJ(Start, START_PATH)
    Save_OBJ(End, END_PATH)
    Save_CSV(DF, SAVE_PATH)
    
