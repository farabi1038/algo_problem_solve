
#Rescontruction of BST from pretravesal

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    root = BST(preOrderTraversalValues[0])
    left_val=[]
    right_val =[]
    for i in range (1,len(preOrderTraversalValues)):
        if preOrderTraversalValues[i]< root.value:
            left_val.append(preOrderTraversalValues[i])
        else:
            right_val.append(preOrderTraversalValues[i])
           
    if left_val:
        root.left =reconstructBst(left_val)
    if right_val:
        root.right =reconstructBst(right_val)

    return root