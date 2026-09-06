class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        
        # Sets to track where queens are already placed
        cols = set()
        pos_diag = set()  # Tracks r + c
        neg_diag = set()  # Tracks r - c
        
        def backtrack(r, current_board):
            # Base case: All N queens have been placed successfully
            if r == n:
                res.append(current_board)
                return
                
            for c in range(n):
                # Check if the current square is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                    
                # Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Format the current row string
                row_str = "." * c + "Q" + "." * (n - c - 1)
                
                # Move to the next row
                backtrack(r + 1, current_board + [row_str])
                
                # Backtrack: Remove the queen and try the next column
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        # Start backtracking from row 0 with an empty board
        backtrack(0, [])
        return res