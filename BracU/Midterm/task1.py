#task1
score=0
sum=0
prod=1
li=[]
flag=True
while(flag):
    count = 0
    n = int(input())
    root=(n**0.5)
    if (int(root+0.5))**2==n:
        li.append(n)
    else:
        break;
    """
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
        #print(i)
    if(count==2):
        break
    """
    #else:
        #li.append(n)
for i in li:
    score+=1
    sum+=i
    prod*=i
if prod==1:
    prod=0
print("Score:",score,"Sum :",sum,"Product :",prod)

