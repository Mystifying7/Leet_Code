class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Array to store the number of distinct subsequences ending with each character
        ends_with = [0] * 26
        total = 0
        
        for char in s:
            idx = ord(char) - ord('a')
            
            # The new subsequences ending with 'char' include all previous subsequences 
            # with 'char' appended, plus the single character 'char' itself.
            new_count = (total + 1) % MOD
            
            # Add the newly formed subsequences to the total, but subtract the 
            # previously counted ones that also ended with 'char' to prevent duplicates.
            total = (total + new_count - ends_with[idx]) % MOD
            
            # Update the record for the current character
            ends_with[idx] = new_count
            
        return total