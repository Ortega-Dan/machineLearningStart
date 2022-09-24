import pandas as pd

data = pd.read_csv("shoes/shoe-size-samples.csv")

# print(data[["sex","shoe_size"]].groupby("sex").median())


print(data.groupby("sex").median(numeric_only=True))


