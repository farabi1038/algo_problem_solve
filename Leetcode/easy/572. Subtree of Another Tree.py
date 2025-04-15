# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def match(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (
                a.val == b.val and 
                match(a.left, b.left) and 
                match(a.right, b.right)
            )
        
        return match(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
