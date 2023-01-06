import pandas as pd
from tqdm import tqdm
import numpy as np

# df = pd.read_csv("lastfm.csv", usecols= ["user_id",	"item_id",	"timestamp",	"state_label",	"comma_separated_list_of_features",])
df = pd.DataFrame(columns= ["user_id",	"item_id",	"timestamp",	"state_label",	"comma_separated_list_of_features"])

#first u have to open  the file and seperate every line like below:

f = open('data/CollegeMsg.txt', "r")
lines = f.readlines()
f.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
  lines[index] = line.strip()

# parse and enter data row by row

i = 0  
for line in tqdm(lines):
  user, item, ts = line.split(" ")
  df.loc[i] = [int(user), int(item), float(ts), 0, 0.0]
  i =i+1

# setting initial timestamp to 0.0
df.loc[:, "timestamp"] = df.loc[:, "timestamp"] - df.loc[0, "timestamp"]

# converting to correct datatypes

df = df.astype({"user_id": np.int64, "item_id": np.int64, "state_label": np.int64, "comma_separated_list_of_features": np.float64})

# save csv file

df.to_csv('data/CollegeMsg.csv', index=False)  