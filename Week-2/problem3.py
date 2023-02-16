list=[1,2,3,-7,-8,-9,1,2,3,4,-7,-5]
n=len(list)
i=0
positive_count=0
negative_count=0
while(i<n):
    if(list[i]<0):
        negative_count=negative_count+1
    elif(list[i]>0):
        positive_count=positive_count+1
    i=i+1
print("Negative count is:-",negative_count)
print("Positive count is:-",positive_count)