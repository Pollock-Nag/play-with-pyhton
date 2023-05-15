"""
Write Python code of a program that reads an integer,
and prints the integer if it is a multiple of NEITHER 2 NOR 5.
"""

num = int(input())
if(num%2==0 or num%5==0):
    print("No")
else:
    print(num)