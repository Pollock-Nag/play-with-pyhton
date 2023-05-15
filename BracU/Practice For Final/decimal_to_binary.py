num = int(input("Please enter a decimal number "))
rem=""

while(num>=1):
    rem+=str(num%2)
    num=num//2

binary=""
for i in range(len(rem)-1,-1,-1):
    binary+=rem[i]
print(binary)
