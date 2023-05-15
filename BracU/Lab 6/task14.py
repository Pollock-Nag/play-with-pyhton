def remove_char(sentance,num):
    rem_char=""
    result_str=sentance[0]
    for i in range(1,len(sentance)):
        if(i%num==0):
            rem_char+=sentance[i]
        else:
            result_str+=sentance[i]
    return result_str+rem_char

sentance = input()
num = int(input())

print(remove_char(sentance,num))
