class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            current_num = nums[right]
            
            # Add the current number to our frequency map
            freq[current_num] = freq.get(current_num, 0) + 1
            
            # If the frequency exceeds k, shrink the window from the left
            while freq[current_num] > k:
                left_num = nums[left]
                freq[left_num] -= 1
                left += 1
                
            # Update the maximum valid window length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len