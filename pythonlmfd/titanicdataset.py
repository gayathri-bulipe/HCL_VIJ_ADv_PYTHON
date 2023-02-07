import pandas as pd
import numpy as np
data1=pd.read_csv("..//data/tested.csv")
#print(data1.shape)#gives rows & cols
#print(data1.isna().any)
#print(data1.isna().sum())
#data1.drop(['Cabin'],axis=1,inplace=True) cabin col is deleted here
#print(data1.isna().sum())
#data1.fillna(method='ffill',inplace=True)
#print(data1['Embarked'])
print(pd.crosstab(index=data1['Sex'],columns=data1['Survived']))
#print(data1.groupby(['Sex','Survived'])['Survived'].count())
#print(data1.isna().sum())
#print(data1)
#print(pd.pivot_table(data1,index=['Sex','Age'],aggfunc=np.sum))
#print(data1.sort_values(by=['Pclass'],ascending=False))
data1['Survived']=data1["Survived"].apply(lambda val:'Yes' if val==1 else 'No')
print(data1)

