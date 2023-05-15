def fibonacci(n):
    fst_num=0
    sec_num=1
    print(fst_num,end=" ")
    print(sec_num,end=" ")
    for i in range(0,100001):
        third_num=fst_num+sec_num
        if (third_num > n):
            break
        print(third_num,end=" ")
        fst_num=sec_num
        sec_num=third_num

    print()

fibonacci(5)