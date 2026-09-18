class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        
        # Step 1: Record the first and last occurrences of each character
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        intervals = []
        
        # Step 2: Expand intervals for each unique character
        for char in first:
            start = first[char]
            right = last[char]
            
            valid = True
            j = start
            
            while j <= right:
                # If a character inside our interval started earlier than our current 'start',
                # this interval is not the tightest valid boundary. Discard it.
                if first[s[j]] < start:
                    valid = False
                    break
                
                # Expand the right boundary if needed
                right = max(right, last[s[j]])
                j += 1
                
            if valid:
                intervals.append((start, right))
                
        # Step 3: Greedy interval scheduling
        # Sort intervals by their end index to maximize the count and minimize length
        intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        
        for start, end in intervals:
            # If the current valid substring doesn't overlap with the last chosen one
            if start > last_end:
                res.append(s[start:end + 1])
                last_end = end
                
        return res