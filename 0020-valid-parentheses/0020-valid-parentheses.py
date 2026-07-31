class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Map closing brackets to their matching opening brackets
        matching_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_map:
                # If stack is not empty and top matches, pop it
                if stack and stack[-1] == matching_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0