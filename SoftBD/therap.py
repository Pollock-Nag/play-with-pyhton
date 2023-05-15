def print_num(start,end):
    for i in range(start,end+1):
        print(i)
        if i%7==0:
            print("Dhaka")
        if i%13 ==0:
            print("Bangladesh")
        if i %7==0 and i%13==0:
            print("Dhaka, Bangladesh")
#print_num(1,500)

sum =0.0
j=1.0
i=2.0
ans = []
while(i/j>0.001):
    j=j+j;
    sum+=i/j
    ans.append(sum)
    print(sum)
print(len(ans))
import math
print(math.sqrt(1000))