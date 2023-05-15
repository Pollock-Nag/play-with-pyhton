#fibonacci serise
n = int(input())

first=0
sec=1
sum=0
print(0,1,end=" ")
for i in range (2,n):


    sum=first+sec
    first=sec
    sec=sum
    print(sum,end=" ")
