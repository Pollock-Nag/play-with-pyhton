str = input().lower()
dict={}
for i in str:
    if (ord(i)>=97 and ord(i)<=122):
        key=i;
        count=0
        for j in range(0,len(str)):
            if(i==str[j]):
                count+=1
        dict[key]=count

print(dict)