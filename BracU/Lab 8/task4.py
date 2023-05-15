file = open('input4.txt','r')
file_list=file.readlines()
count=0

for i in file_list:
    count+=1

print(count)