def rem_duplicate(dup_tuple):
    unique_list=[]
    for i in dup_tuple:
        if i not in unique_list:
            unique_list.append(i)

    return tuple(unique_list)

print(rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2])))
