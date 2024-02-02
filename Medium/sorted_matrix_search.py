#search in sorted matrix


def searchInSortedMatrix(matrix, target):
    # Write your code here.
    rowIdx= 0
    colIdx= len(matrix[0])-1
    while rowIdx<len(matrix) and colIdx>=0:
        if matrix[rowIdx][colIdx]==target:
            return [rowIdx,colIdx]
        elif matrix[rowIdx][colIdx]<target:
            rowIdx+=1
        else:    
            colIdx-=1
    return [-1,-1]
