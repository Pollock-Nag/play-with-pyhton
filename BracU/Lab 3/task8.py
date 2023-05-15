s1= input()
s2= input()
#print((s1.replace(s2,"\n")))

#OR

for i in s1:
    if s2 == i:
        print()
    else:
        print(i,end="")
