dictionary = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}
lower,higher= [int (i)for i in (input().split())]
#print (higher)
#print(lower)
ans_dict={}
for i in dictionary.items():
    (key,val)=i
    if(val>=lower and val<higher):
        ans_dict[key]=val


print(ans_dict)
