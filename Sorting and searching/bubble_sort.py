def bubble_sort(my_list):
    #print("Before sort", my_list)

    for i in range (0, len(my_list) - 1):
        for j in range (0, len(my_list) - i - 1):
            if(my_list[j]>my_list[j+1]):      #if(my_list[j]<my_list[j+1]):   (for reversly sort)
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    #print("After Sort",my_list)
    return my_list
my_listt=[5, 3, 1, 9, 8, 2, 4]
print("Before sort", my_listt)
bubble_sort(my_listt)
print("After Sort",my_listt)


#my_listt array has been sorted