import pandas as pd
data=[['Dinesh',101,'Btech'],['Nithya',121,'Mtech'],['Raji',131,"Diploma pass"]]
df=pd.DataFrame(data,columns=['Name','height','Qualification'])
print(df)
list=[1,2,3]
df['address']=list
print(df)