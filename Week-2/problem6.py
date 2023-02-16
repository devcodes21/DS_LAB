import pandas as pd
data=[['Dinesh',101,'Btech'],['Nithya',121,'Mtech'],['Raji',131,"Diploma pass"]]
df=pd.DataFrame(data,columns=['Name','height','Qualification'])
df.insert(3,"random Number",[32443234,5525,4534235],True)
print(df) 