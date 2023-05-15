"""
Write Python code of a program that reads an integer,
and prints the integer if it is NOT a multiple of 2 OR NOT a multiple of 5.
"""

num = int(input())

if(num%2!=0 or num%5!=0):
    print(num)
else:
    print("No")
