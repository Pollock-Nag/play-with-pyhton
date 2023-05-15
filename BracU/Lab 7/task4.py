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


sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]
even_idx_list=[]
odd_idx_list=[]
for i in range(0,len(sitting_list)):
    if(i%2==0):
        even_idx_list.append(sitting_list[i])
    else:
        odd_idx_list.append(sitting_list[i])


selection_sort(even_idx_list)
selection_sort(odd_idx_list,reverse=True)

j=0
k=1
for i in range(0,len(even_idx_list)):
    sitting_list[j]=even_idx_list[i]
    sitting_list[k] = odd_idx_list[i]
    j+=2
    k+=2

#res=[10, 100, 11, 80, 12, 70, 20, 56, 22, 30, 58, 16, 70, 15]
print(sitting_list)