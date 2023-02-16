import pandas as pd;
new = {'name': ['ram', 'diya', 'chandan','james','alice'] }
df1 = pd.DataFrame.from_dict(new)
print(df1)

new2 = {'Math': [80, 90.0, 77.5,87.5,86.5], 'Physics':[81.0,94,74.5,83.5,82.5],
        'Chemistry': [91.5, 86.5, 85.5, 90,91],'Biology': [82.5, 83.5, 84.5,85,93]} 
df2 = pd.DataFrame.from_dict(new2)
print(df2)


result=df1.join(df2)
print(result)

result["Sum"] = df2.sum(numeric_only=True,axis=1)
print(result)