class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        depth = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # We are entering a deeper nested level
                depth += 1
            else:
                # We are stepping out of a nested level
                depth -= 1
                
                # If the previous character was '(', we found an innermost core "()"
                if s[i - 1] == '(':
                    # It contributes 2^depth to the total score
                    # 1 << depth is an efficient bitwise operation for 2^depth
                    score += 1 << depth
                    
        return score