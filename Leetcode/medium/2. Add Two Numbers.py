# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=''
        list2=''
        while l1 is not None:
            list1+=str(l1.val)
            l1=l1.next
        while l2 is not None:
            list2+=str(l2.val)
            l2=l2.next
        list1=list1[::-1]
        list2=list2[::-1]
        total_sum = int(list1) if list1 else 0
        total_sum += int(list2) if list2 else 0


        total_string = str(total_sum)
        total_string=total_string[::-1]
        head=ListNode(int(total_string[0]))
        current =head
        for c in total_string[1:]:
            n=ListNode(int(c))
            current.next =n
            current = current.next

        return head    
        