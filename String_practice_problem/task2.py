s="It is a string with the smallest and largest word."
max_elem_length=-999999999
min_elem_length=1000000
count=0
si=0
ei=0
max_word_si=0
min_word_si=0

for i in range(0,len(s)):
    if s[i]==" ":
        ei=i;
        count = ei-si
        #print(count)
        if (count > max_elem_length):

            max_word_si = si
            max_elem_length = count
        if(count<min_elem_length):
            min_word_si=si
            min_elem_length=count

        si=ei+1



#print(max_elem_length)
print(s[max_word_si : max_word_si + max_elem_length])
#print(min_elem_length)
print(s[min_word_si: min_word_si + min_elem_length])

