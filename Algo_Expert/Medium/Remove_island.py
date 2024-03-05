#Remove_island

def removeIslands(matrix):
    # Write your code here.
    visited=[[0 for i in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row ==0 or row ==len(matrix)-1) or col==0 or col==len(matrix[0])-1:
                traverse(row,col,visited,matrix)
                
                    
                    
    for row in range(1,len(matrix)):
        for col in range(1,len(matrix[0])):
            if visited[row][col]==0 and matrix[row][col]==1 :
                matrix[row][col]=0    
            
    return matrix

def traverse(row, col, visited, matrix):
    stack = []
    stack.append([row, col])

    while len(stack):
        element = stack.pop()
        i = element[0]
        j = element[1]

        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        if matrix[i][j] == 0:  # Corrected to use i, j for current cell
            continue

        unvisitedNei = getNei(i, j, matrix, visited)
        for nei in unvisitedNei:
            if matrix[nei[0]][nei[1]] == 1 and visited[nei[0]][nei[1]] == 0:
                stack.append(nei)



        
def getNei(row,col,visited,matrix):
    nei=[]
    direction=[[0,1],[1,0],[0,-1],[-1,0]]
    
    for i in direction:
        new_row =row+i[0]
        new_col =col+i[1]
        if (0<= new_row <len(matrix) and 0<= new_col <len(matrix[0])):
            print(matrix[new_row][new_col])
            print('---')
            
            nei.append([new_row,new_col])
    return nei    
    
        
    