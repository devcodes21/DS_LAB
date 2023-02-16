list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n=len(list)
i=0
while(i<len(list)):
    if(list[i]%2==0):
        list.remove(list[i])
    i=i+1
print(list)