# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float("-inf"),float("inf"))

    def validate(self,tree,Min,Max):
        if tree is None:
            return True
        if tree.val<=Min or tree.val>=Max:
            return False
        return self.validate(tree.left,Min,tree.val) and self.validate(tree.right,tree.val,Max)
            
        