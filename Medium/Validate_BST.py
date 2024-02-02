# Validate_BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validate(tree,float("-inf"),float("inf"))

def validate(tree,min,max):
    if tree is None:
        return True
    if tree.value<min or tree.value>=max:
        return False
    return validate(tree.left,min,tree.value) and validate(tree.right,tree.value,max)
