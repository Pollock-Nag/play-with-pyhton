li=['Red','Green','Blue','White','Black']

ans=[]
for i in li:
    ans.append(i[-1:len(i)*-2:-1])
print(ans)
