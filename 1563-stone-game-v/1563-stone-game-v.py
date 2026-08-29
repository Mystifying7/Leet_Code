import bisect

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n == 1:
            return 0
            
        # 1-indexed prefix sums for O(1) range queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
            
        # Initialize DP and running-maximum arrays
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        # Base case for subarrays of length 1
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        # Process subarrays by increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Binary search for the optimal splitting midpoint m
                target_sum = prefix[i] + (prefix[j+1] - prefix[i]) // 2
                idx = bisect.bisect_right(prefix, target_sum)
                
                m = min(idx - 2, j - 1)
                
                res = 0
                if m >= i:
                    sum_left = prefix[m+1] - prefix[i]
                    sum_total = prefix[j+1] - prefix[i]
                    
                    if sum_left * 2 == sum_total:
                        # Left and Right sums are equal, Alice checks both optimal paths
                        res = max(res, max_left[i][m])
                        res = max(res, max_right[m+1][j])
                    else:
                        # Left sum < Right sum, Alice can only keep Left up to index m
                        res = max(res, max_left[i][m])
                        # For split points after m, Left sum > Right sum, Alice keeps Right
                        if m + 2 <= j:
                            res = max(res, max_right[m+2][j])
                else:
                    # At the very first valid split, Left sum is already > Right sum
                    res = max(res, max_right[i+1][j])
                    
                dp[i][j] = res
                
                # Update prefix maximums for future larger subarrays
                current_sum = prefix[j+1] - prefix[i]
                max_left[i][j] = max(max_left[i][j-1], current_sum + dp[i][j])
                max_right[i][j] = max(max_right[i+1][j], current_sum + dp[i][j])
                
        return dp[0][n-1]