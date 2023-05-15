inp = input("Please enter a word ")


if(len(inp)<4):
    print(inp)
if(len(inp)>3 and inp.endswith("er")==False and inp.endswith("est")==False):
    print(inp+"er")
if(inp.endswith("er")):
    print(inp.replace('er',"est"))
if(inp.endswith("est")):
    print(inp.replace('est',"est"))
