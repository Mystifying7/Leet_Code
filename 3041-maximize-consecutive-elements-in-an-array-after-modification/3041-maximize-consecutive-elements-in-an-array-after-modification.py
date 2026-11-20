class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[x] = length of the longest consecutive sequence ending at x
        dp = {}
        
        for num in sorted(nums):
            # Update num + 1 first so we don't reuse the same element twice
            dp[num + 1] = dp.get(num, 0) + 1
            dp[num] = dp.get(num - 1, 0) + 1
            
        return max(dp.values())