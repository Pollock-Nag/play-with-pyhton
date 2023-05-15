def processing(course,code):
    my_dict = {}
    under_grad = []
    masters = []
    for j in course:

        if (j[:3] == code):
            if (int(j[3]) < 5):
                under_grad.append(j)
            else:
                masters.append(j)
    my_dict['undergradurate'] = under_grad
    my_dict['masters'] = masters
    return my_dict


course=['CSE110','CSE111','MAT620','CSE520','EEE361','CSE650','MAT510']
result={}
dept=[]

for i in course:
    dname=""
    for j in range(0,3):
        dname+=i[j]
    if (dname not in dept):
        dept.append(dname)


for i in dept:
    result[i]= processing(course,i)

print(result)