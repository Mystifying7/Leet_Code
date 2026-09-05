class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Precompute the minimums from right to left in O(N)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
            
        # Step 2: Iterate left to right, tracking the running maximum in O(N)
        prefix_max = float('-inf')
        
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            
            # Step 3: Evaluate the condition in O(1) time per index
            instability_score = prefix_max - suffix_min[i]
            if instability_score <= k:
                return i
                
        # If no stable index is found
        return -1