# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Check if there are k nodes left to reverse
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse the k nodes
            # prev starts as group_next so the tail of the reversed group connects to the rest of the list
            prev = group_next
            curr = group_prev.next
            
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # Wire the reversed group back into the main list
            temp = group_prev.next
            group_prev.next = kth
            
            # Advance group_prev to the end of the newly reversed group
            group_prev = temp
            
        return dummy.next
        
    def getKthNode(self, curr, k):
        """Helper function to find the k-th node from the current node."""
        while curr is not None and k > 0:
            curr = curr.next
            k -= 1
        return curr