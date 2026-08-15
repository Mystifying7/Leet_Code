class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_len = 0
        freq = {}
        
        for right in range(len(s)):
            char = s[right]
            
            # Expand the window by adding the current character
            freq[char] = freq.get(char, 0) + 1
            
            # If the frequency exceeds 2, shrink the window from the left
            while freq[char] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
                
            # Update the maximum valid window length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len