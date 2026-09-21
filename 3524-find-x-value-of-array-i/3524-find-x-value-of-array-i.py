import collections

class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # result[x] will store the total number of subarrays with product % k == x
        result = [0] * k
        
        # dp stores the frequencies of (product % k) for subarrays ending at the current index
        dp = collections.defaultdict(int)
        
        for num in nums:
            next_dp = collections.defaultdict(int)
            
            # 1. Extend all existing subarrays ending at the previous element
            for remainder, count in dp.items():
                new_remainder = (remainder * num) % k
                next_dp[new_remainder] += count
                
            # 2. Start a new subarray containing only the current element
            next_dp[num % k] += 1
            
            # 3. Add the valid subarrays ending at the current index to our global results
            for remainder, count in next_dp.items():
                result[remainder] += count
                
            # 4. Move forward
            dp = next_dp
            
        return result