"""
Write Python code of a program that reads an integer,
and prints the integer if it is a multiple of 2 and 5.
"""

num = int(input())
if(num%2==0 and num%5==0):
    print(num)
else:
    print("Not multiple of 2 and 5 both")