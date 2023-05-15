s = input()

r_count=0
g_count=0
b_count=0

R_list=['Red']
G_list=['Green']
B_list=['Blue']

for i in s:
    if(i=='R'):
        r_count+=1
    elif(i=='G'):
        g_count+=1
    elif(i=='B'):
        b_count+=1

R_list.append(r_count)
G_list.append(g_count)
B_list.append(b_count)

temp_list=[]
temp_list.append(tuple(R_list))
temp_list.append(tuple(G_list))
temp_list.append(tuple(B_list))

res=[]
for i in temp_list:
   if(i[1]!=0):
       res.append(i)
print(tuple(res))



