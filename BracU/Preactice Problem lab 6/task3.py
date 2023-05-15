from collections import OrderedDict
import collections
def word_count(test):
    my_list=test.split(" ")
    unique_word=[]
    my_dict={}
    for i in my_list:
        if(i not in unique_word):
            unique_word.append(i)


    for i in unique_word:
        count=0
        for j in my_list:
            if (i==j):
                count+=1
        my_dict[i]=count
    #print(my_dict)
    res=dict(sorted(my_dict.items(), key= lambda item:item[1]))  #sorted dict bu values
    return res


test="go there come and go here and there go care"

print(word_count(test))