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

def run(my_list):
    if(len(my_list)%2!=0):
        return(my_list[len(my_list)//2])
    else:
        first_half_idx = len(my_list) // 2-1
        sec_half_idx = len(my_list) // 2

        return((my_list[first_half_idx]+my_list[sec_half_idx])/2)
        #print(my_list[len(my_list) // 2]+my_list[len(my_list) // 2])


inp1=input("pleasse enter first list ").strip("[]").split(',')
inp2=input("pleasse enter second list ").strip("[]").split(',')
marged_list=[]

for i in inp1:
    marged_list.append(int(i))
for i in inp2:
    marged_list.append(int(i))

selection_sort(marged_list)
print('Sorted list =',marged_list)
print('Median =',run(marged_list))

'''
[1, 2, 1, 4]
[5, 4, 1]
'''