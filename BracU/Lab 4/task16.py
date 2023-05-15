s= input()
first_char=s[0]
ns1=""
if s[0]=="'":
    ns1=ns1.join(s.split("'"))
elif s[0]=='"':
    ns1=ns1.join(s.split('"'))
ns2=""
ns3=""
if(ns1[0]=="["):
    ns2=ns2.join((ns1.strip("[]")))
ns3=""
print(ns1)
print(ns2)


print("[",ns2.replace(" ",""),"]",sep="")
for i in ns3:
    if i==" ":
        print(i,end="")
    else:
        print("'",i,"'",end="",sep="")

print()
