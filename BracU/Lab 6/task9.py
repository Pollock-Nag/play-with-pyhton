import math
def area_circumference_generator(radius):
    area =  math.pi*radius**2
    circumference= 2*math.pi*radius

    return (area,circumference)


print(area_circumference_generator(2.5))
(area,circumference)= area_circumference_generator(2.5)
print("Area of the circle is",area,"and circumference is",circumference)