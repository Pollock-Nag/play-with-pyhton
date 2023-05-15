my_dict={}
n= int(input('number of elements in dictionary '))
sum=0
for i in range(0,n):
    key = input("key ")
    val = int(input("value "))
    my_dict[key]=val

for i in my_dict.values():
    sum+=i
print("average is",sum//n)


