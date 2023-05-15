def matrix_sum(a,b):
    dim_a=[]
    dim_b=[]
    for i in a:
        dim_a.append(len(i))
    for i in b:
        dim_b.append(len(i))

    if(dim_a!=dim_b):
        print("No of columns not same")
    else:
        res =[]

        for i in a:
            li=[]
            for j in i:
                li.append(0)
            res.append(li)

        for i in range(0,len(a)):
            for j in range(0,len(a[i])):
                res[i][j]=a[i][j]+b[i][j]
        print(res)



matrix_A = [ [1,5, 4] , [-4,3, 3] ]
matrix_B = [ [2,-1, -3] , [4,-1, -4] ]
matrix_sum(matrix_A,matrix_B)