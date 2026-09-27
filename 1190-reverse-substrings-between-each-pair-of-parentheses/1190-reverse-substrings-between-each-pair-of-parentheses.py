class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        pair = {}
        stack = []
        
        # Step 1: Map matching parentheses to each other
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        i = 0
        direction = 1
        
        # Step 2: Traverse using the "Wormhole" technique
        while i < n:
            if s[i] == '(' or s[i] == ')':
                # Teleport to the matching bracket and reverse reading direction
                i = pair[i]
                direction = -direction
            else:
                # Add standard characters to the result
                res.append(s[i])
            
            # Move the pointer in the current direction
            i += direction
            
        return "".join(res)