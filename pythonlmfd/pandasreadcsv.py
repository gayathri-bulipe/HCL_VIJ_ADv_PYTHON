import pandas as pd
data=pd.read_csv("..//data/tips.csv")
#print(data.isna().any())
#print(data.isna().sum())
tips_male_fm=data.filter(['tip','sex'])
#print(tips_male_fm.groupby('sex').sum())
#print(tips_male_fm.sex.value_counts())
#print(tips_male_fm.sex.value_counts(normalize=True))
#print(pd.crosstab(index=data['sex'],columns=data['smoker']))
#print(pd.crosstab(data['day'],columns=data['tip']))
#day_wise=data.filter(['tip','day'])
#print(day_wise.groupby('day').sum())
#print(data.info())
print(data.describe())
#print(data.head(3))