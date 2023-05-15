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

my_list=[3,5,7,1,2,-11,-66,7,99,100]

print("Old",my_list)
selection_sort(my_list)
print("New",my_list)

#my_list arr has been sorted 