# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        
        # Step 1: Push the head of each list into the min-heap
        # We use 'i' as a unique tie-breaker just in case two nodes have the exact same value
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
                
        dummy_head = ListNode(-1)
        current = dummy_head
        
        # A counter to ensure every new node pushed into the heap has a unique tie-breaker id
        tie_breaker_id = len(lists)
        
        # Step 2 & 3: Pop the smallest node and push its next node
        while heap:
            val, _, smallest_node = heapq.heappop(heap)
            
            # Attach the smallest node to our merged list
            current.next = smallest_node
            current = current.next
            
            # If there is a next node in the same list, push it into the heap
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, tie_breaker_id, smallest_node.next))
                tie_breaker_id += 1
                
        return dummy_head.next