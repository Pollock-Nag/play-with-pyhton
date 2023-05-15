dictionary = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}

n1=int(input())
n2=int(input())

new_dict={}
for i in dictionary.items():
    if(i[1]>=n1 and i[1]<n2):
        new_dict[i[0]]=i[1]
print(new_dict)