row = int(input())

for i in range(1,row+1):
    for j in range (1,i+1):
        print(j,end="")
    print()
    

"""
space = row-1
num=1

for i in range(0,row):
    for j in range(0,space):
        print(" ",end="")

    for k in range(0,num):
        print(k+1,end="")

    space-=1
    num+=1
    print()
"""


"""
for i in range(row+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print(" ")
"""