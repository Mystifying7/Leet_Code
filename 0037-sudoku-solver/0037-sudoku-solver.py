class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Hash sets to keep track of digits we've already seen
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        empty_cells = []
        
        # Initial scan to populate the tracking sets and find all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[r // 3][c // 3].add(val)
                    
        def backtrack(idx):
            # Base case: we successfully filled all empty cells
            if idx == len(empty_cells):
                return True
                
            r, c = empty_cells[idx]
            
            # Try placing digits 1 through 9
            for digit in map(str, range(1, 10)):
                if (digit not in rows[r] and 
                    digit not in cols[c] and 
                    digit not in boxes[r // 3][c // 3]):
                    
                    # Place the digit and update the sets
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[r // 3][c // 3].add(digit)
                    
                    # Move to the next empty cell
                    if backtrack(idx + 1):
                        return True
                        
                    # Backtrack: undo the placement and try the next digit
                    board[r][c] = "."
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[r // 3][c // 3].remove(digit)
                    
            # If no digit 1-9 works, this path is invalid
            return False
            
        # Start the backtracking process from the first empty cell
        backtrack(0)