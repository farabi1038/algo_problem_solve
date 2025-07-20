import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # A min-heap will store tuples: (node's value, list index, node itself)
        # The list index acts as a tie-breaker if values are equal.
        min_heap = []
        for i, head_node in enumerate(lists):
            if head_node:
                heapq.heappush(min_heap, (head_node.val, i, head_node))

        # A dummy head helps simplify the code
        dummy_head = ListNode()
        current = dummy_head

        # Loop until the heap is empty
        while min_heap:
            # Pop the smallest element
            val, i, node = heapq.heappop(min_heap)
            
            # Append this node to the result list
            current.next = node
            current = current.next
            
            # If the popped node has a next element, push it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy_head.next
