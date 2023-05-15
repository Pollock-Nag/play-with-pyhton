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
temp=[]
for i in given_list:
    li=[]
    for j in i.items():
        li.append(j[1])

    temp.append(li)

name_ratio=[]
for i in temp:
    name=i[0]
    ratio=i[2]/i[1]
    name_ratio.append((name,ratio))
print(name_ratio)

max=-99999.9999
max_name=""
for i in name_ratio:
    if(i[1]>max):
        max=i[1]
        max_name=i[0]
print(max_name)