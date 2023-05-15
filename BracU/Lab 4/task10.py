# to do
s = input("Please enter a string of comma separated numbers ")
list = []
mod_list = []
j = 0
for i in range(0, len(s)):
    if s[i] == ",":
        list.append(int(s[j:i]))
        j = i + 1
list.append(int(s[j + 1:len(s)]))
print(list)

for i in list:
    if i not in mod_list:
        mod_list.append(i)
    # if(list.count(i)>1):

print(mod_list)