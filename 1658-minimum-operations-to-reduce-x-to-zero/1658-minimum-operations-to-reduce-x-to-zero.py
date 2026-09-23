class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target_sum = sum(nums) - x
        
        # Edge case: If the total sum is less than x, it's impossible
        if target_sum < 0:
            return -1
            
        # Edge case: If the total sum is exactly x, we remove all elements
        if target_sum == 0:
            return len(nums)
            
        left = 0
        current_window_sum = 0
        max_subarray_len = -1
        
        # Sliding window to find the longest subarray summing to target_sum
        for right in range(len(nums)):
            current_window_sum += nums[right]
            
            # Shrink the window if the sum exceeds the target
            while current_window_sum > target_sum and left <= right:
                current_window_sum -= nums[left]
                left += 1
                
            # If we find a valid subarray, track its maximum length
            if current_window_sum == target_sum:
                max_subarray_len = max(max_subarray_len, right - left + 1)
                
        # If we never found a valid subarray, return -1
        if max_subarray_len == -1:
            return -1
            
        return len(nums) - max_subarray_len