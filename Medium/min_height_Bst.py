#min_height_Bst


def minHeightBst(array):
    return construct(array,None,0,len(array)-1)

def construct(array,bst,startIdx,endIdx):
    if startIdx>endIdx:
        return
    mid = (startIdx+endIdx)//2
    bstNode=BST(array[mid])
    if bst is None:
        bst =bstNode
    else :
        if array[mid]<bst.value:
            bst.left =bstNode
            bst=bst.left
        else:
            bst.right =bstNode
            bst=bst.right
    construct(array,bst,startIdx,mid-1)
    construct(array,bst,mid+1,endIdx)
    return bst
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)



def minHeightBst(array):
    return construct(array,None,0,len(array)-1)

def construct(array,bst,startIdx,endIdx):
    if startIdx>endIdx:
        return
    mid = (startIdx+endIdx)//2
    if bst is None:
            bst=BST(array[mid])
    else:
            bst.insert(array[mid])
    construct(array,bst,startIdx,mid-1)
    construct(array,bst,mid+1,endIdx)
    return bst
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)