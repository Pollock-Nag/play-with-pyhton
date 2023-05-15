my_dict={'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}
max_val=-999999
max_key=""


for i in my_dict.items():
    if(i[1]>max_val):
        max_val=i[1]
        max_key=i[0]

print(max_key,max_val)