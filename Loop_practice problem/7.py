n = int(input("No of sides: "))
if(n==1 or n==2):
    print("A line can be drawn")

elif(n==3):
    list=[]
    print("Length of sides: ")
    for i in range(0,n):
        inp= int(input())
        list.append(inp)
    if(list[0]+list[1]>list[2] and list[1]+list[2]>list[0] and
      list[2]+list[0]>list[1]):
        print("A triangle can be drawn")
    else:
        print("A triangle cannot be drawn")


elif(n==4):
    list=[]
    print("Length of sides: ")
    for i in range(0,n):
        inp= int(input())
        list.append(inp)
    if(list[0]+list[1]+list[2]>list[3] and list[1]+list[2]+list[3]>list[0] and
      list[2]+list[3]+list[0]>list[1]and list[3]+list[0]+list[1]>list[2]):
        print("A rectangle can be drawn")
    else:
        print("A rectangle cannot be drawn")
