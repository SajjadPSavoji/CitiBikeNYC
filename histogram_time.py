from matplotlib.pyplot import ylabel
from utils import *
pd.set_option("display.max_rows", 10, "display.max_columns", 20)
def time_diff_in_seconds(dt_1, dt_2):
    return int((dt_2 - dt_1).total_seconds())

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
    df = preprocess_on_columns(df, "started_at", str_to_datetime)
    df = preprocess_on_columns(df, "started_at", lambda x: x.day, True, "started_at_day")
    hist, binedges = scalable_histogram(df["started_at_day"], verbose=False, bins=62)
    return hist, binedges

def hist_date_weekday(file_path):
    df = read_csv(file_path)
    df = preprocess_on_columns(df, "started_at", str_to_datetime)
    df = preprocess_on_columns(df, "started_at", lambda x: x.weekday(), True, "started_at_weekday")
    hist, binedges = scalable_histogram(df["started_at_weekday"], verbose=False, bins=14)
    return hist, binedges

def hist_trip_duration(file_path):
    df = read_csv(file_path)
    df = df.dropna()
    df = preprocess_on_columns(df, "ended_at", str_to_datetime)
    df = preprocess_on_columns(df, "started_at", str_to_datetime)

    df["trip_duration"] = df.apply(lambda x: time_diff_in_seconds(x["started_at"], x["ended_at"]), axis=1)
    hist, binedges = scalable_histogram(df["trip_duration"][df['trip_duration'] < 24*60*60], verbose=True, bins = 10)
    # print(hist)
    # print(binedges)
    # plt.hist(hist)
    # return hist, binedges

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
    
    
if __name__ == "__main__":
    dataset_path = "./Dataset/Preprocessed/"
    csvs_path = get_csvs_path(dataset_path)
    results = execute_on_dataset(csvs_path, hist_starting_time_hourly)
    plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of start time", save_path="./Results/hist_starttime.png")
    results = execute_on_dataset(csvs_path, hist_ending_time_hourly)
    plot_distributed_hist(results, xlabel="hour", ylabel="count", title="histogram of ending ti me", save_path="./Results/hist_endtime.png")

    # hist_starting_time_hourly(file_path)
    # hist_ending_time_hourly(file_path)
    # hist_date_daily(file_path)
    # hist_date_weekday(file_path)
    # hist_trip_duration(file_path)
