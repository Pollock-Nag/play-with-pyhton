my_dictionary={"Potato":12, "Onion":16, "Ginger":15, "Garlic":12, "Tomato":15}

try:
    sum =0
    inp=input('please input comma separated grocery item ')
    order_list=inp.split(',')
    for i in order_list:
        price=my_dictionary[i]
        sum+=price
    print(sum)

except KeyError:
    print("Some groceries are not available in the dictionary.")

except TypeError:
    print("the variable to store the total price has not been initialized.")

except Exception:
    print("Some other error occurs")
