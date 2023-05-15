sum=0
for i in range (0,601):
    if(i%7==0 or i%9==0):
        if(i%7==0 and i%9==0):
            sum+-0
        else:
            sum+=i

print(sum)