file = open('input3.txt','r')
file_output = open('output3.txt','a')
file_list= file.readlines()


for i in file_list:
    temp=i.strip().split()
    string= ""
    for j in temp:
        string+=j+" "

    file_output.write(string+"\n")
file_output.close()