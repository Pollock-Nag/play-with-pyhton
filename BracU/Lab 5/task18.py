given_list=[(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]
dict={}
unique_keys=[]

for i in given_list:
    if (i[1] not in unique_keys):
        unique_keys.append(i[1])

for i in unique_keys:
    li=[]
    for j in given_list:
        if(i==j[1]):
            li.append(j)
    dict[i]=li
print(dict)