class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        valid_islands = 0
        
        for i in range(m):
            for j in range(n):
                # If we find an unvisited land cell, it's the start of a new island
                if grid[i][j] > 0:
                    current_island_sum = 0
                    stack = [(i, j)]
                    
                    # Add the initial cell's value and mark it as visited by sinking it
                    current_island_sum += grid[i][j]
                    grid[i][j] = 0 
                    
                    # Traverse the entire connected component
                    while stack:
                        r, c = stack.pop()
                        
                        # Explore all 4 adjacent directions
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            
                            # If the neighbor is within bounds and is land
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                current_island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                stack.append((nr, nc))
                                
                    # After fully exploring the island, check if the sum is divisible by k
                    if current_island_sum % k == 0:
                        valid_islands += 1
                        
        return valid_islands