class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        
        # Hash sets to track the numbers we've seen
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                    
                # Identify the 3x3 sub-box coordinate
                box_coord = (r // 3, c // 3)
                
                # Check for rule violations
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_coord]):
                    return False
                    
                # Record the value in our sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_coord].add(val)
                
        return True