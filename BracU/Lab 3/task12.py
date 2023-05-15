s1 = input()
c1= input()
ans=""
if(s1.find(c1)==True):
    ans+=s1.replace(c1,"")
    print(ans)

elif(s1.find(c1)==False or len(s1)>3):
    ans+=s1[1:len(s1)-1]
    print(ans)
else:
    print(s1)
