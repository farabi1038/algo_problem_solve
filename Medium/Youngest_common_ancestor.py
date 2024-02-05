#Youngest_common_ancestor

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    history=set()
    while descendantOne and descendantOne.name:
        history.add(descendantOne.name)
        descendantOne = descendantOne.ancestor
        
    while descendantTwo and descendantTwo.name:
        
        
        if descendantTwo.name in history:
            print(descendantTwo.name)
            return descendantTwo
        descendantTwo = descendantTwo.ancestor
    return None    
        
        