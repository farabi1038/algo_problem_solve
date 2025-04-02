"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        found = set()
        while p:
            found.add(p)
            p=p.parent
        while q:
            if q in found :
                return q
            q=q.parent        
        