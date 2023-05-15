# d)18,-27, 36,-45,54,-63
start=18

while(start<=63):

    if(start%2==0):
        print(start,end=", ")
    else:
        if(start==63):
            print(start*-1,end="")
        else:
            print(start*-1,end=", ")

    start+=9
