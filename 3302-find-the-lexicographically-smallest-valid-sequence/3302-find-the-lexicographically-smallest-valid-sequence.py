class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n = len(word1)
        m = len(word2)
        
        # right_match[k] stores the rightmost starting index in word1 
        # where the exact suffix word2[k:] can be found.
        # We append 'n' to handle the base case where the suffix is empty (j == m).
        right_match = [-1] * m + [n]
        
        j = m - 1
        # Precompute from right to left
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                right_match[j] = i
                j -= 1
                
        seq = []
        j = 0
        changed = False
        
        # Greedily pick the sequence from left to right
        for i in range(n):
            # Option 1: Exact match - always the best move
            if word1[i] == word2[j]:
                seq.append(i)
                j += 1
            # Option 2: Use our 1 allowed mismatch
            # Only valid if we haven't changed yet AND the rest of word2 can be matched perfectly
            elif not changed and right_match[j + 1] >= i + 1:
                seq.append(i)
                j += 1
                changed = True
                
            # If we've successfully matched all characters in word2
            if j == m:
                return seq
                
        # If the loop finishes without matching all characters
        return []