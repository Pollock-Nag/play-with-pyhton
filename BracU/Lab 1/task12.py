"""
Write Python program to compute and display a person’s weekly salary as determined by the following conditions:

If the hours worked are less than or equal to 40, then the person receives Tk200.00 per hour.
If the hours worked are greater than 40, then the person receives Tk8000.00 plus Tk300.00 for each hour worked over 40 hours.
The program should request the hours worked as asn input from the user and should display the salary as output.
You need to make sure that user input is valid. For example, a person cannot work for -5 hours or more than 168 hours in a week.
So the valid marks range is 0 to 168.
"""
hours = int(input("Please input hours "))
if(hours<0):
    print("Hour cannot be negative")
elif(hours>168):
    print("Impossible to work more than 168 hours weekly")
elif(hours<=40):
    print(200*hours)
elif(hours>40):
    print(8000+300*(hours-40))

