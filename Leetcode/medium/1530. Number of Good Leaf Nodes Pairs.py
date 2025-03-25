# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.res=0

        def dfs(node):
            if not node :
                return []
            if not node.left and not node.right:
                return [0]
            leftD = dfs(node.left)
            rightD = dfs(node.right)

            for l in leftD:
                for r in rightD:
                    if l+r+2<=distance:        
                        self.res+=1
            return [d+1 for d in leftD+rightD]            
        dfs(root)
        return self.res        