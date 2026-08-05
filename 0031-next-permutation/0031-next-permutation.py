class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Step 1: Find the pivot (first decreasing element from the right)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # If the array is not entirely in descending order
        if i >= 0:
            # Step 2: Find the successor (element just larger than the pivot from the right)
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
                
            # Step 3: Swap the pivot and the successor
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 4: Reverse the suffix starting exactly after the pivot index
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1