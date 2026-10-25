class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            # If out of bounds or water, return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
                
            # Sink the current land to prevent revisiting
            grid[r][c] = 1
            
            # Explore all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # Step 1: Sink all islands connected to the left and right boundaries
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)
                
        # Step 1: Sink all islands connected to the top and bottom boundaries
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)
                
        # Step 2: Count the remaining interior closed islands
        closed_count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_count += 1
                    dfs(r, c)
                    
        return closed_count