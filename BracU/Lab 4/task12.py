li=[]
max=-99999999
sec_max= -99999999
sec_max_ind=0
for i in range(0,5):
    li.append(int(input()))
    if li[i]>max:
        max=li[i]
        max_index=i

for i in range (0,len(li)):
    if li[i]>sec_max and li[i]!=max:
        sec_max=li[i]
        sec_max_ind=i
print("My list:", li)
print("Second largest number in the list is",sec_max,"which was found at index",sec_max_ind,end=".")