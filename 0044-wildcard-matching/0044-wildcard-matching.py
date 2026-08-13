class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0
        p_idx = 0
        star_idx = -1
        match_idx = 0
        
        while s_idx < len(s):
            # Case 1: Exact match or '?' (matches any single character)
            if p_idx < len(p) and (p[p_idx] == '?' or s[s_idx] == p[p_idx]):
                s_idx += 1
                p_idx += 1
                
            # Case 2: Encounter a '*' wildcard
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                # Tentatively assume '*' matches zero characters
                p_idx += 1
                
            # Case 3: Mismatch, but we have a previous '*' to fallback on
            elif star_idx != -1:
                # Force the previous '*' to match one more character of 's'
                match_idx += 1
                s_idx = match_idx
                # Reset pattern pointer to right after the '*'
                p_idx = star_idx + 1
                
            # Case 4: Mismatch and no previous '*' to save us
            else:
                return False
                
        # Clean up any remaining '*' in the pattern
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        # If we consumed the entire pattern, it's a perfect match
        return p_idx == len(p)