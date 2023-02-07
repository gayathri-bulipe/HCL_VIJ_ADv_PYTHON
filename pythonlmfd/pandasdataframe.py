import pandas as pd
d={'Team':["India","Austrlia","pakistan","Srilanka","england"],
   'Rank':[1,2,3,4,5],
   'Winper':['60%','55%','45%','35%','48%']
   }
df=pd.DataFrame(d)
df.rename(columns={'Rank':'Ranking'},inplace=True)
#print(df.iloc[[0,1],:])
print(df.iloc[:3,-1])
