def upper_lower_count(s):
    upper_count=0
    lower_count=0
    for i in s:
        if(ord(i)>=ord('A') and ord(i)<=ord('Z')):
            upper_count+=1
        elif(ord(i)>=ord('a') and ord(i)<=ord('z')):
            lower_count+=1

    print("No. of Uppercase characters:",upper_count)
    print("No. of Lowercase Characters:",lower_count)


upper_lower_count('The quick Sand Man')
