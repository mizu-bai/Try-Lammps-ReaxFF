import pandas as pd
import re
import os
from io import StringIO

# read file
file_name = "my_species copy.out"
with open(file_name, "r") as f_o:
    species = f_o.read()

# processing out file
print("Processing out file...")
# split
res = re.split("# ", species)
res.pop(0)
# text -> dataframe
df_list = list()
n = len(res)

for i in range(n):
    if i % int(n / 50) == 0:
        print(f"processing {i}/{n}")
    
    part = res[i]
    part = re.sub(r"[\t ]+", " ", part)
    part = re.sub(r"( \n)+", r"\n", part)
    tmp_io = StringIO(part)
    df_tmp = pd.read_csv(tmp_io, sep=r" ")
    df_list.append(df_tmp)

f_o.close()

# concat dataframes
print("Concatting dataframes...")
df_all = pd.concat(df_list, axis=0)
df_all.fillna(0.0, inplace=True)
# print(df_all)

# write to file
print("Writing to file...")
df_all.to_csv("my_species_processed.csv", index=False)

# done
print("Done!")
