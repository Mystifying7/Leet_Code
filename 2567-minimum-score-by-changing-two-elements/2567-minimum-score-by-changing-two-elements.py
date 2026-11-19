import heapq

class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the 3 smallest and 3 largest elements in O(N) time
        # small = [min1, min2, min3]
        # large = [max1, max2, max3]
        small = heapq.nsmallest(3, nums)
        large = heapq.nlargest(3, nums)
        
        # Evaluate the 3 possible ways to shrink the range by changing 2 elements:
        # 1. Change 2 smallest -> max1 - min3
        # 2. Change 2 largest  -> max3 - min1
        # 3. Change 1 smallest & 1 largest -> max2 - min2
        return min(
            large[0] - small[2],
            large[2] - small[0],
            large[1] - small[1]
        )