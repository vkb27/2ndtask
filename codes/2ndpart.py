import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split
import seaborn as sn
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

df=pd.read_csv('task2.csv')
# print(df.isnull())
df.fillna(0)

mapping = {'web': 1, 'gender': 2,"university":3,"mobile":4}

df=df.replace({"Segment type":mapping})

mapping1 = {'No':1, 'Yes':2 ,"I don't use Tinder":3}
df=df.replace({"Answer":mapping1})

x=df['Segment Description'].value_counts()
item_type_mapping={}
item_list=x.index
for i in range(0,len(item_list)):
    item_type_mapping[item_list[i]]=i

df['Segment Description']=df['Segment Description'].map(lambda x:item_type_mapping[x]) 


df1=df.iloc[:,0:6]
# df1=df1.drop(['Segment Description'], axis = 1)
df2=df.iloc[:,6]

# print(df2)
x_train, x_test, y_train, y_test = train_test_split(df1,df2,test_size = 0.3)

model = KNeighborsClassifier(n_neighbors = 1)
model.fit(x_train, y_train)
predictions = model.predict(x_test)
# print(predictions)

print(classification_report(y_test, predictions))