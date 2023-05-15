s1="India is great"
s1=s1.lower()

s2="is"
ans=[]
dirty_char=[]
res=""
removing_idx=0
for i in range (0,len(s2)):
    for j in range (0,len(s1)):
        if(s2[i]==s1[j]):
            ans.append(j)
li = list(s1)

#print(ans)
for i in range(0,len(ans)):
    dirty_char.append((s1[ans[i]]))

for i in s1:
    if i not in dirty_char:
        res+=i
print(res)