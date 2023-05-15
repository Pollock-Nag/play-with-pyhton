file=open("task1.txt")
file_list= file.readlines()
max_length = -1
max_length_word = ""

for i in file_list:
    temp=(i.strip().replace('.','').split())
    for j in temp:
        if(len(j)>max_length):
            max_length=len(j)
            max_length_word=j

print(max_length_word)
