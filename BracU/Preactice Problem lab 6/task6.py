def print_mat(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()
matrix= [[1, 0, 0, 0], [0, 5, 0, 0], [0, 0, 9, 0], [0, 0, 0, 3]]
print_mat(matrix)