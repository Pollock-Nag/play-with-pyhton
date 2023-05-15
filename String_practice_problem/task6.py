n = int(input())
ans=""
for i in range(0,n):
    for j in range(0,i+1):
        ans+="1"
    ans+="+"
cor_ans=ans[0:len(ans)-1]
list= cor_ans.split("+")
sum=0

for i in list:
    sum+=int(i)
print(cor_ans)
print("The sum is:",sum)