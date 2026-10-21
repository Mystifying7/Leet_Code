class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # Check if the string is already sorted
        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i+1]:
                is_sorted = False
                break
                
        if is_sorted:
            return 0
            
        # If length is 2 and it's not sorted, proper substrings are length 1 (useless)
        if n <= 2:
            return -1
            
        min_s = min(s)
        max_s = max(s)
        
        # Check if 1 operation is sufficient
        if s[0] == min_s or s[-1] == max_s:
            return 1
            
        # Check if it strictly requires 3 operations
        # This happens ONLY when s[0] is the UNIQUE maximum and s[-1] is the UNIQUE minimum
        if s[0] == max_s and s.count(max_s) == 1 and s[-1] == min_s and s.count(min_s) == 1:
            return 3
            
        # Otherwise, 2 operations are always sufficient and optimal
        return 2