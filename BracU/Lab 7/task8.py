def minimum_sum(my_list):
    if(len(my_list)<2):
        print ("Invalid length of array")
    else:
        min_sum=my_list[0]+my_list[1]
        min_sum_first_idx=0
        min_sum_2nd_idx=1
        for i in range(0,len(my_list)-1):
            for j in range(i+1,len(my_list)):
                curr_sum= my_list[i]+my_list[j]
                if(abs(curr_sum)<abs(min_sum)):
                    min_sum=curr_sum
                    min_sum_first_idx=i
                    min_sum_2nd_idx=j

        print("Two pairs which have the smallest sum =",my_list[min_sum_first_idx],"and",my_list[min_sum_2nd_idx])




inp=input("please enter list ").strip("[]").split(',')
input_list=[]
for i in inp:
    input_list.append(int(i))
minimum_sum(input_list)