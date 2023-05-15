inp= input("Please enter a word ")
for i in inp:
    next_ascii=ord(i)+1
    if(next_ascii==123):

        print(chr(97), end="")
    else:
        print(chr(next_ascii),end="")
