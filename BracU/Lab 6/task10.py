def make_square(limit):
    my_dict={}
    for i in range(limit[0],limit[1]+1):
        my_dict[i]=i**2
    return my_dict
make_square((1,3))
print(make_square((5,9)))