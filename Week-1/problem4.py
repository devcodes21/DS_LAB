x=int(input('Enter first number'))
y=int(input('Enter second number'))
z=int(input('Enter third number'))

if(x>y):
    if(x>z):
        print('%d is largest' %(x))
    else:
        print('%d is largest' %(z))
elif(y>x):
    if(y>z):
        print('%d is largest' %(y))
    else:
        print('%d is largest' %(z))