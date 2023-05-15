"""
Write Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds.
"""

sec = int(input("please enter seconds "))
min = sec/60
hours= min/60

print("Hours:",int(hours)," Minutes:",int(min%60)," Seconds:",int(sec%60))