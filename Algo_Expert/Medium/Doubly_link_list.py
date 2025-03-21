#Doubly link list implementation


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head=node
            self.tail=node
            return
            
        self.insertBefore(self.head,node )
        pass

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
            return
            
            
        self.insertAfter(self.tail,node )
        pass

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert ==self.head and nodeToInsert ==self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev=node.prev
        nodeToInsert.next=node
        if node.prev is None:
            self.head =nodeToInsert
        else:
            node.prev.next =nodeToInsert
        node.prev= nodeToInsert   
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert ==self.head and nodeToInsert ==self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev=node
        nodeToInsert.next=node.next
        if node.next is None:
            self.tail =nodeToInsert
        else:
            node.next.prev =nodeToInsert
        node.next= nodeToInsert   
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position==1:
            self.setHead(nodeToInsert)
            return
        node=self.head
        current=1
        while node is not None and current!=position:
            node=node.next
            current+=1
        if node is not None:
            self.insertBefore(node,nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        node=self.head
        while node is not None:
            nodetoRemove= node
            node=node.next
            if nodetoRemove.value==value:
                self.remove(nodetoRemove)    
            

    def remove(self, node):
        # Write your code here.
        if node==self.head:
            self.head=self.head.next
        if node==self.tail:
            self.tail=self.tail.prev
        if node.prev is not None:
            node.prev.next=node.next
            
        if node.next is not None:
            node.next.prev=node.prev
        node.prev=None
        node.next=None
        

    def containsNodeWithValue(self, value):
        # Write your code here.
        node=self.head
        while node is not None and node.value!= value:
            node=node.next
        return node is not None    
            
        pass
