class Solution(object):
    def longestCommonPrefix(self, strs):
        # If the list is empty, there is no common prefix
        if not strs:
            return ""
            
        # Assume the first string is the common prefix to start
        prefix = strs[0]
        
        # Compare the prefix with each subsequent string
        for s in strs[1:]:
            # While the current string does not start with the prefix
            while not s.startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If the prefix becomes empty, there is no common prefix at all
                if not prefix:
                    return ""
                    
        return prefix