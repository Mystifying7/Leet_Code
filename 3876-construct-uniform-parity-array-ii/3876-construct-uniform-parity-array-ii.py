class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_val = min(nums1)
        
        # If the absolute minimum element is odd, we can make all elements odd
        if min_val % 2 != 0:
            return True
            
        # If the minimum element is even, it cannot be made odd.
        # Thus, we can only succeed if ALL elements in the array are already even.
        for num in nums1:
            if num % 2 != 0:
                return False
                
        return True