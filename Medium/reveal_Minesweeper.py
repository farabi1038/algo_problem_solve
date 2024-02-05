#reveal_Minesweeper


def revealMinesweeper(board, row, column):
    # Write your code here.
    if board[row][column]== 'M':
        board[row][column] = 'X'
        return board
    stack =[[row,column]]
    board[row][column]=0

    while stack:
        row,column = stack.pop()
        nei=[]
        for r,c in getNei(row,column,board):
            if board[r][c]=='M':
                board[row][column]+=1
            elif board[r][c]=='H':
                nei.append([r,c])
        if board[row][column]==0:
            for r,c in nei:
                stack.append([r,c])
                board[r][c]=0
        board[row][column]=str(board[row][column])
        
                
    return board


def getNei(row,column,board):
    direct = [(1,0),(1,1),(0,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
    nei=[]
    for r,c in direct:
        new_row = row + r
        new_col = column+ c
        if 0<= new_row <len(board) and 0<= new_col <len(board[0]):
            nei.append([new_row,new_col])
    return nei        
        
    