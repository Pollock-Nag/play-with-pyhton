def selection_sort(my_list):
    for i in range(0,len(my_list)-1):
        min_val=my_list[i]
        min_idx=i
        for j in range(i+1,len(my_list)):
            if(my_list[j]<min_val):
                min_val=my_list[j]
                min_idx=j
        #swap
        temp=my_list[i]
        my_list[i]=my_list[min_idx]
        my_list[min_idx]=temp
    return my_list


my_list = [10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]
#res=[1, 2, 2, 3, 5, 6, 10, 11, 12, 14, 15, 17, 18, 20, 29]
print(selection_sort(my_list))