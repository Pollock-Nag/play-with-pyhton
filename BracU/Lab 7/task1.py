def bubble_sort(my_list):
    for i in range(0,len(my_list)-1):
        for j in range(0,len(my_list)-i-1):
            if(my_list[j]>my_list[j+1]):
                temp = my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp

    return my_list


my_list=[1, 2, 2, 3, 5, 6, 10, 11, 12, 14, 15, 17, 18, 20, 29]
#res=[1, 2, 2, 3, 5, 6, 10, 11, 12, 14, 15, 17, 18, 20, 29]
print(bubble_sort(my_list))