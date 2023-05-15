s= input()
li=list(s.split(","))
prod=1
print(li)
for i in li:
    prod*=int(i)
print("Producy:",prod,sep="")