my_list=[i for i in input("Enter space separated frequency : ").split()]
h=1050
try :
    for i in range(0,len(my_list)):
        my_list[i]=int(my_list[i])*h
    print(my_list)
except ValueError:
    print("Wrong input type")

