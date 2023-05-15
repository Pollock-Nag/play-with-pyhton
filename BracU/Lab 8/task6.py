my_list = [10, 20, 30, 40, 60, 100, 2, 5]
try:
    n = int(input())
    print(my_list[n])
except IndexError:
    print("Index out of range.")
except ValueError:
    print("For position, please enter an Integer value.")
except Exception:
    print("Some other error occurs")
finally:
    print('Program ended')
