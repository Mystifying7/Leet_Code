class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        # Initialize an (m+1) x (n+1) grid with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns that can match an empty string (e.g., "a*", "a*b*")
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match or pattern has a '.', carry over the previous state
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # If pattern has a '*', we have two choices
                elif p[j - 1] == '*':
                    # Choice 1: Treat '*' as zero occurrences of the preceding character
                    dp[i][j] = dp[i][j - 2]
                    
                    # Choice 2: If the preceding character matches the current string character,
                    # treat '*' as one or more occurrences
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]