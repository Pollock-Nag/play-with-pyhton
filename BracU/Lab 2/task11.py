num = int(input("please enter a number "))

while(num!=0):
    digit=num%10
    if(digit==num):
        print(digit,end="")
    else:
        print(digit,end=", ")
    num//=10