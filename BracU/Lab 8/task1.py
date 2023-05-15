file=open("task1.txt")
file_list= file.readlines()

n=int(input("Please enter how many number of lines you want to read between 1-4 "))

for i in range(0,n):
    print(file_list[i],end="")