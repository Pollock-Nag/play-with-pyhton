dict={}
sum =0
n=0
for i in range(0,3):
    key=input("Please Enter Key ")
    val=int(input("Please Enter Value "))
    dict[key]=val
    n+=1

for i in dict.values():
    sum+=i
print("Average is",sum//n)