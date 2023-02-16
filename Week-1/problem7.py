abcd=(1,2,3,4,5,6,7,8,9,10)
efgh=()
for i in range(len(abcd)):
    if(abcd[i]%2==0):
        efgh=efgh+(abcd[i],)
        # print(abcd[i])
print(efgh)