#((33, 22, 11), (30, 45, 56, 45,20), (81, 90, 39, 45), (1, 2, 3, 4,5,6))


inp = input().replace(" ","").strip("()")
inp=inp.replace("(","")
inp_list=inp.split("),")

print(inp_list)
outer_list=[]

for i in inp_list:
    inner_list =i.split(",")
    outer_list.append(inner_list)

print(outer_list)
avg_list=[]

max_sum=-1111111111
max_list_index=0
for i in range (0,len(outer_list)):
    sum=0
    count=0
    for j in range(0,len(outer_list[i])):
        sum+=int(outer_list[i][j])
        count+=1

    if(sum>max_sum):
        max_sum=sum
        max_list_index=i

    avg_list.append(sum/count)




list_with_max_sum_integer=[]
for i in outer_list[max_list_index]:
    list_with_max_sum_integer.append(int(i))

print(avg_list)
print(tuple(list_with_max_sum_integer))