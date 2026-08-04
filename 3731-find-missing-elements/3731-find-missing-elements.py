class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # If the list is too small to have missing numbers between bounds
        if len(nums) < 2:
            return []
            
        # Determine the boundaries of the original range
        min_val = min(nums)
        max_val = max(nums)
        
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        missing_elements = []
        
        # Iterate strictly between the minimum and maximum values
        for i in range(min_val + 1, max_val):
            # If the number is not in the set, it's missing
            if i not in num_set:
                missing_elements.append(i)
                
        return missing_elements