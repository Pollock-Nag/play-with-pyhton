dict1 = {'x': 100, 'y': 'Green', 'z': 400,"p":700}
dict2 = {'x': 300, 'y': 'Red', 'z': 600,'w': 50}
new_dict=dict1.copy()
new_dict.update(dict2)

#print(new_dict)

similar_key_li = []
for i in dict1.items():
    #print(i)
    if (i[0] in dict2.keys()):
        similar_key_li.append(i[0])

#print(similar_key_li)



for i in new_dict.items():
    li=[]
    if i[0] not in similar_key_li:
        li.append(i[1])
    new_dict[i[0]]=li
    #print(list(i[1]))
for i in similar_key_li:
    li=[]
    li.append(dict1[i])
    li.append(dict2[i])
    new_dict[i]=li


print("Ans",new_dict)


