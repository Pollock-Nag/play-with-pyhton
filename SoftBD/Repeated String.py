
s='aba'
n = 10
temp=""
for i in range(n):
    #temp+=s[i]
    if(i>len(s)-1):
        #pass
        new_i = i%len(s)
        temp+=s[new_i]
    else:
        temp+=s[i]
print(temp.count("a"))