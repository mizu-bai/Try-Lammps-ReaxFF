import pandas as pd

df = pd.read_csv("CH4_O2.lammpsstrj.csv", sep=" ")
df.drop(labels=["Unnamed: 0"], axis=1, inplace=True)
df["type"].replace(2, 4, inplace=True) # 2 -> 4
df["type"].replace(1, 2, inplace=True) # 1 -> 2
df["type"].replace(4, 1, inplace=True) # 4 -> 1
df.insert(2, "zero", 1.0)
df.to_csv("CH4_O2_processed.lammpsstrj.csv", index=False, sep=" ")
