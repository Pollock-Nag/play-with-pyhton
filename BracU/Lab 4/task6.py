li=[]
max=-99999999
max_idx=0
for i in range(0,5):
    li.append(int(input()))
    if(li[i]>max):
        max=li[i]
        max_idx=i

print("My list:",li)
print("Largest number in the list is",max,"which was found at index",max_idx,end=".")