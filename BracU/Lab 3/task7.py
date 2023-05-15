s1= input("please enter a String with length greater than 1 ")
s2 = int (input("please enter index "))

for i in range (s2,-1,-1):
    print(s1[i],end="")
print(s1[s2+1:])
