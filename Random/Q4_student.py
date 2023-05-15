def student(name,marks):

    sotred_marks=bubble_sort(marks)
    avg=0
    sum = 0
    count=0
    if(len(marks)%2==0):
        count=len(marks)-2
        sum = 0
        for i in range(0,count):
            sum+=sotred_marks[i]

    else:
        count = len(marks)-1
        for i in range(0, count):
            sum+=sotred_marks[i]

    avg=sum/count

    s="Average of "+name+"'s quiz marks: "+str(avg)
    return s
def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]):
                # here we are not using temp variable
                list1[j],list1[j+1] = list1[j+1], list1[j]

    new_list=[]
    for i in range(len(list1)-1,-1,-1):
        new_list.append(list1[i])
    return new_list

#"Jim",[18,20,15,12,19]
print(student("Jim",[18,20,15,12,19]))