class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else: # char == '*'
                # Treat '*' as ')' for the minimum, and '(' for the maximum
                min_open -= 1
                max_open += 1
            
            # If the absolute maximum possible open parentheses is negative,
            # it means there are too many ')' to ever be balanced.
            if max_open < 0:
                return False
            
            # We can't have negative open parentheses. If min_open drops below 0,
            # it means we counted too many '*' as ')'. We just treat them as empty
            # strings instead by resetting min_open to 0.
            if min_open < 0:
                min_open = 0
                
        # Valid if we can exactly close all open parentheses
        return min_open == 0