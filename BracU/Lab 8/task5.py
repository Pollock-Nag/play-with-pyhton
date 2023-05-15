file1=open('input5_1.txt','r')
file2=open('input5_2.txt','r')
file_output=open('output5.txt','a')
file1_list=[]
file2_list=[]


for i in file1:
    file1_list.append(i.strip())
for i in file2:
    file2_list.append(i)

for i in range(0,len(file1_list)):
    string=file1_list[i]+" "+file2_list[i]
    file_output.write(string)
    print(string,end="")

print(file2_list)