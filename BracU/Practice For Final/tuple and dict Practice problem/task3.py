inp=input()
t = inp.strip("()").replace("(","").replace(" ","").split("),")
avg=[]
max=-999999
max_idx=0
for i in t:
    sum = 0
    count = 0
    temp = i.split(",")
    for i in temp:
       sum+=int(i)
       count+=1
    avg.append(sum/count)
print(avg)
for i in range(0,len(avg)):
    if(avg[i]>max):
        max=avg[i]
        max_idx=i
print('('+(t[max_idx])+")")