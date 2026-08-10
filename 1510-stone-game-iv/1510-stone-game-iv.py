class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # dp[i] will be True if the current player can win with i stones remaining
        dp = [False] * (n + 1)
        
        # Build the dp array from 1 up to n
        for i in range(1, n + 1):
            # Check all possible valid square moves
            k = 1
            while k * k <= i:
                # If a move leaves the opponent in a losing state, the current player wins
                if not dp[i - k * k]:
                    dp[i] = True
                    # We found a winning strategy, no need to check other moves for this i
                    break
                k += 1
                
        # The result for n stones tells us if Alice (the first player) wins
        return dp[n]