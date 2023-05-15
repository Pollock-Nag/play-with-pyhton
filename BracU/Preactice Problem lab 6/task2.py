def unique_char(my_str):
    li=[]
    my_dict={}
    for i in my_str:
        if i not in li:
            li.append(i)
    list_of_index=[]
    for i in li:
        curr_inx=[]
        for j in range( 0,len(my_str)):
            if (i==my_str[j]):
                curr_inx.append(j) #For positive index
                curr_inx.append(((len(my_str) * -1) + j)) #For negative index
        list_of_index.append(curr_inx)
        my_dict[i]=curr_inx

    return my_dict


s= "pythonbook"
print(unique_char(s))