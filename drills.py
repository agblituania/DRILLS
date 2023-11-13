import pandas as pd
import random as r


df = pd.read_csv("table1.csv").dropna()                                             #import
df.insert(0, "ID" , [i for i in range(len(df.index))])                              #add ID
df["Date"] = "META-" + df["Date"]                                                   #modify date
df.insert(2, "Dummy" , [r.randint(0,1) for _ in range(len(df.index))])              #dummy
print(df)

df.to_csv("table2.csv")                                                             #last step table 2