# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

            idx = {v: i for i, v in enumerate(inorder)}
            
            def build(l, r, i):
                if l > r: return None, i
                root = TreeNode(preorder[i])
                m = idx[preorder[i]]
                i += 1
                root.left, i = build(l, m - 1, i)
                root.right, i = build(m + 1, r, i)
                return root, i

            return build(0, len(inorder) - 1, 0)[0]