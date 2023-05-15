course=['CSE110','CSE111','MAT620','CSE520','EEE361','CSE650','MAT510']

def processing(uniq_course,coure_name):
    temp = {}
    for j in uniq_course:
        ug = []
        g = []
        for i in course:

            if (i[:3] == coure_name):

                if (int(i[3]) <= 4):
                    ug.append(i)
                else:
                    g.append(i)

        temp['Undergraduate'] = ug
        temp['Graduate'] = g
    return temp


uniq_course=[]
for i in course:
    if(i[:3] not in uniq_course):
        uniq_course.append(i[:3])

print(uniq_course)

res={}

for i in uniq_course:
    res[i]=processing(uniq_course,i)

print(res)