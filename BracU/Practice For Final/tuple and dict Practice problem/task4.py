dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}

dict3=dict1.copy()
dict3.update(dict2)

similar=[]

for i in dict1.keys():
    if(i in dict2.keys()):
        similar.append(i)


for i in similar:
    li=[]
    li.append(dict1[i])
    li.append(dict2[i])
    dict3[i]=li

for i in dict3.items():
    if(i[0] not in similar):
        li = []
        li.append(dict3[i[0]])
        dict3[i[0]]=li



print(dict3)