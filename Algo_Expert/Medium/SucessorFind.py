

# This is an input class. Do not edit.Inorder tracversal Leetcode 285
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    traversal = inOrderTraverse(tree, [])
    print("traversal",traversal,node.value)
    for i in range(len(traversal)):
        if traversal[i].value == node.value:
            return traversal[i + 1] if i + 1 < len(traversal) else None
            
def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is not None:
        inOrderTraverse(tree.left,array)
        array.append(tree)
        inOrderTraverse(tree.right,array)
    return array    
