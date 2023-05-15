def num_of_chanfed_position(li):
    sorted_list=sorted(li)
    count=0
    for i in range(0,len(li)):
        if(sorted_list[i]!=li[i]):
            count+=1
    return count

my_list = [4, 2, 3, 1, 6, 5]
print(num_of_chanfed_position(my_list))