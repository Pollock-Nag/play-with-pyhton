s='()[]{{}}'

stack=[]
for i in s:
    if(i =='(' or i=="{" or i == '['):
        stack.append(i)
    if(s[0]==')' or s[0]=='}' or s[0]=="]"):
        stack.append(s[0])
        break
    else:
        if(stack[-1]=='(' and i==')' ):
            stack.pop()
        elif (stack[-1] == '{' and i == '}'):
            stack.pop()

        elif (stack[-1] == '[' and i == ']'):
            stack.pop()

if(len(stack)==0):
    print('true')
else:
    print("false")

