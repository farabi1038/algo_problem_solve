# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        min_,max_=0,0
        dict_ = defaultdict(list)
        q.append([root,0])
        if not root:
            return []
        while q:
            item,level = q.popleft()
            dict_[level].append(item.val)
            min_=min(min_,level)
            max_=max(max_,level)
            if item is not None:
                if item.left:
                    q.append([item.left,level-1])
                if item.right:
                    q.append([item.right,level+1])    

        result=[]
        for i in range(min_,max_+1):
            result.append(dict_[i])
        return result                    


        