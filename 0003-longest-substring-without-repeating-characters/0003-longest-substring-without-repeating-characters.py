class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is a duplicate and is inside the current window,
            # move the left pointer to the right of the old duplicate's index.
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            
            # Update the most recent index of the current character
            char_map[current_char] = right
            
            # Update the maximum length found so far
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length