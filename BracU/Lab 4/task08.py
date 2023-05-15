l1=[1,2,3,4,5,6,7,8,9]
l2=[10,11,12,-13,-14,-15,-16]
ans=[]

for i in l1:
    if(i%2==0):
        ans.append(i)

for i in l2:
    if(i%2==0):
        ans.append(i)

print("Output for the above lists:", ans)
