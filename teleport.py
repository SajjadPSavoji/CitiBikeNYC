from matplotlib.pyplot import ylabel
from utils import *
import copy 
from tqdm import tqdm
tqdm.pandas()

pd.set_option("display.max_rows", 10, "display.max_columns", 20)

def update_teleport(x):
    global bikes, teleports
    if x['bikeid'] in bikes:
        if bikes[x['bikeid']]["end station id"] != x["start station id"] and x["starttime"] > bikes[x["bikeid"]]["stoptime"]:
            # print("magic triip found")
            # print(x)
            # print(bikes[x["bikeid"]])
            # raise "finish thiis shit"
            # teleportation happend
            bikes[x["bikeid"]]["starttime"] = bikes[x["bikeid"]]["stoptime"]
            bikes[x["bikeid"]]["start station id"] = bikes[x["bikeid"]]["end station id"]
            bikes[x["bikeid"]]["start station name"] = bikes[x["bikeid"]]["end station name"]
            bikes[x["bikeid"]]["start station latitude"] = bikes[x["bikeid"]]["end station latitude"]
            bikes[x["bikeid"]]["start station longitude"] = bikes[x["bikeid"]]["end station longitude"]

            bikes[x["bikeid"]]["stoptime"] = x["starttime"]
            bikes[x["bikeid"]]["end station id"] = x["start station id"]
            bikes[x["bikeid"]]["end station name"] = x["start station name"]
            bikes[x["bikeid"]]["end station latitude"] = x["start station latitude"]
            bikes[x["bikeid"]]["end station longitude"] = x["start station longitude"]

            cols = ["starttime", "stoptime", "start station id", "end station id", "start station name",
             "end station name", "start station latitude", "end station latitude",
             "start station longitude", "end station longitude", "bikeid"]
            for col in cols:
                teleports[col].append(bikes[x["bikeid"]][col])
            # teleports.append(bikes[x["bikeid"]])

    bikes[x["bikeid"]] = x
#  select a csv file that has bikeid in its coloumns 202001
csv_path = "./Dataset/Preprocessed/202001-citibike-tripdata.csv.csv"
df = pd.read_csv(csv_path)
df = df.dropna()
df = preprocess_on_columns(df, "stoptime", str_to_datetime)
df = preprocess_on_columns(df, "starttime", str_to_datetime)
df = df.drop_duplicates()
df = df.sort_values(by=['starttime'])
print("done sorting")
bikes = {}
teleports = {"starttime": [], "stoptime":[], "start station id":[], "end station id":[], "start station name":[],
             "end station name":[], "start station latitude":[], "end station latitude":[],
             "start station longitude":[], "end station longitude":[], "bikeid": []}

# df.apply(lambda x: update_teleport(x), axis=1)
for index, row in tqdm(df.iterrows()):
    update_teleport(row)

df2 = pd.DataFrame.from_dict(teleports)
df2.to_csv('./Results/magic_trips.csv', index=False)
print("done")