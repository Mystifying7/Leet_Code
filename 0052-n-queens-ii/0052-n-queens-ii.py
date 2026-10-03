class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using a list to hold the count allows us to update it inside the nested function 
        # without running into scope issues on older Python 2/3 environments (bypassing 'nonlocal').
        count = [0]
        
        cols = set()
        main_diagonals = set()  # Tracks row - col
        anti_diagonals = set()  # Tracks row + col
        
        def backtrack(row):
            # If we've successfully placed a queen in every row, we found a solution
            if row == n:
                count[0] += 1
                return
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if the square is under attack
                if col in cols or (row - col) in main_diagonals or (row + col) in anti_diagonals:
                    continue
                
                # Mark the column and diagonals as under attack
                cols.add(col)
                main_diagonals.add(row - col)
                anti_diagonals.add(row + col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Backtrack: remove the queen and free up the column and diagonals
                cols.remove(col)
                main_diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
                
        # Start the backtracking process from the first row (index 0)
        backtrack(0)
        
        return count[0]