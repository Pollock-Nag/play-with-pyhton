def calculator(operation,num1,num2):
    result=0.0
    if (operation=="+"):
        result=num1+num2
    elif (operation=="-"):
        result=num1-num2
    elif (operation=="*"):
        result=num1*num2
    elif (operation=="/"):
        result=num1/num2
    return result



operation=input("Please input + or - or * or / ")
num1= float(input())
num2= float(input())
print(calculator(operation,num1,num2))
