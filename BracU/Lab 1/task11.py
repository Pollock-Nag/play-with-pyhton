'''
Write Python code of a program that reads a student’s mark for a single subject, and prints out the corresponding grade
for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the
marks are valid. For example, a student cannot receive -5 or 110. So the valid marks range is 0 to 100.
'''

number = int(input("please enter number "))

if (number>100 or number<0):
    print("invalid number")
elif(number>=90 and number<=100):
    print("A")
elif(number>=80 and number<=89):
    print("B")
elif(number>=70 and number<=79):
    print("C")
elif(number>=60 and number<=69):
    print("D")
elif(number>=50 and number<=59):
    print("E")
elif(number>=0 and number<50):
    print("F")

