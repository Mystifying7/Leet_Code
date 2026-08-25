class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Convert list to a set for O(1) lookups
        nums_set = set(nums)
        
        # Step 2: Start checking multiples from 1 * k
        multiple = k
        
        # Step 3: Keep incrementing by k until we find a missing number
        while multiple in nums_set:
            multiple += k
            
        return multiple