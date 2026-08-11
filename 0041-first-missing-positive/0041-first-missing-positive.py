class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Cyclic sort to place numbers in their correct indices
        for i in range(n):
            # While the number is strictly positive, fits within the array size,
            # and is not already resting at its correct index...
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap the current number to its correct target index
                # Note: We assign target index to a variable to avoid Python evaluation order bugs during swap
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Scan to find the first index that breaks the pattern
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If everything from 1 to n is in place, the answer is n + 1
        return n + 1