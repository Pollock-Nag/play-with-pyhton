"""
Write a Python code for the following:

Ask the user to enter a Number, N
Display the summation of multiples of 7 up to that number (from 1 to N inclusive)
"""

num = int(input("please input a number "))
sum=0
for i in range (1,num+1):
    if(i%7==0):
        sum+=i

print(sum)

