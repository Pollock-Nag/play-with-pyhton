"""
Write Python code of a program that reads two numbers from the user.
Your program should then print "First is greater" if the first number is greater,
"Second is greater" if the second number is greater, and "The numbers are equal" otherwise
"""

number1 = int(input())
number2 = int(input())

if(number1>number2):
    print("First is greater")
elif(number2>number1):
    print("Second is greater")
else:
    print("The numbers are equal")
