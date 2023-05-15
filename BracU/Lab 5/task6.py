tup= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
li = []
for i in range(len(tup)-1,-1,-1):
    li.append(tup[i])
print(tuple(li))
