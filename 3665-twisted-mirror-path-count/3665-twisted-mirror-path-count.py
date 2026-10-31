class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # D[j] stores the valid paths entering from above for column j
        D = [0] * n
        
        for i in range(m):
            # R stores the valid paths entering from the left
            R = 0
            
            for j in range(n):
                # The starting cell initializes the paths
                if i == 0 and j == 0:
                    R = 1
                    D[j] = 1
                    continue
                    
                in_R = R
                in_D = D[j]
                
                if grid[i][j] == 0:
                    # Empty cell: Add incoming paths and pass the sum both ways
                    total = (in_R + in_D) % MOD
                    R = total
                    D[j] = total
                else:
                    # Mirror cell: Swap the directions of the incoming paths
                    R = in_D
                    D[j] = in_R
                    
        # The destination grid[m-1][n-1] is guaranteed to be 0 by the constraints, 
        # so R naturally holds the sum of all valid paths reaching the end.
        return R