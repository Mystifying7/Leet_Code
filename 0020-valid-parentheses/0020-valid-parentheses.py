class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        # Map closing brackets to their corresponding opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the topmost element if stack is not empty, else assign a dummy character
                top_element = stack.pop() if stack else '#'
                
                # If the mapped opening bracket doesn't match the top of the stack, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were successfully matched
        return not stack