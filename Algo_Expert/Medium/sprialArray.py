'''
Sprial Array traverse
'''


def spiralTraverse(array):
    # Write your code here.
    result = []
    startRow,endRow = 0, len(array) -1
    startCol, endCol = 0, len(array[0]) -1

    while startRow<=endRow and startCol<=endCol:
        for col in range(startCol,endCol):
            result.append(array[startRow][col])
        for row in range(startRow,endRow+1):
            result.append(array[row][endCol])


        for col in reversed(range(startCol,endCol)):
            if startRow==endRow:
                break
            result.append(array[endRow][col])
            
        for row in reversed(range(startRow+1,endRow)):
            if startCol==endCol:
                break
            result.append(array[row][startCol])

        startRow +=1
        endRow   -=1
        startCol +=1
        endCol   -=1
    return result       
