quantity = int (input("Please enter quantity"))
max=-9999999999
min=999999999
sum=0
for i in  range(0,quantity):
    num = int(input())
    sum+=num
    if(num>max):
        max=num
    if(num<min):
        min =num
print("Maximum",max)
print("Minimum",min)
print("Average is",sum/quantity)
