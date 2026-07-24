# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Iterate while there are nodes to process or a carry leftover
        while l1 is not None or l2 is not None or carry != 0:
            # Get the values from the current nodes (or 0 if end of list)
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate total sum for the current decimal place
            total = val1 + val2 + carry
            
            # Update the carry for the next decimal place
            carry = total // 10
            
            # Create a new node with the single-digit result and append it
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in l1 and l2 if available
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        # Return the actual head of the result list
        return dummy_head.next