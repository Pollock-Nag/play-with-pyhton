n = int(input("Please give number from 1 to 9 "))
if(n==1):
    print(n)
else:
    for i in range (1,n+1):
        print(i,end="")
    for i in range(n-1,0,-1):
        print(i, end="")
