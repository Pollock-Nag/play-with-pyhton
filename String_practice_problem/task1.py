s="This is CSE110 Course."
countA=0
coutntD=0
countSC=0

for i in s:
    if(ord(i)>96 and ord(i)<123 or ord(i)>64 and ord(i)<90 ):
        countA+=1
    elif(ord(i)>47 and ord(i)<58):
        coutntD+=1
    else:
        countSC+=1
print("Char",countA)
print("digit",coutntD)
print("Special char",countSC)