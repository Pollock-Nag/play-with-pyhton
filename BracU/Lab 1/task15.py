"""
Take an hour from the user as input and tell it is time for which meal.

• The user will input the number in a 24-hour format. So, 14 means 2 pm, 3 means 3 am, 18 means 6 pm, etc.
• Valid inputs are 0 to 23. Inputs less than 0 or more than 23 are invalid in 24-hour clock.
• Assume, Input will be whole numbers. For example, 3.5 will NOT be given as input.
==========================================================

Inputs: Message to be printed
4 to 6: Breakfast
12 to 13: Lunch
16 to 17: Snacks
19 to 20: Dinner
For all other valid inputs, say "Patience is a virtue"
For all other invalid inputs, say "Wrong time"

==========================================================

For example,
If the user enters 4, your program should print the message "Breakfast".
If the user enters 5, your program should print the message "Breakfast".
If the user enters 6, your program should print the message "Breakfast".
If the user enters 0, your program should print the message "Patience is a virtue".
If the user enters 1, your program should print the message "Patience is a virtue".
If the user enters 18, your program should print the message "Patience is a virtue".
If the user enters 23, your program should print the message "Patience is a virtue".
If the user enters 24, your program should print the message "Wrong Time".
If the user enters -1, your program should print the message "Wrong Time".
If the user enters 27, your program should print the message "Wrong time".

==========================================================

"""

hours = int(input())

if(hours<0 or hours>23):
    print("Wrong Time")
elif(hours==4 or hours==5 or hours==6):
    print("Breakfast")
elif(hours==12 or hours==13):
    print("Lunch")
elif(hours==16 or hours==17):
    print("Snacks")
elif(hours==19 or hours==20):
    print("Dinner")
else:
    print("Patience is a virtue")


