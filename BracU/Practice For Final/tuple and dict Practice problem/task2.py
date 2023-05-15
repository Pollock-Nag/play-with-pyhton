s=input().upper()

rgb=[0,0,0]

for i in s:
    if(i=="R"):
        rgb[0]+=1
    if (i == "G"):
        rgb[1] += 1
    if (i == "B"):
        rgb[2] += 1

tuple_list=[]


for i in range(0,len(rgb)):
    if(rgb[i]>0):
        if(i==0):
            tuple_list.append(('Red',rgb[i]))
        if(i==1):
            tuple_list.append(('Green',rgb[i]))
        if (i == 2):
            tuple_list.append(('Blue', rgb[i]))

print(tuple(tuple_list))