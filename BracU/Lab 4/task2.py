n = int(input("please enter length of the list "))
inp=[]
ans=[]

for i in range(0,n):
  inp.append(int(input()))
if(len(inp)<4):
    print("Not possible")
else:
    for i in range(2,len(inp)-2):
        ans.append(inp[i])
    print(ans)