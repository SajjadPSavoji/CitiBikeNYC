from matplotlib.pyplot import ylabel
from utils import *
pd.set_option("display.max_rows", 10, "display.max_columns", 20)
def time_diff_in_hour(dt_1, dt_2):
    return float((dt_2 - dt_1).total_seconds())/(60*60)

def hist_starting_time_hourly(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "starttime", str_to_datetime)
    df = preprocess_on_columns(df, "starttime", time_to_second, True, "started_at_time_sec")
    hist, binedges = scalable_histogram(df["started_at_time_sec"], verbose=False, bins=np.linspace(0, 24, 24*60))
    return hist, binedges
    
def hist_ending_time_hourly(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "stoptime", str_to_datetime)
    df = preprocess_on_columns(df, "stoptime", time_to_second, True, "ended_at_time_sec")
    hist, binedges = scalable_histogram(df["ended_at_time_sec"], verbose=False, bins=np.linspace(0, 24, 24*60))
    return hist, binedges

def hist_date_daily(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "starttime", str_to_datetime)
    df = preprocess_on_columns(df, "starttime", lambda x: x.day, True, "started_at_day")
    hist, binedges = scalable_histogram(df["started_at_day"], verbose=False, bins=32)
    return hist, binedges

def hist_date_weekday(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "starttime", str_to_datetime)
    df = preprocess_on_columns(df, "starttime", lambda x: x.weekday(), True, "started_at_weekday")
    hist, binedges = scalable_histogram(df["started_at_weekday"], verbose=False, bins=8)
    return hist, binedges

def hist_trip_duration(file_path):
    df = read_csv(file_path)
    df = df.dropna()
    df = preprocess_on_columns(df, "stoptime", str_to_datetime)
    df = preprocess_on_columns(df, "starttime", str_to_datetime)

    df["trip_duration"] = df.apply(lambda x: time_diff_in_hour(x["starttime"], x["stoptime"]), axis=1)
    hist, binedges = scalable_histogram(df["trip_duration"][df['trip_duration'] < 24*7], verbose=False, bins = np.linspace(0, 24*7, 24*7*2))
    # hist, binedges = scalable_histogram(df["trip_duration"], verbose=False, bins=1000)
    return hist, binedges

def plot_distributed_hist(results, xlabel, ylabel, title, save_path=None):
    '''
    assuming that the bin edges are the same for all histograms
    '''
    binedges = results[0][1]
    hists = np.zeros_like(results[0][0])
    for h, be in results:
        hists += h
    plt.plot(binedges[1:], hists)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    if save_path is not None:
        plt.savefig(save_path)
    else: plt.show()
    plt.close()
    return hists, binedges
    
    
if __name__ == "__main__":
    # ------------------------------------------------------------------------------------
    # dataset_path = "./Dataset/Preprocessed/"
    # csvs_path = get_csvs_path(dataset_path)
    # results = execute_on_dataset(csvs_path, hist_starting_time_hourly)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of start time", save_path="./Results/hist_starttime.png")
    # results = execute_on_dataset(csvs_path, hist_ending_time_hourly)
    # hists_end, bins_end = plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of ending time", save_path="./Results/hist_endtime.png")
    # plt.plot(bins_str[1:], hists_str, label="start")
    # plt.plot(bins_str[1:], hists_end, label="end")
    # plt.xlabel("time")
    # plt.ylabel("trip count")
    # plt.title("trip histogram")
    # plt.grid()
    # plt.legend()
    # plt.savefig("./Results/hist_str_end.png")
    # plt.close()
    # ---------------------------------------------------------------------------------------
    # dataset_path = "./Dataset/Preprocessed/"
    # csvs_path = get_csvs_path(dataset_path)
    # results = execute_on_dataset(csvs_path, hist_date_daily)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="day", ylabel="count", title="histogram of start time", save_path="./Results/hist_starttime_daily.png")
    # ---------------------------------------------------------------------------------------
    # dataset_path = "./Dataset/Preprocessed/"
    # csvs_path = get_csvs_path(dataset_path)
    # results = execute_on_dataset(csvs_path, hist_date_weekday)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="week day", ylabel="count", title="histogram of start time", save_path="./Results/hist_starttime_weekday.png")
    # -----------------------------------------------------------------------------------------
    # dataset_path = "./Dataset/Preprocessed/"
    # csvs_path = get_csvs_path(dataset_path)
    # results = execute_on_dataset(csvs_path, hist_trip_duration)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of trip duration", save_path="./Results/hist_duration.png")
    # -----------------------------------------------------------------------------------------
    # hist_starting_time_hourly(file_path)
    # hist_ending_time_hourly(file_path)
    # hist_date_daily(file_path)
    # hist_date_weekday(file_path)
    # hist_trip_duration(file_path)

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    # ------------------------------------------------------------------------------------
    # csvs_path = ["Results/magic_trips.csv"]
    # results = execute_on_dataset(csvs_path, hist_starting_time_hourly)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of start time", save_path="./Results/magic_hist_starttime.png")
    # results = execute_on_dataset(csvs_path, hist_ending_time_hourly)
    # hists_end, bins_end = plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of ending time", save_path="./Results/magic_hist_endtime.png")
    # plt.plot(bins_str[1:], hists_str, label="start")
    # plt.plot(bins_str[1:], hists_end, label="end")
    # plt.xlabel("time")
    # plt.ylabel("trip count")
    # plt.title("trip histogram")
    # plt.grid()
    # plt.legend()
    # plt.savefig("./Results/magic_hist_str_end.png")
    # plt.close()
    # # --------------------------------------------------------------------------------------
    # csvs_path = ["Results/magic_trips.csv"]
    # results = execute_on_dataset(csvs_path, hist_date_daily)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="day", ylabel="count", title="histogram of start time", save_path="./Results/magic_hist_starttime_daily.png")
    # ---------------------------------------------------------------------------------------
    # csvs_path = ["Results/magic_trips.csv"]
    # results = execute_on_dataset(csvs_path, hist_date_weekday)
    # hists_str, bins_str = plot_distributed_hist(results, xlabel="week day", ylabel="count", title="histogram of start time", save_path="./Results/magic_hist_starttime_weekday.png")
    # -----------------------------------------------------------------------------------------
    csvs_path = ["Results/magic_trips.csv"]
    results = execute_on_dataset(csvs_path, hist_trip_duration)
    hists_str, bins_str = plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of trip duration", save_path="./Results/magic_hist_duration.png")
    # -----------------------------------------------------------------------------------------
    # hist_starting_time_hourly(file_path)
    # hist_ending_time_hourly(file_path)
    # hist_date_daily(file_path)
    # hist_date_weekday(file_path)
    # hist_trip_duration(file_path)