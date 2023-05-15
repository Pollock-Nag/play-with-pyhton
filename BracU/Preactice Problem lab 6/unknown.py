import math
def makelist(r,c):
    li=[]
    for i in range(0,r):
        col=[]
        for j in range(0,c):
            col.append("*")
        li.append(col)

    return populatelist(li,r,c)


def populatelist(li,r,c):
    count=0
    for i in range (0,r):
        for j in range(0,c):
            li[i][j]=math.factorial(count)
            count+=1
    return li


(r,c)= (input().split())

grid=makelist(int(r),int(c))

for i in grid:
    for j in i:
        print(j,end=" ")
    print()
