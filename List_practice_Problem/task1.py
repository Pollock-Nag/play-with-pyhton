#l1=[10,20,30,40]
#l2=[100,200,30,400]
l1=[90,30,-30,20,12]
l2=[-8,-5,-2,100,6]
count= len(l2)-1
for i in range(0,len(l1)):
    print(l1[i],end=" ")
    print(l2[count])
    count-=1

