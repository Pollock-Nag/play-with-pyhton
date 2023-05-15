try:
    day = input()
    month = input()

    if(not day.isdigit()):
        raise TypeError
    if(not month.isdigit()):
        raise TypeError


    day=int(day)
    month=int(month)


    flag="NONE"
    if (day<0 or day>31):
        flag="DE"
        raise ValueError

    if (month<0 or month>12):
        flag = "ME"
        raise ValueError

    distance=0
    if day<10:
        distance=5+(day*2)/month
    else:
        distance=3 + (day / month)

    print(distance,"kilometres")

except ZeroDivisionError:
    print("0 is not a valid month")

except TypeError:
    print("Please do not enter any string as input")

except ValueError:
    if(flag=="DE"):
        print(day, "is not a valid day of any month")
    else:
        print(month, "is not a valid month")

except Exception:
    print("Some error occurs ")