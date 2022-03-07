# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:29:48 2022

@author: afadaei
"""

import pandas as pd
import os

def updateDict(BicycleDictionary, datas, IDstring):
    for i in range(len(datas)):
        BicycleDictionary[datas[IDstring][i]] = 1
    return BicycleDictionary

def updateStartLocation(StartLocation, dataset, StartLat_string, StartLong_string):
    for i in range(len(dataset)):
        StartLocation[(dataset[StartLat_string][i], dataset[StartLong_string][i])] = 1
    return StartLocation
        
def updateEndLocation(EndLocation, dataset, EndLat_string, EndLong_string):
    temp = dataset[EndLat_string].isnull()
    for i in range(len(dataset)):
        if(temp[i] == True):
            continue
        EndLocation[(dataset[EndLat_string][i], dataset[EndLong_string][i])] = 1
    return EndLocation
 
def cal_number_trips(DIR_PATH, SAVE_PATH):
    num = []
    month_list = []
    years = []
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                years.append(year)
                month_list.append(month)
                num.append(len(data))
                print(month, len(data))
                del data
    d = {"Year": years, 'Months': month_list, 'number submission': num}
    df = pd.DataFrame(data=d)
    df.to_csv(SAVE_PATH, index=True)
    
def count_number_stations(DIR_PATH, SAVE_PATH):
    years = []
    months = []
    start_station = []
    ending_station = []
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "start station id" in data:
                    years.append(year)
                    months.append(month)
                    start_station.append(len(data["start station id"].value_counts(dropna=True)))
                    ending_station.append(len(data["end station id"].value_counts(dropna=True)))
                elif "Start Station ID" in data:
                    years.append(year)
                    months.append(month)
                    start_station.append(len(data["Start Station ID"].value_counts(dropna=True)))
                    ending_station.append(len(data["End Station ID"].value_counts(dropna=True)))
                elif "Start Station id" in data:
                    years.append(year)
                    months.append(month)
                    start_station.append(len(data["Start Station id"].value_counts(dropna=True)))
                    ending_station.append(len(data["End Station id"].value_counts(dropna=True)))
                elif "Start Station Id" in data:
                    years.append(year)
                    months.append(month)
                    start_station.append(len(data["Start Station Id"].value_counts(dropna=True)))
                    ending_station.append(len(data["End Station Id"].value_counts(dropna=True)))
                elif "start_station_id" in data:
                    years.append(year)
                    months.append(month)
                    start_station.append(len(data["start_station_id"].value_counts(dropna=True)))
                    ending_station.append(len(data["end_station_id"].value_counts(dropna=True)))
                else:
                    print("No Data this year")
                print(year, month)
    d = {"Year": years, "Months": month, 'Number Unique Start': start_station, 'Number Unique End': ending_station}
    df = pd.DataFrame(data=d)
    df.to_csv(SAVE_PATH, index=True)
        
def count_number_bikes(DIR_PATH, SAVE_PATH):
    Bike_id = []
    years = []
    months = []
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "Bikeid" in data:
                    years.append(year)
                    months.append(month)
                    Bike_id.append(len(data["Bikeid"].value_counts(dropna=True)))
                elif "bikeid" in data:
                    years.append(year)
                    months.append(month)
                    Bike_id.append(len(data["bikeid"].value_counts(dropna=True)))
                elif "Bike ID" in data:
                    years.append(year)
                    months.append(month)
                    Bike_id.append(len(data["Bike ID"].value_counts(dropna=True)))
                else:
                    print("No Data this year")
                print(year, month)
    d = {"Year": years, "Months": month, 'Number Unique Bikes': Bike_id}
    df = pd.DataFrame(data=d)
    df.to_csv(SAVE_PATH, index=True)
        
def count_cumulative_stations(DIR_PATH, SAVE_PATH):
    Start = {}
    End = {}
    CumulativeStart = []
    CumulativeEnd = []
    years = []
    months = []
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "start station latitude" in data:
                    updateStartLocation(Start, data, "start station latitude", "start station longitude")
                    updateEndLocation(End, data, "end station latitude", "end station longitude")
                elif "Start Station Latitude" in data:
                    updateStartLocation(Start, data, "Start Station Latitude", "Start Station Longitude")
                    updateEndLocation(End, data, "End Station Latitude", "End Station Longitude")
                elif "start_lat" in data:           
                    updateStartLocation(Start, data, "start_lat", "start_lat")
                    updateEndLocation(End, data, "end_lat", "end_lng")
                else:
                    print("No Data this year")
                years.append(year)
                months.append(month)
                CumulativeStart.append(len(Start))
                CumulativeEnd.append(len(End))
                print(year, month)
    d = {"Year": years, "Months": month, "Cumulative Starting Station": CumulativeStart, "Cumulative Ending Station": CumulativeEnd}
    df = pd.DataFrame(data=d)
    df.to_csv(SAVE_PATH, index=True)
    
def count_cumulative_bikes(DIR_PATH, SAVE_PATH):
    Byedict = {}
    CumulativeBike = []
    years = []
    months = []
    for year in os.listdir(DIR_PATH):
        new_dir = DIR_PATH + "\\" + year
        for month in os.listdir(new_dir):
            FolderPath = new_dir + "\\" + month
            if(month == "ZipFile"):
                continue
            for item in os.listdir(FolderPath):
                DataSetPath = FolderPath + "\\" + item
                data = pd.read_csv(DataSetPath)
                if "Bikeid" in data:
                    Byedict = updateDict(Byedict, data, "Bikeid")
                elif "bikeid" in data:
                    Byedict = updateDict(Byedict, data, "bikeid")
                elif "Bike ID" in data:
                    Byedict = updateDict(Byedict, data, "Bike ID")
                else:
                    print("No Data this year")
                years.append(year)
                months.append(month)
                CumulativeBike.append(len(Byedict))
                print(year, month)
    d = {"Year": years, "Months": month,'Bike Number Cumulative': CumulativeBike}
    df = pd.DataFrame(data=d)
    df.to_csv(SAVE_PATH, index=True)

        
if __name__ == "__main__":
    DIR_PATH = r"D:\Amin\Education\Course\Data Analytics and Visualization (Winter 2021-2022)\Project\DataSet";
    # Uncomment any one of the following functions to use them   
 
    #cal_number_trips(DIR_PATH, 'NumSub.csv')
    #(DIR_PATH, 'StartEndBike.csv')
    #ount_number_bikes(DIR_PATH, 'NumBike.csv')
    #count_cumulative_stations(DIR_PATH, 'StationCumulative.csv')
    count_cumulative_bikes(DIR_PATH, 'BikeCumulative.csv')
