'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''

def transposeMatrix(matrix):
    # Write your code here.
    return [list(t) for t in list(zip(*matrix))]
