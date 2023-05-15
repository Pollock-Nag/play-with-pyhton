"""
Write a Python code that will calculate the value of y if the expression of y is as follows (n is the input):

y=12−22+32−42+52.........+n2
"""
n = int(input("please enter value of n "))
ans=0
for i in range(0,n+1):
    if(i%2==0):
        ans-=i**2
    else:
        ans+=i**2
print(ans)
