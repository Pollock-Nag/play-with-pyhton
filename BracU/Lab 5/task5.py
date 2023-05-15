tuple=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

n = int(input())
count=0
for i in tuple:
    if (i==n):
       count+=1
print(n,"appears",count,"times in the tuple")