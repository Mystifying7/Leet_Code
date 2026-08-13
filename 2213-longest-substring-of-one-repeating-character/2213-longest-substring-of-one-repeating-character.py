class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        k = 1
        while k < n:
            k *= 2
            
        # Segment tree arrays
        pref_len = [0] * (2 * k)
        pref_char = [''] * (2 * k)
        suff_len = [0] * (2 * k)
        suff_char = [''] * (2 * k)
        max_len = [0] * (2 * k)
        sz = [0] * (2 * k)
        
        # Initialize leaf nodes with the given string
        for i in range(n):
            idx = k + i
            pref_len[idx] = suff_len[idx] = max_len[idx] = sz[idx] = 1
            pref_char[idx] = suff_char[idx] = s[i]
            
        # Build the segment tree from bottom to top
        for i in range(k - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            
            sz[i] = sz[left] + sz[right]
            
            pref_char[i] = pref_char[left]
            pref_len[i] = pref_len[left]
            if pref_len[left] == sz[left] and pref_char[left] == pref_char[right]:
                pref_len[i] += pref_len[right]
                
            suff_char[i] = suff_char[right]
            suff_len[i] = suff_len[right]
            if suff_len[right] == sz[right] and suff_char[right] == suff_char[left]:
                suff_len[i] += suff_len[left]
                
            m = max_len[left] if max_len[left] > max_len[right] else max_len[right]
            if suff_char[left] == pref_char[right] and suff_char[left] != '':
                cross = suff_len[left] + pref_len[right]
                if cross > m:
                    m = cross
            max_len[i] = m

        ans = []
        # Process each query
        for i in range(len(queryIndices)):
            idx = queryIndices[i] + k
            char = queryCharacters[i]
            
            # Update the character at the leaf node
            pref_char[idx] = suff_char[idx] = char
            
            # Bubble up the changes to the root
            idx //= 2
            while idx > 0:
                left = 2 * idx
                right = 2 * idx + 1
                
                sz[idx] = sz[left] + sz[right]
                
                pref_char[idx] = pref_char[left]
                pref_len[idx] = pref_len[left]
                if pref_len[left] == sz[left] and pref_char[left] == pref_char[right]:
                    pref_len[idx] += pref_len[right]
                    
                suff_char[idx] = suff_char[right]
                suff_len[idx] = suff_len[right]
                if suff_len[right] == sz[right] and suff_char[right] == suff_char[left]:
                    suff_len[idx] += suff_len[left]
                    
                m = max_len[left] if max_len[left] > max_len[right] else max_len[right]
                if suff_char[left] == pref_char[right] and suff_char[left] != '':
                    cross = suff_len[left] + pref_len[right]
                    if cross > m:
                        m = cross
                max_len[idx] = m
                
                idx //= 2
                
            # The maximum sequence length after the update resides at the root (index 1)
            ans.append(max_len[1])
            
        return ans