import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
df=pd.read_csv('task1.csv')
# df1=df.loc[df['sex'] =="F"]
# df2=df.loc[df['sex'] == "M"]
# df1=df1[['G3','studytime']].loc[df['address']=="U"]
# df2=df2[['G3','studytime']].loc[df['address']=="R"]
# print(df1.mean())
# print(df2.mean())

# df1=df.sort_values(("G3"),ascending=False)
# print(df1.iloc[0])
# df1=df.loc[df['Dalc'] ==1]
# df2=df.loc[df['Dalc'] ==2]
# df3=df.loc[df['Dalc'] ==3]
# df4=df.loc[df['Dalc'] ==4]
# df5=df.loc[df['Dalc'] ==5]
# print(df1[["G3"]].mean())
# print(df2[["G3"]].mean())
# print(df3[["G3"]].mean())
# print(df4[["G3"]].mean())
# print(df5[["G3"]].mean())

# df1=(df.loc[df["G3"]>=15])
# df2=df1.loc[df["higher"]=="yes"]
# df3=df.loc[df["higher"]=="yes"]
# print(len(df.index))
# print(len(df2.index))
# print(len(df3.index))

# df1=df.loc[df['romantic'] =="yes"]
# df2=df.loc[df['romantic'] == "no"]

# print(df1["G3"].mean()-df2["G3"].mean())
# print(df2["G3"].mean())

# df1=df.loc[df['sex'] =="F"]
# df2=df.loc[df['sex'] == "M"]
# df1f=df1.loc[df['activities']=="yes"]
# df2m=df2.loc[df['activities']=="yes"]
# print(len(df1.index))
# print(len(df1f.index))
# print(len(df2.index))
# print(len(df2m.index))

df1=df[["Dalc","Walc","famrel"]]
# print(df1.iloc[0])

df1["TotalAlc"]=df1["Dalc"]+df1["Walc"]
# print(df1.corr(method='pearson'))
print(df1)