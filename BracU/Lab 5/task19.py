inp = input("Please enter a string ").replace(".","")
inp=inp.split()
spc_char=[]
length=int(input("Plase input the length of special char list "))
my_dictionary={}
working_list=[]

for i in range(0,length):
    spc_char.append(input())

for i in inp:
    ascii_sum=0
    for j in i:
        ascii_sum+=ord(j)
    working_list.append((i,ascii_sum%length))


unique_idx=[]

for i in working_list:
    if i[1] not in unique_idx:
        unique_idx.append(i[1])

for i in unique_idx:
    key= spc_char[i]
    li=[]

    for j in working_list:
        if(i==j[1]):
            if(j[0] not in li):
                li.append(j[0])
    my_dictionary[key]=li

print("Words in the given String:",inp)
print("Answer:",my_dictionary)

