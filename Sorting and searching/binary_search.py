def binary_search(my_list,element):
    left_idx=0
    right_idx=len(my_list)-1

    while(left_idx<=right_idx):
        mid=(left_idx+right_idx)//2

        if(my_list[mid]==element):
            return mid
        elif(element<my_list[mid]):
            right_idx=mid-1
        else:
            left_idx=mid+1
    return -1





my_list=[2,3,5,6,10,15]
elem=6

my_list.sort()
print(elem,"is at index number",binary_search(my_list,elem))