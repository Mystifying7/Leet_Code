class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Target found
            if nums[mid] == target:
                return mid
            # Target is larger, search the right half
            elif nums[mid] < target:
                left = mid + 1
            # Target is smaller, search the left half
            else:
                right = mid - 1
                
        # left pointer will naturally be at the correct insertion index
        return left