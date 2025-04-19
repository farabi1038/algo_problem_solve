"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.cloned_nodes ={}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None :
            return None

        if node in self.cloned_nodes:
            return self.cloned_nodes[node]
        
        clone =Node(node.val)
        self.cloned_nodes[node]=clone

        for ngh in node.neighbors:
            clone.neighbors.append(self.cloneGraph(ngh))
        return clone            