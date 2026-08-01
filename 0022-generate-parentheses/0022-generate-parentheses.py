class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if the string length is 2*n, a valid combination is complete
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
                
            # If we still have open parentheses available, add one and recurse
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # If there are unmatched open parentheses, we can add a close parenthesis
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the backtracking with an empty string and 0 counts
        backtrack("", 0, 0)
        
        return result