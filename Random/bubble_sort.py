def bubble_sort (list):
    for i in range(0,len(list)):
        for j in range (0,len(list)-1-i):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

li=[5,2,4,3,1]

print(bubble_sort(li))

