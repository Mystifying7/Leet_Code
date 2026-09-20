class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_degree = 0
        
        # enumerate(s, 1) provides a 1-based index automatically
        for i, char in enumerate(s, 1):
            # Calculate the reversed alphabet index ('a' = 26, 'b' = 25, ..., 'z' = 1)
            rev_index = 26 - (ord(char) - ord('a'))
            
            # Multiply by the string position and add to the total
            total_degree += rev_index * i
            
        return total_degree