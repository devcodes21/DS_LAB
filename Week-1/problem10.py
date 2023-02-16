abcd=[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6]
a=len(abcd)
for i in abcd:
    if(abcd[i]%2==0):
        print(abcd[i])
        abcd.remove(abcd[i])
        # a=a-1
print(abcd)