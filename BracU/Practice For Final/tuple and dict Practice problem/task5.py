def prime_list(li):
    res=[]
    for i in li:
        if(isprime(i)):
            res.append(i)
    return res

def isprime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return True
    else:
        return False


my_dict={"N":(4,9,3),"k":[95,37,197],"F":(32,5,97),"s":[31,94,55]}
new_dict={}
#print(my_dict)

for i in my_dict.items():

    if(i[0].isupper()):
        temp=list(i[1])
        #print(temp)
        pl=prime_list(i[1])
        new_dict[i[0]]=tuple(pl)

    else:
        pl=prime_list(i[1])
        new_dict[i[0]] = pl

print(new_dict)