def create_empty_grid(no_of_row,no_of_col):
    grid = []
    for i in range(no_of_row):
        grid.append([0] * no_of_col)
    return grid

def inserting_Val_into_Grid(x,y,grid,row,col):
    for i in range(0,row):
        for j in range(0,col):
            grid[x][y]=1
            grid[y][x] = 1

def printGrid(grid,row,col):
    for i in range(0,row):
        for j in range(0,col):
            print(grid[i][j], end=" ")
        print()

#**************  MAIN  **********#
no_of_nodes = 6 #user input
no_of_edges = 8 #user input

row = col = no_of_nodes
#creating empty grid of 0's
grid = create_empty_grid(row,col)

#inserting weights into grid
for i in range(no_of_edges):
    li = input().split(" ")
    x, y = int(li[0]), int(li[1])
    inserting_Val_into_Grid(x,y,grid,row,col)

#printing grid
printGrid(grid,row,col)

