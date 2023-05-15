s1= input("please enter a string ")
s2= input("please enter another string ")

bigger=0
smaller=0
ans=""
if(len(s1)>len(s2)):
    bigger=s1
    smaller=s2
else:
    bigger=s2
    smaller=s1

for i in range(0,len(smaller)):
    ans+=s1[i]
    ans+=s2[i]
print(ans,bigger[len(smaller):len(bigger)],sep="")


