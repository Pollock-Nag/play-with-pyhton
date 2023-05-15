"""
Write python program, which prints the following sequences of values in loops:

a) 24, 18, 12, 6, 0, -6
b) -10, -5, 0, 5, 10, 15, 20
c) 18, 27, 36, 45, 54, 63
d) 18, -27, 36, -45, 54, -63
"""

counter = 24

while(counter>=-6):

    if counter==-6:
        print(counter,end=" ")
    else:
        print(counter, end=", ")
    counter -= 6