def customized_dict(s):
    li=s.split(" ")

    year=[] #tup of first 2 digits
    for i in li:
        year.append((i[0],i[1]))

    unq_year=[] #unique keys

    for i in year:
        if(i not in unq_year):
            unq_year.append(i)


    my_dict={}
    for i in unq_year:
        s1=i[0]
        s2=i[1]
        dict_key=s1+s2+"th"

        dict_val = []
        for i in li:
            if(s1==i[0] and s2==i[1]):
                dict_val.append(i)

        my_dict[dict_key]=dict_val
    return (my_dict)

stu_id=input()
#stu_id="18101202 18104354 20101457 19103372 20301021"
#stu_id="10101202 12104354 13101457 13103372 20301021 10101457"

print(customized_dict(stu_id))

