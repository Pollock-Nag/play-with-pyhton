s1= input("please enter a string ")
cur=""
ans=""
for i in range (0,len(s1)):
    if(s1[i] != cur):
        cur = s1[i]
        ans+=s1[i]

print(ans)
