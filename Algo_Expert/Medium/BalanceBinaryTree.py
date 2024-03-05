# This is an input class. Do not edit. Heihgt Balance Binary tree leetcode 110
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class treeInfo:

    def __init__(self,balance,height):
        self.balance=balance
        self.h=height
def heightBalancedBinaryTree(tree):
    # Write your code here.
    
    treeInfo=height(tree)
    return treeInfo.balance
    
def height(tree):
    if tree is None:
        return treeInfo(True,-1)
    left=height(tree.left)
    right=height(tree.right)
    isBalance= left.balance and right.balance and abs(left.h - right.h)<=1
    hght =max(left.h,right.h)+1

    return treeInfo(isBalance,hght)
