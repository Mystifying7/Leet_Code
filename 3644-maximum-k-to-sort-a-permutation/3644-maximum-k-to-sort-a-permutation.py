class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        
        for i, x in enumerate(nums):
            # If the element is not in its correct sorted position
            if i != x:
                # Accumulate the bitwise AND of all out-of-place elements
                ans &= x
                
        # If the array was already perfectly sorted, ans remains -1
        # The problem dictates returning 0 in this case.
        return max(ans, 0)