
import pandas as pd
import numpy as np
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)
        return self.df
    def total_df(self):
        self.df['total']=self.df.iloc[:,2:].sum(axis=1)
        return self.df
    def avg_df(self):
        self.df['avg']=self.df['total']/5
        return self.df

csv1=Readcsv()
df=pd.read_csv("..//data/readfile.csv")
print(csv1.create_df(df))
print(csv1.total_df())
print(csv1.avg_df())