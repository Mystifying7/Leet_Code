class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        
        # current_prefix starts as the sum of the entire array (P_{n-1})
        current_prefix = sum(stones)
        
        # Base case: picking the entire array ends the game
        dp = current_prefix
        
        # Evaluate from right to left, down to index 1
        for i in range(n - 1, 1, -1):
            # Roll back the prefix sum to P_{i-1}
            current_prefix -= stones[i]
            
            # Transition: max(Skip current index, Take current index)
            dp = max(dp, current_prefix - dp)
            
        return dp