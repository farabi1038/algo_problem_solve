# This is an input class. Do not edit. 
#Remove_kth_node_from_the_end
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    
    realK=nodeCounter(head)-k
    
    
    if realK==0:
        if head.next is None:
            head.value=None
        else:
            
            head.value=head.next.value
            head.next=head.next.next
        return

        
    node=head
    pos=1
    
    while node is not None and pos<realK:
        node=node.next
        pos+=1
    if node is not None and node.next is not None:    
        node.next=node.next.next        
            
            
            
    
def nodeCounter(head):
    node =head
    count=0
    while node is not None:
        node=node.next
        count+=1
        
    return count    
    
