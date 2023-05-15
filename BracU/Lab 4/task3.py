list=[]

for i in range(0,5):
    list.append(int(input()))

print("input data:",list,"\nPrinting values from the list in reverse order:")

for i in range(len(list)-1,-1,-1):
    print(list[i])