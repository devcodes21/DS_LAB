# boppy=[]
poppy=[1,2,3,4,5,6,-1,+2,-3,-4,-5,-6]
count1=0
count2=0
for i in range(len(poppy)):
    if(poppy[i]<0):
        count1=count1+1
    else:
        count2=count2+1
print("Count of positive is:-")
print(count2)
print("Count of negative is:-")
print(count1)
