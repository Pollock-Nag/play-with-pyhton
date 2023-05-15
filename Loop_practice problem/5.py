check=1
while(True):
    inp = input();
    if (inp == "STOP"):
        break
    else:
        num=int(inp)
        check=num*check

print(check,end=" ")
