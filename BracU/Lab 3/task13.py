s1= input()
ns=""
ans=""
idx=[]
for i in range (0,len(s1)):
    if(ord(s1[i])>64 and ord(s1[i])<91  or ord(s1[i])>96 and ord(s1[i])<123 ):
        ns+=s1[i]
    else:
        idx.append(i)

for i in range(0,len(ns)):
    if(i%2==0):
        ans+=ns[i].upper()
    else:
        ans+=ns[i].lower()

li=list(ans)

for i in range (0,len(idx)):
    li.insert(idx[i],s1[idx[i]])


for i in range(0,len(li)):
    print(li[i],end="")
