#li_1=[1,4,3,2,6]
#li_2=[5,6,9,8,7]


li_1=[1,4,3,2,5]
li_2=[8,7,6,9]

flag=False

for i in li_2:
    if i in li_1:
        flag=True
        break
print(flag)