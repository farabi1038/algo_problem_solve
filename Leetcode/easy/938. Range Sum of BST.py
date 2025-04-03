# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        sum_list =[]
        q=deque()
        q.append(root)

        while q:
            item =q.popleft()
            if item:
                if low<=item.val<=high:
                    sum_list.append(item.val)
                if item.val>low:
                    q.append(item.left)
                if item.val<high:
                    q.append(item.right)
        return sum(sum_list)            


        