class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_than_count = 0
        target_count = 0
        
        # Single pass to count smaller elements and target occurrences
        for num in nums:
            if num < target:
                less_than_count += 1
            elif num == target:
                target_count += 1
                
        # Generate the list of target indices
        # If target_count is 0, this list comprehension naturally returns an empty list []
        return [less_than_count + i for i in range(target_count)]