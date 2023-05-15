#dict = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
dict={'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}
max_val=-9999999
key=""
for i in dict.values():
    if(i>max_val):
        max_val=i


for i in dict.items():
    if i[1] == max_val:
        key=i[0]

print("The highest selling book genre is '",key,"' and the number of books sold are ",max_val, end=".",sep="")