#BFS using name and child

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        Q=deque([self])
        while len(Q)>0:
            current=Q.popleft()
            array.append(current.name)
            Q.extend(current.children)
        return array    

    
        
        pass
