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

def normalization(old_list,min_val,max_val):
    res=[]
    print(min_vla, max_val)
    for i in old_list:
        norm_val= (i-min_val)/(max_val-min_val)
        res.append(norm_val)
    return res




li=[10,4,23,49,36]
old_list=[]

for i in li:
    old_list.append(i)
selection_sort(li)

min_vla=li[0]
max_val=li[-1]

print(normalization(old_list,min_vla,max_val))
