"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None 
        stack = deque()
        current =root
        prev =None
        head = None
        while stack or current:
            if current:
                stack.append(current)
                current =current.left
            else:
                current =stack.pop()

                if prev:
                    prev.right = current
                    current.left =prev
                else:
                    head = current
                prev = current    

                current=current.right    

        head.left=prev
        prev.right=head
        return head        

        