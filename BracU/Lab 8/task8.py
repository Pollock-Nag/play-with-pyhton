def operation(l1,l2):
    try:
        result = 0
        for i in range(0, len(mylist_1)):
            result += int(mylist_1[i]) * int(mylist_2[i])
        return result
    except ValueError:
        return "The list has some non number values"

    except IndexError:
        return "Index out of bound"
    except Exception:
        return "Some other error occurs"


mylist_1=[i for i in input("Enter the list items : ").split()]
mylist_2=[i for i in input("Enter the list items : ").split()]


print(operation(mylist_1,mylist_2))
