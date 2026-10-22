class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        zero = nums.index(0)
        
        def check(step):
            # Check if traversing the array from 'zero' by 'step' gives a valid sorted sequence
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True
            
        ans = float('inf')
        
        # Scenario 1: The array is an ascending cyclic shift
        if check(1):
            # Option A: Rotate left until 0 is at the start
            ans = min(ans, zero)
            # Option B: Reverse, rotate left, then reverse back
            ans = min(ans, n - zero + 2)
            
        # Scenario 2: The array is a descending cyclic shift
        if check(-1):
            # Option A: Rotate left to move 0 to the end, then reverse
            ans = min(ans, zero + 2)
            # Option B: Reverse the array first, then rotate left
            ans = min(ans, n - zero)
            
        return ans if ans != float('inf') else -1