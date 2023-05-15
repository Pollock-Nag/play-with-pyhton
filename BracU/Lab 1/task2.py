"""
Write Python code of a program that reads the radius of a circle and prints its circumference and area.
"""

import math 

#taking input from the user, then converting it to float.
#Since radius can be a floating point value

radius  = float(input("please enter the radius value:"))


# squares can be made using this 3 ways, as written in hints.
# all 3 ways, generates the same result of area

area = math.pi * radius **2
print("Area is:", area)

#==============================================================
# TODO
# calculate circumference

circumference = 2*math.pi*radius
print("Circumference is:", circumference)

#==============================================================