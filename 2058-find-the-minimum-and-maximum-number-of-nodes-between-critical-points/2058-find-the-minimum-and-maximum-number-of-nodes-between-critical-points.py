
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # If the list has fewer than 3 nodes, there can be no critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        first_cp = -1
        last_cp = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        nxt = curr.next
        pos = 1
        
        # Traverse the list until 'nxt' reaches the end
        while nxt:
            # Check if the current node is a local maxima or local minima
            is_local_max = curr.val > prev.val and curr.val > nxt.val
            is_local_min = curr.val < prev.val and curr.val < nxt.val
            
            if is_local_max or is_local_min:
                if first_cp == -1:
                    # Record the first critical point
                    first_cp = pos
                else:
                    # Update minimum distance using the adjacent critical points
                    min_dist = min(min_dist, pos - last_cp)
                    
                # Always update the last seen critical point
                last_cp = pos
                
            # Shift pointers forward
            prev = curr
            curr = nxt
            nxt = nxt.next
            pos += 1
            
        # If we found at least two critical points, return the distances
        if first_cp != -1 and first_cp != last_cp:
            return [min_dist, last_cp - first_cp]
            
        # Otherwise, return [-1, -1]
        return [-1, -1]