s= input()
s+=" "
max_count =0
count=0
current=s[0]
si=0
ei=0
ans=[]
for i in range(1,len(s)):
    if(s[i]!=current):
        #print(s[i])
        ei=i
        count=ei-si
        #print("strat",si,"end",ei,"counr", count)
        ans.append(s[si:ei])

        if(count>max_count):
            max_count=count
        current = s[i]
        si=i
max_idx=0
max_val=0
#print(ans)
for i in range(0,len(ans)):
    if(len(ans[i])>max_val):
        max_val=len(ans[i])
        max_idx=i
        #print(max_idx)
result=ans[max_idx]

if(len(result)<=1):
    print("None")
else:
    print(result)