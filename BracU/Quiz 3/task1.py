'''
given_list=[
{'Name': "Tony", "Age": 20, "Salary": 5000},
{"Name": "Salman", "Age": 40, "Salary": 10000},
{"Name": "Jenny", "Age": 21, "Salary": 1500}
]
'''
given_list=[
{'Name': "John Elton", "Age": 22, "Salary": 5000},
{"Name": "Zeus Shah", "Age": 24, "Salary": 8000},
{"Name": "Abu Dhabi", "Age": 20, "Salary": 1000}
]

name_ratio=[]
temp=[]
for i in given_list:
    ratio=0
    li=[]
    for j in i.values():
        li.append(j)
    temp.append(li)



for i in temp:
    name=i[0]
    ratio=i[2]/i[1]
    name_ratio.append((name,ratio))

#print(name_ratio)
max_num=-9999999.999999
max_name=0

for i in name_ratio:
    #print(i[1])
    if(i[1]>max_num):
        max_num=i[1]
        max_name=i[0]




#print("Man_num",max_num)
print(max_name)
