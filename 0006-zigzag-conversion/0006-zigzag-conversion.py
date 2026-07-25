class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If the zigzag pattern doesn't alter the string, return it immediately
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create an array of strings to represent each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through the string and place characters in the correct row
        for char in s:
            rows[current_row] += char
            
            # Reverse direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move to the next row
            current_row += 1 if going_down else -1
            
        # Concatenate all rows to form the final string
        return "".join(rows)