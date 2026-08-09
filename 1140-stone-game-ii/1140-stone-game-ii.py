class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        
        # Suffix sums array to quickly get total stones from index i to the end
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, M):
            # Base case: if all remaining piles can be taken in one turn
            if i + 2 * M >= n:
                return suffix_sum[i]
                
            if (i, M) in memo:
                return memo[(i, M)]
                
            max_stones = 0
            
            # Try taking X piles where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                next_M = max(M, X)
                # Current player's score = total remaining - opponent's best score from next state
                stones = suffix_sum[i] - dp(i + X, next_M)
                max_stones = max(max_stones, stones)
                
            memo[(i, M)] = max_stones
            return max_stones
            
        return dp(0, 1)