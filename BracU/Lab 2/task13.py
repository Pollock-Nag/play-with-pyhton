num= int(input("please enter a number "))
temp=num
count=0
while(num!=0):
    num=num//10
    count+=1

x=10**(count-1)
while(x!=0):
    if(x==1):
        print(temp//x,end=" ")
    else:
        print(temp//x,end=", ")

    temp=temp%x
    x=x//10

