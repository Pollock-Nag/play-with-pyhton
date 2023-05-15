def is_prime(n):
    count=0;
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return  True
    else:
        return False

dict1={"N":(4,9,3),"k":[95,37,197],"F":(32,5,97),"s":[31,94,55]}
dict_prime={}
for i in dict1.items():
    #print(i[1])
    prime_list = []
    for j in i[1]:

       #print(j)
        if (is_prime(j)):
            prime_list.append(j)
    if(ord(i[0])>=97 and ord(i[0])<=122):
        dict_prime[i[0]]=prime_list
    else:
        #print(tuple(prime_list))
        dict_prime[i[0]]=tuple(prime_list)


print(dict_prime)
