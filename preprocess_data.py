from matplotlib.pyplot import axis
from utils import *
def unify_features(csv_path):

    file_name = os.path.basename(csv_path)
    file_date = file_name.split("-")[0] 
    file_year = int(file_date[0:4])
    file_date = int(file_date)
      
    col_2020 = ['starttime', 'stoptime', 'start station id',
           'start station name', 'start station latitude',
           'start station longitude', 'end station id', 'end station name',
           'end station latitude', 'end station longitude', 'bikeid']

    col_2021 = ['bikeid', 'starttime', 'stoptime', 'start station name',
            'start station id', 'end station name', 'end station id',
            'start station latitude', 'start station longitude',
            'end station latitude', 'end station longitude']

    data = pd.read_csv(csv_path, low_memory=False)

    if file_date <= 202101:
        cols_to_drop = ["birth year", "gender", "tripduration", "usertype"]
        for col in cols_to_drop:
            data = data.drop(col, axis=1)
        data.columns = col_2020
    
    elif file_date > 202101:
        cols_to_drop = ["member_casual", "rideable_type"]
        for col in cols_to_drop:
            data = data.drop(col, axis=1)
        data.columns = col_2021

    ## Export
    data.to_csv(f"{csv_path}.csv", index = False)

if __name__ == "__main__":
    dataset_path = "./Dataset"
    csvs_path = get_csvs_path(dataset_path)
    execute_on_dataset(csvs_path, unify_features)