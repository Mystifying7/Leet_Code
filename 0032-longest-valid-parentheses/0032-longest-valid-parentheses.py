class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        max_len = 0
        
        # Pass 1: Left to right scan
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            
            # Valid balanced substring found
            if left == right:
                max_len = max(max_len, 2 * right)
            # Invalidated by too many closing parentheses
            elif right > left:
                left = right = 0
                
        # Reset counters for the reverse pass
        left = right = 0
        
        # Pass 2: Right to left scan
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            
            # Valid balanced substring found
            if left == right:
                max_len = max(max_len, 2 * left)
            # Invalidated by too many opening parentheses
            elif left > right:
                left = right = 0
                
        return max_len