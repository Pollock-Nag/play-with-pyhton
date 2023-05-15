def factorial (num):
    ans=1
    for i in range(0, num):
        ans *= num
        num -= 1
    return ans

num = int(input("please input a number "))
result=0
if(num<0):
    print("Invalid Input")
else:
    for i in range (1,num+1,1):
        if(i%2!=0):
            result+=factorial(i)
        else:
            result-=factorial(i)
    print(result)