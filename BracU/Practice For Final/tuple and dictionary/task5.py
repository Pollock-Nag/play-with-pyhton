t= (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
num =int (input())
count=0
for i in t:
    if (i==num):
        count+=1
print(num,'appears',count,'times in the tuple')