class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # The number of available points in our transformed strictly-increasing space
        total_points = n + k - 1
        
        # We need to choose exactly 2k endpoints
        points_to_choose = 2 * k
        
        # If we need to choose more points than are available, it's impossible
        if points_to_choose > total_points:
            return 0
            
        # Manual combination computation for cross-version compatibility
        c = 1
        # Symmetry optimization: C(n, k) == C(n, n - k)
        points_to_choose = min(points_to_choose, total_points - points_to_choose)
        
        for i in range(points_to_choose):
            c = c * (total_points - i) // (i + 1)
            
        return c % MOD