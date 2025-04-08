# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        mid =(count//2)+1
        temp=head
        count=0
        
        while temp:
            if count==mid-1:
                return temp
            count+=1    
            print(temp.val)    
            temp=temp.next
            
                   
        