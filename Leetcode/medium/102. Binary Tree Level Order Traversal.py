# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=deque()
        if not root:
            return []

        q.append(root)
        visited=set()
        output_list=[]

        while q:
            level_size = len(q)
            level_nodes = []

            for _ in range(level_size):
                item = q.popleft()
                level_nodes.append(item.val)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            output_list.append(level_nodes)
                
        return output_list
        