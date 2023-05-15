def is_magic_number(n):
    even_sum=0
    odd_sum=0
    for i in range (0,len(n)):
        if(i%2==0):
            even_sum+=int(n[i])
        else:
            odd_sum+=int(n[i])
    if(even_sum==odd_sum):
        return True
    else:
        return False

s= input().replace(" ","").split(",")

magic_number=[]
normal_number=[]
whole_list=[]

for i in s:
    if(is_magic_number(i)):
        magic_number.append(int(i))
    else:
        normal_number.append(int(i))
whole_list.append(tuple(magic_number))
whole_list.append(tuple(normal_number))
print(tuple(whole_list))


