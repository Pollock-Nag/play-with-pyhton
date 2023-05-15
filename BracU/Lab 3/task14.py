s1=input()
s2=input()
l1=[]
l2=[]


if (s1==s2 or len(s1)!= len(s2)):
    print("Not anagram")
else:
    for i in range(0,len(s1)):
        l1.append(ord(s1[i]))
        l2.append(ord(s2[i]))
    flag=False

    l1.sort()
    l2.sort()
    if(l1==l2):
        print("Anagram")
    else:
        print("Not Anagram")

