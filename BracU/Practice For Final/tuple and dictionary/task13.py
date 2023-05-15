list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

unique=[]
my_dict={}
for i in list:
    if(i[0] not in unique):
        unique.append(i[0])

for i in unique:
    my_list=[]
    for j in list:
        if(i==j[0]):
            my_list.append(j[1])
    my_dict[i]=my_list

print(my_dict)
