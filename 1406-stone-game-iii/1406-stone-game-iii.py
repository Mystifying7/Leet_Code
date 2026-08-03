class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        
        # We pad the DP array with 3 extra zeros at the end. 
        # This prevents "index out of bounds" errors when looking ahead 1, 2, or 3 steps.
        dp = [0] * (n + 3)
        
        # Iterate backwards through the stones
        for i in range(n - 1, -1, -1):
            # Initialize with negative infinity so we can find the maximum
            dp[i] = float('-inf')
            current_take = 0
            
            # Try taking 1, 2, or 3 stones
            for k in range(3):
                # Ensure we don't go out of bounds of the actual stoneValue array
                if i + k < n:
                    current_take += stoneValue[i + k]
                    # Maximize the score difference: (stones taken) - (opponent's best future difference)
                    dp[i] = max(dp[i], current_take - dp[i + k + 1])
                    
        # dp[0] holds the max score difference for the first player (Alice)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"