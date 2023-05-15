import math
n = int (input("please enter a number "))
ans=0
if(n<=0):
    print("Invalid Input!")
    print("End of program.")
else:
    for i in range (1,n+1):
        if(i%2!=0):
            ans+=math.factorial(i)
        elif(i%2==0):
            ans-=math.factorial(i)
    print("Value of S is:",ans)
    print("End of program.")

