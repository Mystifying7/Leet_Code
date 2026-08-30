class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
            
        # Step 1: Find the indices of the minimum and maximum elements
        min_idx = 0
        max_idx = 0
        
        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
                
        # Ensure 'left' is the smaller index and 'right' is the larger index
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        
        # Step 2: Calculate the cost of the three different strategies
        # Strategy 1: Delete entirely from the front
        front_only = right + 1
        
        # Strategy 2: Delete entirely from the back
        back_only = n - left
        
        # Strategy 3: Delete the left element from the front and the right element from the back
        both_sides = (left + 1) + (n - right)
        
        # Step 3: Return the minimum of the three strategies
        return min(front_only, back_only, both_sides)