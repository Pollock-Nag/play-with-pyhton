n = int(input("Please enter list length "))
list=[]
first_even=0
first_odd=0

for i in range(0,n):
    list.append(int(input()))

for i in list:
    if(i%2==0):
        first_even=i
        break

for i in list:
    if(i%2!=0):
        first_odd=i
        break
if(first_even==0):
    print("First even:", "not fount", "and First odd:", first_odd)
elif(first_odd==0):
    print("First even:", first_even, "and First odd:", "not found")
else:
    print("First even:",first_even,"and First odd:",first_odd)


