my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
li=[]
for i in my_dictionary.items():
    if(i[1]==None):
        li.append(i[0])
for i in li:
    my_dictionary.pop(i)
print(my_dictionary)