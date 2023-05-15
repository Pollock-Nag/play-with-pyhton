s=input()
ans=list(s)
index=[]

for i in range(1,len(s)):

    if(s[i-1]==" "):
        ans.pop(i)
        ans.insert(i,chr(ord(s[i])-32))
ans_string=''.join(ans)
print(ans_string)

