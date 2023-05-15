number=[]
li=[]

for i in range(0,5):
    s= input()
    num = ""
    si = 0
    ei = 0
    for i in range(0,len(s)):
        index = []
        bad_idx = []
        if (ord(s[i]) > 47 and ord(s[i]) < 58):
            dig=s[i]
            index.append(i)
            num+=dig
        else:
            li.append(num)
            bad_idx.append(i)
            num=""
    """
    for i in index:
        li.append(int(s[i]))
    print(li)
    """
    li.append(num)
for i in li:
    if i is i!="":
     number.append(int(i))

print(number)

