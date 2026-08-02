# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge cases at the head
        dummy = ListNode(-1)
        dummy.next = head
        
        # prev will always point to the node immediately before the pair we are swapping
        prev = dummy
        
        while prev.next is not None and prev.next.next is not None:
            # Identify the two nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Perform the swap by updating the three necessary pointers
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the prev pointer forward to the end of the newly swapped pair
            prev = first
            
        return dummy.next