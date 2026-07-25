class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return ""
            
        def expand_around_center(left, right):
            # Expand outwards as long as the characters match and indices are in bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the indices of the actual palindrome boundaries
            return left + 1, right - 1
            
        start, end = 0, 0
        
        for i in range(len(s)):
            # Find the longest odd-length palindrome centered at i
            left1, right1 = expand_around_center(i, i)
            # Find the longest even-length palindrome centered between i and i+1
            left2, right2 = expand_around_center(i, i + 1)
            
            # Update the global longest palindrome bounds if a new maximum is found
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
                
        return s[start:end + 1]