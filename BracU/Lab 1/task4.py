"""
Write Python code of a program that reads two numbers,
subtracts the smaller number from the larger one,
and prints the result.
"""
number1 = int(input())
number2 = int(input())
max=0
min=0
if(number1>number2):
    max=number1
    min=number2
elif(number2>number1):
    max=number2
    min=number1
else:
    max=number1
    min=number2

print(max-min)