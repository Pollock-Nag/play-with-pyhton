"""
Write a Python code of a program that asks the user to enter ten numbers then display the total and the average of ONLY the odd numbers among those ten numbers.
"""

sum=0
count=0
for i in range (0,10):
    num=int(input())
    if(num%2!=0):
        count+=1
        sum+=num
print("Total is",sum,"and Average is",sum/count)