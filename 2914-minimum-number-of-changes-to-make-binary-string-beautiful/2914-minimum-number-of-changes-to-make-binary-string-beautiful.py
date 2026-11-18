class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        changes = 0
        
        # Step through the string checking every non-overlapping pair
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                changes += 1
                
        return changes