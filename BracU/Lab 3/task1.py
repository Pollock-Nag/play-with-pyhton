inp = input("Please enter a string")
for i in range (0,len(inp)):
    for j in range (0,i+1):
        print(inp[j],end="")
    print()


