class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        
        # If the needle is longer than the haystack, it cannot be found
        if m > n:
            return -1
            
        # Iterate through the haystack checking substrings of length m
        for i in range(n - m + 1):
            # If the current substring matches the needle, return the starting index
            if haystack[i:i + m] == needle:
                return i
                
        # If no match is found after checking all possible windows, return -1
        return -1