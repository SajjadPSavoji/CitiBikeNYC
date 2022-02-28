from matplotlib import scale
from utils import *
pd.set_option("display.max_rows", 10, "display.max_columns", 20)
def hist_starting_time_hourly(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "started_at", str_to_datetime)
    df = preprocess_on_columns(df, "started_at", time_to_second, True, "started_at_time_sec")
    hist, binedges = scalable_histogram(df["started_at_time_sec"], verbose=True, bins=24*60)
    return hist, binedges
    
def hist_ending_time_hourly(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "ended_at", str_to_datetime)
    df = preprocess_on_columns(df, "ended_at", time_to_second, True, "ended_at_time_sec")
    hist, binedges = scalable_histogram(df["ended_at_time_sec"], verbose=True, bins=24*60)
    return hist, binedges

def hist_date_daily(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "started_at", str_to_datetime)
    df = preprocess_on_columns(df, "started_at", lambda x: x.day, True, "started_at_day")
    hist, binedges = scalable_histogram(df["started_at_day"], verbose=True, bins=62)
    return hist, binedges

def hist_date_weekday(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "started_at", str_to_datetime)
    df = preprocess_on_columns(df, "started_at", lambda x: x.weekday(), True, "started_at_weekday")
    hist, binedges = scalable_histogram(df["started_at_weekday"], verbose=True, bins=14)
    return hist, binedges

if __name__ == "__main__":
    file_path = "/home/savoji/Desktop/CitiBikeNYC/202201-citibike-tripdata.csv"
    # hist_date_daily(file_path)
    hist_date_weekday(file_path)
