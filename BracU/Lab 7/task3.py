def selection_sort(my_list):
    for i in range(0,len(my_list)-1):
        max_val=my_list[i]
        min_idx=i
        for j in range(i+1,len(my_list)):
            if(my_list[j]>max_val):
                max_val=my_list[j]
                min_idx=j
        #swap
        temp=my_list[i]
        my_list[i]=my_list[min_idx]
        my_list[min_idx]=temp
    return my_list


my_list = [10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]
#res=[29, 20, 18, 17, 15, 14, 12, 11, 10, 6, 5, 3, 2, 2, 1]
print(selection_sort(my_list))