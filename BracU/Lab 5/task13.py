list = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dict={}
list_a = []
list_b = []
list_c = []

for i in list:

    if(i[0]=='a'):
        key_a='a'
        list_a.append(i[1])
        dict[key_a] = list_a

    if (i[0] == 'b'):
        key_b = 'b'
        list_b.append(i[1])
        dict[key_b] = list_b

    if (i[0] == 'c'):
        key_c = 'c'
        list_c.append(i[1])
        dict[key_c] = list_c


print(dict)
