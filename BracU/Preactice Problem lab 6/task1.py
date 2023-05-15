def unique_char(my_str):
    li=[]
    for i in my_str:
        if i not in li:
            li.append(i)
    for i in range (0,len(li)):
        ans=str(ord(li[i]))+li[i]+str(ord(li[i]))
        li[i]=ans

    return li


s= "pythonbook"
print(unique_char(s))