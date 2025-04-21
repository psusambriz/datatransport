import pandas as pd

# load csv
df = pd.read_csv("gypsy_id.csv", header=None)

# convert to array
ids_array = df[0].values
