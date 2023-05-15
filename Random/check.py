months =  { 1 : 31 ,2 : 28 , 3 : 31 , 4 : 30 , 5 : 31 , 6 : 30 , 7 : 31 , 8 : 31 , 9 : 30 , 10 : 31 , 11 : 30 , 12 : 31}
try:
    day = input()
    month =input()

    if (not day.isdigit()):
        raise ValueError

except ValueError:
    print("Please do not enter any string as input")



