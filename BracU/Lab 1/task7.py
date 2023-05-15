"""
Write Python code of a program that reads an integer,
and prints the integer it is a multiple of either 2 or 5 but not both.
"""

num = int(input())
if(num%2==0):
    if(num%5==0):
        print("multiple of 2 and 5 both")
    else:
        print(num)
elif(num%5==0):
    if(num%2==0):
        print("multiple of 2 and 5 both")
    else:
        print(num)

else:
    print("Not a multiple")
