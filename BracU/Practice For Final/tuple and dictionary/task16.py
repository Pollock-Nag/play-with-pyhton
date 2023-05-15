my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
bad_elem=[]
for i in my_dictionary.items():
    if(i[1]==None):
        bad_elem.append(i[0])
for i in bad_elem:
    my_dictionary.pop(i)
print(my_dictionary)