#kth largest eklement of BST

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array=[]
    array=inorder(tree,array,float('-inf'),float('inf'))
    return array[-k]
def inorder(tree,array,min,max):


    if tree is None :
        return
    inorder(tree.left,array,min,tree.value)
    array.append(tree.value)
    inorder(tree.right,array,tree.value,max)
    return array
