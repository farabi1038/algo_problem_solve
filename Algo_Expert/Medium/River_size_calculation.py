#River_size_calculation



def riverSizes(matrix):
    # Write your code here.
    river_list=[]
    river_size=0
    visited= [[0 for i in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range (len(matrix[0])):
            if visited[row][col]==1:
                continue
            traverse(row,col,matrix,visited,river_list)    
    return river_list

def traverse(row,col,matrix,visited,sizes):
    size=0
    stack=[]
    stack.append([row,col])
    while len(stack):
        current=stack.pop()
        i=current[0]
        j=current[1]
        if visited[i][j]:
            continue
        visited[i][j]=1
        if matrix[i][j]==0:
            continue
        size+=1
        unvisitedNei=getNei(i,j,matrix,visited)
        for nei in unvisitedNei:
            stack.append(nei)

    if size>0:
        sizes.append(size)    

def getNei(row,column,board,visited):
    direct = [(1,0),(0,1),(0,-1),(-1,0)]
    nei=[]
    for r,c in direct:
        new_row = row + r
        new_col = column + c
        if 0<= new_row <len(board) and 0<= new_col <len(board[0]) and ( board[new_row][new_col]==1 and visited[new_row][new_col]==0):
            nei.append([new_row,new_col])
    return nei
