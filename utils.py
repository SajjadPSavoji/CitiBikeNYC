import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

def read_csv(file_path):
    return pd.read_csv(file_path, low_memory=False)

def scalable_histogram(data, verbose=False, bins=31):
    hist, binedges = np.histogram(data, bins=bins)
    if verbose:
        plt.plot(binedges[:-1], hist)
        plt.show()
        plt.grid()
    return hist, binedges

def preprocess_on_columns(df, col_name, func, new_col=False, new_col_name=None):
    prep_series = df[col_name].apply(lambda x: func(x))
    if new_col:
        df[new_col_name] = prep_series
    else:
        df[col_name] = prep_series

    return df

def str_to_datetime(str_dt):
    temp = str_dt.split(" ")
    date_str , time_str = temp[0], temp[1]
    temp_date = list(map(float, date_str.split("-")))
    temp_time = list(map(float, time_str.split(":")))
    temp_date = [int(i) for i in temp_date]
    temp_time = [int(i) for i in temp_time]
    year , month, day = temp_date[0], temp_date[1], temp_date[2]
    hour, minute, second = temp_time[0], temp_time[1], temp_time[2]
    return dt.datetime(year, month, day, hour, minute, second)

def time_to_second(dt_i):
    return (dt_i.hour + dt_i.minute/60 + dt_i.second/3600) 

def execute_on_dataset(csvs_path, func):
    results = []
    for csv_path in tqdm(csvs_path):
        res = func(csv_path)
        results.append(res)
    return results

def get_csvs_path(dataset_path):
    csvs_name = sorted(os.listdir(dataset_path), key=str.lower)
    # sorting the files will ensure that the cronological order of resutls are saved
    csvs_path = [os.path.join(dataset_path, i) for i in csvs_name]
    return csvs_path