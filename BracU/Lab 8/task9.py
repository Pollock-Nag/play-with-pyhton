inp= input().lower()

v_c=0
c_c=0

for i in inp:
    if(ord(i)>=97 and ord(i)<=123):
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            v_c+=1
        else:
            c_c+=1

try:
    if(v_c>=c_c):
        #print("Number of vowels greater/equal to consonants. Please paraphrase.")
        raise RuntimeError
    else:
        print("The sentence will work.")
except RuntimeError:
    print("Number of vowels greater/equal to consonants. Please paraphrase.")
