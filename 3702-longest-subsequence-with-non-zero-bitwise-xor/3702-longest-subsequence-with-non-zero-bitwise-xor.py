class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        has_non_zero = False
        
        # Calculate the total XOR and check for any non-zero element
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        # Case 1: The entire array has a non-zero XOR
        if total_xor != 0:
            return len(nums)
            
        # Case 2: The total XOR is 0, but we can remove one non-zero element
        if has_non_zero:
            return len(nums) - 1
            
        # Case 3: The array is full of zeros
        return 0