a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

inp= input()
for i in a_tuple:
    i[2]=inp
print(a_tuple)