# Sum_of_linked_list
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    list1=linkedtoList(linkedListOne)
    list2=linkedtoList(linkedListTwo)
    list1=list1[::-1]
    number1 = int(''.join(str(i) for i in list1))
    
    list2=list2[::-1]
    number2 = int(''.join(str(i) for i in list2))
    sum=number1+number2
    sum=str(sum)[::-1]
    final_list= createList(str(sum))
    
    

        
    return final_list

def linkedtoList(list):
    list1=[]
    node1=list
    while node1 is not None:
        list1.append(node1.value)
        node1=node1.next
    return list1    
def createList(sum):
    head=LinkedList(int(sum[0]))
    node=head
    for i in range(1,len(sum)):
         
        node1=LinkedList(int(sum[i]))
        node.next=node1
        node=node.next
    return head    
            
            
    
    
        
    