import pandas as pd
d={'Team':["India","Austrlia","pakistan","Srilanka","england"],
   'rank':[1,2,3,4,5,6]
   }
Team=["India","Austrlia","pakistan","srilanka","england"]
s=pd.Series(Team,index=['a','b','c','d','e'])
print(s)
