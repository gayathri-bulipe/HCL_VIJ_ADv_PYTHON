import pandas as pd
#import numpy as np
data1=pd.read_excel("..//data/cmpdata3.xlsx",sheet_name="Sheet1")
data2=pd.read_excel("..//data/cmpdata4.xlsx",sheet_name="Sheet2")
print(data1)
print(data2)
#print(data1.compare(data2))
#data1['Price-1']=np.where(data1['Price']==data2['Price'],0,data2['Price']-data1['Price'])
#print(data1)


