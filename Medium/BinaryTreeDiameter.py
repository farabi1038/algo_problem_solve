# Diameter of binary tree 543 Leetcode

# This is an input class. Do not edit.
class BinaryTree:
    global maxDia
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    global maxDia
    maxDia=0
   
    path=height(tree)
    return maxDia
    return path
def height(tree):
    global maxDia
    if tree is None:
        return 0
    left_path=height(tree.left)
    right_path=height(tree.right)
    cur_max = left_path+right_path
    maxDia=max(maxDia,cur_max)
    return max(left_path,right_path)+1
    