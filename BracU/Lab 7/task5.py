def selection_sort(my_list,reverse=False):
    if(reverse==True):
        for i in range(0, len(my_list) - 1):
            max_val = my_list[i]
            max_idx = i
            for j in range(i + 1, len(my_list)):

                if (my_list[j] > max_val):
                    max_val = my_list[j]
                    max_idx = j

            # swap
            temp = my_list[i]
            my_list[i] = my_list[max_idx]
            my_list[max_idx] = temp
        return my_list

    else:
       for i in range(0,len(my_list)-1):
            min_val=my_list[i]
            min_idx= i
            for j in range(i+1,len(my_list)):

                if(my_list[j] < min_val):
                    min_val=my_list[j]
                    min_idx=j

            #swap
            temp=my_list[i]
            my_list[i]=my_list[min_idx]
            my_list[min_idx]=temp
       return my_list


def operation(number_list,course_index):
    selection_sort(number_list, reverse=True)
    #print(mat110)
    j = 0
    for i in number_list:
        for j in lst:
            #print(i, j[course_index])
            if (i == j[course_index]):
                print(j[0])


lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]


inp=input().upper()




if(inp=="CSE110"):
    cse110 = []
    for i in lst:
        cse110.append(i[1])
    #print("cse list",cse110)
    operation(cse110, 1)
elif(inp=="PHY111"):
    phy111 = []
    for i in lst:
        phy111.append(i[2])
    #print("phy list",phy111)
    operation(phy111, 2)
elif(inp=="MAT110"):
    mat110 = []
    for i in lst:
        mat110.append(i[3])
    #print("mat list",mat110)
    operation(mat110,3)

