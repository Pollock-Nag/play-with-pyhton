t=['p','q','r','s']
n=2
ans=[]
for i in range(1,n+1):
    for j in t:
        ans.append(j+str(i))

print(ans)