s = input().lower().replace(" ","")
unique=[]

for i in s:
    if i not in unique:
        unique.append(i)


my_dict={}
for i in unique:
    count=0
    for j in s:
        if(i==j):
            count+=1
    my_dict[i]=count

print(my_dict)