t= (10, 20, 30, 40, 50, 60)
li=[]

for i in range (len(t)-1,-1,-1):
    li.append(t[i])

print(tuple(li))