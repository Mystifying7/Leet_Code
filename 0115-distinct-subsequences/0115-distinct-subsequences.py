class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # If the target is longer than the source, it's impossible to form
        if n > m:
            return 0
            
        # dp[j] stores the number of distinct subsequences forming target prefix t[0...j-1]
        dp = [0] * (n + 1)
        
        # Base case: 1 way to form an empty string (by deleting everything)
        dp[0] = 1
        
        # Iterate through the characters of source string s
        for i in range(1, m + 1):
            # Iterate backwards through target string t to avoid overwriting needed values
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, add the ways to form the prefix without this char
                    dp[j] += dp[j - 1]
                    
        return dp[n]