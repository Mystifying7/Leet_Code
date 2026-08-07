class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def findBound(is_first):
            left = 0
            right = len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        # Target found, but keep looking left for the first occurrence
                        right = mid - 1
                    else:
                        # Target found, but keep looking right for the last occurrence
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # If the array is empty, we can exit early
        if not nums:
            return [-1, -1]
            
        first_pos = findBound(True)
        
        # If the first position is -1, the target isn't in the array at all
        if first_pos == -1:
            return [-1, -1]
            
        last_pos = findBound(False)
        
        return [first_pos, last_pos]