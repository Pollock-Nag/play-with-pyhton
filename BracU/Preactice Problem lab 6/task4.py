def procesing(s):
    unq=[]
    my_dict = {}
    for i in s:
        if i not in unq:
            num = int(i)
            unq.append(num)
    for i in unq:
        li_tup = []
        li_tup.append(is_even(i))
        li_tup.append(is_prime(i))
        li_tup.append(is_perfect(i))
        my_dict[i]=tuple(li_tup)
    print(my_dict)


def is_even(num):
    flag="odd"
    if(num%2==0):
        flag="even"
    else:
        flag="odd"
    return flag

def is_prime(n):
    flag="not prime"
    count=0
    for i in range(1,n+1):
        if(n%i==0):
           count+=1
    if(count==2):
        flag="prime"
    else:
        flag="not prime"
    return flag

def is_perfect(n):
    flag="not perfect"
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i

    if sum==n:
        flag="perfect"
    else:
        flag="not perfect"
    return flag

test = "2441396"
print(procesing(test))