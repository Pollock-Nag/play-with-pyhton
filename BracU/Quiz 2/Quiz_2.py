s= input("Please input ")
digit=[]
even_sum=0
odd_sum=0
even_Count=0
odd_Count=0
for i in s:
    if(ord(i)>47 and ord(i)<58):
        digit.append(int(i))

for i in digit:
    if(i%2==0):
        even_sum+=i
        even_Count+=1
    else:
        odd_sum+=i
        odd_Count+=1
if(even_Count== len(digit) or odd_Count==len(digit)):
    for i in s:
        if(ord(i)>96 and ord(i)<123 or ord(i)>64 and ord(i)<90):
            print(i,end="")
    print()
else:
    for i in s:
        if(ord(i)>96 and ord(i)<123 or ord(i)>64 and ord(i)<90):
            print(i,end="")
    print(even_sum,end="")
    print(odd_sum,end="")
    print()
